import youtube_dl
from youtube_dl.extractor import SoundcloudEmbedIE
import os
import eyed3
import urllib.request
import re






class SoundCloud:
    def __init__(self):
        self.ydl_option = {
            'dumpjson': False,
            'exctact_flat': False,
            # 'outtmpl': "jama.mp3"
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
                
            
            
# sc = SoundCloud()
# url='https://on.soundcloud.com/Zjq3wdHECTRGtHwd9'
# info_dict = sc.dowlnload(url=url)
# print(info_dict)
# sc.show(info_dict=info_dict)