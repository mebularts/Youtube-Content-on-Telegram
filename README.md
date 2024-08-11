# YouTube Content on Telegram

[![Boyut](https://img.shields.io/github/repo-size/mebularts/Youtube-Content-on-Telegram?logo=git&logoColor=white&label=Boyut)](#)
[![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/mebularts/Youtube-Content-on-Telegram&title=Görüntülenme)](#)
<a href="https://t.me/mebularts" target="_blank"><img src="https://img.shields.io/badge/☕️-İletişime Geç-ffdd00" title="İletişime Geç" style="padding-left:5px;"></a>

[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://t.me/mebularts/)

[@mebularts](https://t.me/mebularts) tarafından <img href="https://t.me/mebularts" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/17fa94fb-0ae5-45a2-8313-2d3eedaf69db/d8fohut-eb4f893c-d1ad-4111-8e05-29993454b082.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE3ZmE5NGZiLTBhZTUtNDVhMi04MzEzLTJkM2VlZGFmNjlkYlwvZDhmb2h1dC1lYjRmODkzYy1kMWFkLTQxMTEtOGUwNS0yOTk5MzQ1NGIwODIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.J7M952F5dOS4-H45vJfTWA1yYE0ePYbTwamSfZHEQPY" width="30" height="30" /> ile yazılmıştır.



Bu proje, belirttiğiniz YouTube kanallarından videoları alarak Telegram kanalınıza göndermenizi sağlar. YouTube API'sinden video bilgilerini çeker, videoları indirir ve Telegram botu aracılığıyla gönderir.

## Özellikler

- Belirttiğiniz YouTube kanallarından en yeni videoları alır.
- Videoları Telegram kanalınıza gönderir.
- Gönderilen videoların geçmişini saklar. (Aynı videoları göndermemek için)

## Gereksinimler

Aşağıdaki Python kütüphanelerine ihtiyacınız olacak:

- `pytube` - YouTube videolarını indirmek için
- `telebot` - Telegram botu ile etkileşim için
- `requests` - HTTP istekleri yapmak için
- `schedule` - Belirli aralıklarla görevleri planlamak için
- `googleapiclient` - YouTube API ile etkileşim için

## Kurulum

Projenizi başlatmak için gerekli kütüphaneleri yüklemek için aşağıdaki adımları izleyin:

1. GitHub deposunu klonlayın:

   ```bash
   git clone https://github.com/mebularts/YouTube-Content-on-Telegram.git
   cd YouTube-Content-on-Telegram
   ```

2. Gerekli Python kütüphanelerini yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

3. `main.py` dosyasındaki `TOKEN`, `CHAT_ID`, `YOUTUBE_API_KEY` ve `CHANNELS_URL` değişkenlerini kendi bilgilerinizle güncelleyin.

4. Uygulamayı başlatın:

   ```bash
   python main.py
   ```

## Kullanım

`main.py` dosyasını çalıştırarak, belirlediğiniz Telegram kanalına belirli YouTube kanallarındaki videoları göndermeye başlayabilirsiniz. Kod, her 6 saatte bir kontrol eder ve uygun videoları gönderir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
```
