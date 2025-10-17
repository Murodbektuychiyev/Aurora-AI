# Aurora AI

Aurora AI — bu Windows uchun ovozli yordamchi dastur. U sizning aytgan buyruqlaringizni ingliz tilida qabul qiladi va quyidagi oddiy vazifalarni bajaradi: ekran rasmini olish, ilovalarni ochish, tizim haqidagi ma'lumotlarni aytish.

## Xususiyatlari

- **Ekran rasmini olish**: Joriy ekraningizni saqlaydi va `screenshot.png` faylini yaratadi.
- **YouTube’ni ochish**: Google Chrome orqali [YouTube](https://youtube.com) saytini ochadi.
- **Chrome brauzerni ochish**: Google Chrome’ni ishga tushiradi.
- **VSCode’ni ochish**: Visual Studio Code’ni ishga tushiradi.
- **Vaqtni aytish**: Hozirgi tizim vaqtini ovoz orqali bildiradi.
- **Batareyani tekshirish**: Noutbuk batareya foizini bildiradi.
- **Yordam / Buyruqlar ro‘yxati**: Siz nima deyishingiz mumkinligini ko‘rsatadi.

## Talablar

- Python 3.11+
- Kutubxonalar:
  - `pyttsx3`
  - `pyautogui`
  - `speechrecognition`
  - `psutil`
  - `pyaudio` (yoki `sounddevice` mikrofon uchun)

Kerakli kutubxonalarni quyidagicha o‘rnatish mumkin:

```bash
pip install pyttsx3 pyautogui speechrecognition psutil pyaudio
