import os
import glob
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Label, Entry, Button, Radiobutton, Style, Frame
from pytube import YouTube
from moviepy.editor import VideoFileClip

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Video to MP3 Converter")
        self.geometry("500x350")
        self.resizable(False, False)
        self.create_widgets()
        
    def create_widgets(self):
        style = Style()
        style.theme_use('clam')
        
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TRadiobutton", font=("Arial", 12))
        style.configure("TProgressbar", thickness=20)

        self.container = Frame(self, padding="20")
        self.container.pack(expand=True, fill=tk.BOTH)

        self.link_label = Label(self.container, text="Digite o link do vídeo:")
        self.link_label.pack(pady=(10, 5))

        self.link_entry = Entry(self.container, width=50, font=("Arial", 10))
        self.link_entry.pack(pady=5)

        self.download_choice = tk.StringVar(value="video")
        self.video_radio = Radiobutton(self.container, text="Download do vídeo", variable=self.download_choice, value="video")
        self.audio_radio = Radiobutton(self.container, text="Download apenas do áudio", variable=self.download_choice, value="audio")
        self.video_radio.pack(pady=5)
        self.audio_radio.pack(pady=5)

        self.download_button = Button(self.container, text="Baixar", command=self.download_and_convert, style="TButton")
        self.download_button.pack(pady=15)

        self.progress = Progressbar(self.container, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.percent_label = Label(self.container, text="0%", font=("Arial", 10))
        self.percent_label.pack(pady=5)
        
        self.status_label = Label(self.container, text="", wraplength=400)
        self.status_label.pack(pady=10)
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.update_idletasks()

    def download_and_convert(self):
        link = self.link_entry.get()
        if not link:
            messagebox.showerror("Erro", "Por favor, insira um link.")
            return

        try:
            yt = YouTube(link, on_progress_callback=self.on_progress)
            self.update_status(f'Baixando... {yt.title}')
            
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            stream.download()
            self.update_status('Download concluído!')

            download_type = self.download_choice.get()
            if download_type == "audio":
                self.convert_to_mp3()
            else:
                messagebox.showinfo("Sucesso", "Download do vídeo concluído!")

            self.ask_for_another_download()
        
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.progress['value'] = percentage_of_completion
        self.percent_label.config(text=f'{percentage_of_completion:.2f}%')
        self.update_status(f'Download: {percentage_of_completion:.2f}% concluído')
        self.update_idletasks()

    def convert_to_mp3(self):
        try:
            mp4_files = glob.glob('*.mp4')
            for video in mp4_files:
                self.update_status('Lendo arquivo mp4...')
                mp4 = VideoFileClip(os.path.join(video))
                mp3_filename = video[:-4] + '.mp3'
                self.update_status('Convertendo para mp3...')
                mp4.audio.write_audiofile(os.path.join(mp3_filename))
                self.update_status(f'Converteu {video} para {mp3_filename}')
                messagebox.showinfo("Sucesso", f'Conversão concluída! Arquivo salvo como {mp3_filename}')
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def ask_for_another_download(self):
        answer = messagebox.askyesno("Outro download", "Deseja fazer outro download?")
        if answer:
            self.link_entry.delete(0, tk.END)
            self.progress['value'] = 0
            self.percent_label.config(text="0%")
            self.status_label.config(text="")
        else:
            self.quit()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()
