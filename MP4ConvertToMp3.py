from pytube import YouTube
from moviepy.editor import VideoFileClip

def descargar_youtube_a_mp3(url, nombre_archivo):
    # Descargar el video de YouTube
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(filename=nombre_archivo + ".mp4")

    # Convertir el video a formato MP3
    video_clip = VideoFileClip(nombre_archivo + ".mp4")
    video_clip.audio.write_audiofile(nombre_archivo + ".mp3")

    # Eliminar el archivo de video original
    video_clip.close()
    os.remove(nombre_archivo + ".mp4")

if __name__ == "__main__":
    import os

    # Ingresa la URL del video de YouTube y el nombre deseado para el archivo de salida
    url_youtube = "https://www.youtube.com/watch?v=example"
    nombre_salida = "cancion"

    # Llamada a la función para descargar y convertir
    descargar_youtube_a_mp3(url_youtube, nombre_salida)
