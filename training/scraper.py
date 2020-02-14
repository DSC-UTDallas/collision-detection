import pytube
from pytube import YouTube
import youtube_dl
import os
import cv2
print(cv2.__file__)

cwd = os.getcwd()
raw_dir = cwd + "\\raw"

# https://www.youtube.com/watch?v=NCmlbDaj-uE
# https://www.youtube.com/watch?v=rVssEL2jhu8
# https://www.youtube.com/watch?v=tDN-mwNSJc8

# don't use this. pytube doesn't work.
def dlv() :
    yt = YouTube("https://www.youtube.com/watch?v=tDN-mwNSJc8")
    print(yt.streams.all())
    stream = yt.streams.first()
    stream.download()

# use this.
def dlvydl():
    print(cwd)

    ydl_opts = {
        'outtmpl': cwd+'\\%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=NCmlbDaj-uE'])

#https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
def extract() :
    vidcap = cv2.cv2.VideoCapture('Car crashes caught on red light cameras from around New Jersey.mp4')
    success, image = vidcap.read()
    count = 0
    modocount = 0
    print(success)
    while success:
        success,image = vidcap.read()
        if (modocount % 15 == 0):
            print('Saving image')
            image = cv2.cv2.resize(image, (540, 360))
            cv2.cv2.imwrite("raw/img%d.jpg" % count, image)     
        print('Read a new frame: ', success, '. waiting with ', modocount)
        count += 1
        modocount += 1

if __name__ == "__main__":
    # dlvydl()
    extract()