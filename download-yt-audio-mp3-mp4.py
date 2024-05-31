from pytube  import YouTube
from moviepy.editor import VideoFileClip

def download_video(url):
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        return True
    except Exception as e:
        return False
    
def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        audio_stream.download(output_path=".", filename="audio")
        
        # Convertir el archivo de audio de mp4 a mp3
        video_clip = VideoFileClip("audio.mp4")
        video_clip.audio.write_audiofile("audio.mp3")
        video_clip.close()
        return True
    except Exception as e:
        return False

# Escoger el video y audio a descargar
opcion = int(input('1. Descargar video\n2. Descargar audio\nOpción: '))
if opcion == 1:
    url = input('Enter the video URL: ')
    if download_video(url):
        print('Video downloaded successfully')
    else:
        print('Error downloading the video')
elif opcion == 2:
    url = input('Enter the audio URL: ')
    if download_audio(url):
        print('Audio downloaded successfully')
    else:
        print('Error downloading the audio')
