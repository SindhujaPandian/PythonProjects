import sys
from pytube import YouTube
path = 'C:/'

#link = input("Enter the youtube link that you need to download :  ")

try:
    youtube = YouTube("https://youtu.be/g_Bihjc5lqw")
    print("The object get created")
except:
    print(sys.exc_info()[0])
    print("There is some connection issues \nTry again later !!")
    sys.exit(0)
filters = youtube.streams.filter(progressive=True, file_extension='mp4')


filters.get_highest_resolution().download(output_path='C:/Users/elcot/Desktop', filename='yt_video.mp4')

print("The video downloaded successfully !!!")    
