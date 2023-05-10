from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import zipfile
import os
from time import sleep

def remove_especial (old):
    new_string = old
    remover = ["\"", "/", "|" , "<", ">", "*", ":", "“", "?"]
    for x in remover:
        new_string = new_string.replace(x, '')
    return new_string


tipo = input('Digite como você quer baixar(video, musica ou playlist): ')

if tipo == 'musica':       
    yt = YouTube(input('Insira aqui seu link: '), use_oauth=True, allow_oauth_cache=True)
    #yt.streams.filter(only_audio=True, file_extension='mp3').first()
    #stream = yt.streams.get_audio_only()
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_lowest_resolution()
    titulo = remove_especial(yt.title)
    stream.download(filename=f"{titulo}.mp4")
    video = VideoFileClip(f'{titulo}.mp4')
    video.audio.write_audiofile(f'{titulo}.mp3')
    sleep(5)
    video.close()
    os.remove(f'{titulo}.mp4')


elif tipo == 'video':
    yt = YouTube(input('Insira aqui seu link: '))
    yt.streams.filter(progressive=True, resolution='2160p', file_extension='mp4')
    stream = yt.streams.get_by_itag(22)
    titulo = remove_especial(yt.title)
    stream.download(filename=f"{titulo}.mp4")


elif tipo == 'playlist':
    playlista = Playlist(input('Insira aqui seu link: '))
    for url in playlista.video_urls:
        yt = YouTube(url,use_oauth=True, allow_oauth_cache=True)
        stream = yt.streams.get_lowest_resolution()
        titulo = remove_especial(yt.title)
        stream.download(filename=f"{titulo}.mp4")
        video = VideoFileClip(f'{titulo}.mp4')
        video.audio.write_audiofile(f'{titulo}.mp3')
        sleep(3)
        video.close()
        os.remove(f'{titulo}.mp4')

 