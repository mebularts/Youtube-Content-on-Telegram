import os
import re
import json
import pytube
import telebot
import requests
import schedule
import time
from googleapiclient.discovery import build
from pytube.exceptions import PytubeError, AgeRestrictedError

TOKEN = 'TELEGRAM_BOT_TOKEN'
CHAT_ID = '@telegramkanaliniz'
YOUTUBE_API_KEY = 'YOUTUBE_API_KEY'
CHANNELS_URL = 'https://siteadiniz.com/kanallar.json'
VIDEO_HISTORY_FILE = 'paylasilanlar.json'

bot = telebot.TeleBot(TOKEN)

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

if os.path.exists(VIDEO_HISTORY_FILE):
    with open(VIDEO_HISTORY_FILE, 'r') as f:
        video_history = json.load(f)
else:
    video_history = []

def save_video_history():
    with open(VIDEO_HISTORY_FILE, 'w') as f:
        json.dump(video_history, f)

def get_channel_ids():
    response = requests.get(CHANNELS_URL)
    data = response.json()
    return data['channels']

def get_video_urls(channel_id):
    video_urls = []
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=50,
        order='date'
    )
    response = request.execute()

    for item in response['items']:
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            if video_id not in video_history:
                title = item['snippet']['title']
                tags = item['snippet'].get('tags', [])
                url = f"https://www.youtube.com/watch?v={video_id}"
                
                duration = get_video_duration(video_id)
                
                # Ben shorts için kullanıyorum burada 60 saniye ve üzeri videoları almamasını istedim.
                if duration <= 60:
                    video_urls.append((video_id, title, tags, url))
    
    return video_urls

def get_video_duration(video_id):
    request = youtube.videos().list(
        part='contentDetails',
        id=video_id
    )
    response = request.execute()
    duration = response['items'][0]['contentDetails']['duration']
    
    match = re.match(r'PT(\d+)M(\d+)S', duration)
    if match:
        minutes = int(match.group(1)) if match.group(1) else 0
        seconds = int(match.group(2)) if match.group(2) else 0
        total_seconds = minutes * 60 + seconds
        return total_seconds
    else:
        return 0

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_and_send_video(video_id, title, tags, url):
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        cleaned_title = clean_filename(title)
        video_path = f"{cleaned_title}.mp4"
        stream.download(filename=video_path)
        
        with open(video_path, 'rb') as video_file:
            caption = f"{title}\n{' '.join(tags[:1])}"
            bot.send_video(CHAT_ID, video_file, caption=caption)
        
        os.remove(video_path)
        video_history.append(video_id)
        save_video_history()
    
    except (PytubeError, AgeRestrictedError) as e:
        print(f"Video indirilemedi {video_id}: {e}")
        pass

def check_channels_and_send_videos():
    channel_ids = get_channel_ids()
    for channel_id in channel_ids:
        video_urls = get_video_urls(channel_id)
        for video_id, title, tags, url in video_urls:
            download_and_send_video(video_id, title, tags, url)

# Burada kanalların kontrolünü kaç saate bir yapılacağını yazın (6)
schedule.every(6).hours.do(check_channels_and_send_videos)

check_channels_and_send_videos()

while True:
    schedule.run_pending()
    time.sleep(1)
