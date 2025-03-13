import youtube_dl
from youtube_dl.extractor import SoundcloudEmbedIE
import os
import requests
import re

class SoundCloud:
    def __init__(self):
        self.ydl_option = {
            'dumpjson': False,
            'exctact_flat': False,
        }

    def validate_url(self, url: str):
        if url.find("soundcloud") != -1:
            return True
        else:
            return False

    def delete_file(self, file: str):
        os.remove(file)

    def dowlnload(self, url: str):
        with youtube_dl.YoutubeDL(self.ydl_option) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            rename = f"{info_dict['title']}"
            try:
                os.rename(f"{filename}", f"{rename}.mp3")
                info_dict.update({"rename": f"{rename}.mp3"})
                print(f"1  {rename}.mp3")
                return info_dict
                
            except OSError:
                reg = re.compile('[^a-zA-Z ]')
                a = reg.sub('', rename)
                os.rename(f"{filename}", f"{a}.mp3")
                info_dict.update({"rename": f"{a}.mp3"})
                print(f"2  {rename}.mp3")
                return info_dict

def download_soundcloud_track(url, download_path="./downloads"):
    """
    Скачивает аудио с SoundCloud без API-ключа.

    :param url: Ссылка на трек SoundCloud
    :param download_path: Папка для сохранения
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Получаем HTML-страницу трека
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Ошибка доступа к треку.")
        return

    # Ищем прямую ссылку на аудиофайл
    match = re.search(r'"transcodings":\[(.*?)\]', response.text)
    if not match:
        print("Не удалось найти ссылку на аудиофайл.")
        return

    json_data = match.group(1)
    stream_url_match = re.search(r'"url":"(https://[^"]+)"', json_data)

    if not stream_url_match:
        print("Ошибка: потоковый URL не найден.")
        return

    stream_url = stream_url_match.group(1).replace("\\/", "/")  # Чистим ссылку

    # Получаем реальную ссылку на MP3
    stream_response = requests.get(stream_url, headers=headers)
    if stream_response.status_code != 200:
        print("Ошибка получения аудиопотока.")
        return

    mp3_url = re.search(r'"url":"(https://[^"]+)"', stream_response.text)
    if not mp3_url:
        print("Не удалось извлечь ссылку на MP3.")
        return

    mp3_url = mp3_url.group(1).replace("\\/", "/")

    # Загружаем аудиофайл
    os.makedirs(download_path, exist_ok=True)
    file_path = os.path.join(download_path, "track.mp3")

    print(f"Скачивание трека: {mp3_url}")
    mp3_data = requests.get(mp3_url, headers=headers).content

    with open(file_path, "wb") as f:
        f.write(mp3_data)

    print(f"Трек сохранён в: {file_path}")
