# YouTube Content on Telegram

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

### `requirements.txt`

```text
pytube
pyTelegramBotAPI
requests
schedule
google-api-python-client
```

### Açıklamalar

- **`pytube`**: YouTube videolarını indirmek için kullanılır.
- **`pyTelegramBotAPI`**: Telegram botları ile etkileşim kurmak için kullanılan kütüphanedir.
- **`requests`**: HTTP istekleri yapmak için kullanılır.
- **`schedule`**: Belirli aralıklarla işlerinizi planlamanızı sağlar.
- **`google-api-python-client`**: YouTube API ile etkileşimde bulunmak için kullanılır.
