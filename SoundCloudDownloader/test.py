import eyed3
import urllib.request

audiofile = eyed3.load("D:\car s outside.mp3")
audiofile.initTag(version=(2, 3, 0))
audiofile.tag.artist = "Token Entry"
audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = "Various Artists"
audiofile.tag.title = "The Edge"
print(audiofile.tag)
audiofile.rename

response = urllib.request.urlopen("https://i1.sndcdn.com/artworks-RTaPbaSmO2c7zzTg-1ImXIg-original.jpg")
imagedata = response.read()
audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
audiofile.tag.save()