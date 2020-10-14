### Youtube Downloader ###
### Jared Corker ###

from pytube import YouTube

link = "https://www.youtube.com/watch?v=MZuZMrPhJk4&list=RDMZuZMrPhJk4&start_radio=1&ab_channel=MartyRayProject"
yt = YouTube(link)

#print("Title: ", yt.title)
print("Number of Views: ", yt.views)
print("Length in Seconds: ", yt.length)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download("./")
print("Download completed")