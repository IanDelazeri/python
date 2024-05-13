from pytube import YouTube
import os
from moviepy.editor import*
import glob

link = input('digite o link do video que você deseja: ')

yt = YouTube(link)

mp4 = VideoFileClip(os.path.join(YouTube))
print(' baixando....', yt.title)
print('-'*20)

resolucao = yt.streams.filter(progressive = True, file_extension = 'mp4'). order_by('resolution').desc().first()
resolucao.download()
print('download concluido !!!')

lista_mp4 = glob.glob('*.mp4')

for video in lista_mp4:
    print('Lendo arquivo mp4...')
    print('-'*20)
    mp4 = VideoFileClip(os.path.join(video))
    nome_mp3 = video[:-4]+'.mp3'
    print('Converterndo para mp3')
    mp4.audio.write_audiofile(os.path.join(nome_mp3))
    print('-'*20)
    print('converteu mp4' + video + 'para mp3' + nome_mp3)


