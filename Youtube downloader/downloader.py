from pytube import YouTube
from pytube import Playlist
import zipfile
import os

def remove_especial (old):
    new_string = old
    remover = ["\"", "/", "|" , "<", ">", "*", ":", "“", "?"]
    for x in remover:
        new_string = new_string.replace(x, '')
    return new_string


tipo = input('Digite como você quer baixar(video, musica ou playlist): ')

if tipo == 'musica':       
    yt = YouTube(input('Insira aqui seu link: '))
    yt.streams.filter(only_audio=True)
    stream = yt.streams.get_audio_only()
    titulo = remove_especial(yt.title)
    stream.download(filename=titulo+".mp3")


elif tipo == 'video':
    yt = YouTube(input('Insira aqui seu link: '))
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_highest_resolution()
    titulo = remove_especial(yt.title)
    stream.download(filename=f"{titulo}.mp4")


elif tipo == 'playlist':
    playlista = Playlist(input('Insira aqui seu link: '))
    z = zipfile.ZipFile('playlist.zip', 'w', zipfile.ZIP_DEFLATED)
    for music in playlista.videos:
        music.streams.filter(only_audio=True)
        stream = music.streams.get_audio_only()
        titulo = remove_especial(music.title)
        stream.download(filename=titulo+".mp3")
        z.write(f'{titulo}.mp3')
        os.remove(f'{titulo}.mp3')
    z.close()
 