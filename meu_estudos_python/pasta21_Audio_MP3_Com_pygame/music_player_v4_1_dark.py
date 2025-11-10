"""
🎵 Music Player 4.1 - Tema Escuro
----------------------------------------
Versão em português com tema escuro moderno, usando Tkinter e Pygame.
Permite abrir pastas, tocar músicas MP3, ajustar volume e exibir capa do álbum.
"""

import tkinter as tk
from tkinter import filedialog, Listbox, Button, Label, Scale, DoubleVar, Canvas
from PIL import Image, ImageTk
import pygame
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎶 Tocador de Músicas 4.1 - Tema Escuro")
        self.root.geometry("420x340")
        self.root.config(bg="#121212")  # Fundo preto suave

        pygame.mixer.init()

        self.playlist = []
        self.current_index = 0
        self.paused = False
        self.volume = DoubleVar(value=0.5)
        self.background_image = None

        self.create_background()
        self.create_widgets()

    def create_background(self):
        """Canvas principal para exibir a capa."""
        self.canvas = Canvas(self.root, width=420, height=340, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.config(bg="#121212")

    def load_album_art(self, folder_path):
        """Carrega uma imagem de capa se houver na pasta."""
        cover_files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            and f.lower().startswith(('cover', 'folder', 'albumart'))
        ]

        if cover_files:
            try:
                image = Image.open(os.path.join(folder_path, cover_files[0]))
                image = image.resize((420, 340))
                self.background_image = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
            except Exception as e:
                print(f"⚠️ Erro ao carregar capa: {e}")
                self.canvas.config(bg="#121212")
        else:
            self.canvas.config(bg="#121212")

    def create_widgets(self):
        """Cria botões e controles do player."""
        # Lista de músicas
        self.listbox = Listbox(
            self.canvas, selectmode=tk.SINGLE, bg="#1E1E1E", fg="#FFFFFF",
            selectbackground="#00C853", selectforeground="black",
            relief="flat", font=("Arial", 9)
        )
        self.listbox.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)
        self.listbox.bind('<<ListboxSelect>>', self.load_and_play_selected)

        # Música atual
        self.current_song_label = Label(
            self.canvas, text="Nenhuma música selecionada",
            bg="#121212", fg="#E0E0E0", font=("Arial", 10, "bold")
        )
        self.current_song_label.place(relx=0.05, rely=0.52)

        # Botões
        self.btn_open = Button(
            self.canvas, text="📂 Pasta", bg="#00C853", fg="black",
            relief="flat", command=self.load_folder
        )
        self.btn_open.place(relx=0.05, rely=0.65, relwidth=0.25)

        self.btn_play = Button(
            self.canvas, text="▶️ Play", bg="#1E88E5", fg="white",
            relief="flat", command=self.play_music, state=tk.DISABLED
        )
        self.btn_play.place(relx=0.35, rely=0.65, relwidth=0.15)

        self.btn_pause = Button(
            self.canvas, text="⏸️ Pause", bg="#FFB300", fg="black",
            relief="flat", command=self.pause_music, state=tk.DISABLED
        )
        self.btn_pause.place(relx=0.52, rely=0.65, relwidth=0.18)

        self.btn_stop = Button(
            self.canvas, text="⏹️ Stop", bg="#E53935", fg="white",
            relief="flat", command=self.stop_music, state=tk.DISABLED
        )
        self.btn_stop.place(relx=0.73, rely=0.65, relwidth=0.18)

        # Controle de volume
        Label(self.canvas, text="🔊 Volume", bg="#121212", fg="#E0E0E0").place(relx=0.05, rely=0.80)
        volume_scale = Scale(
            self.canvas, variable=self.volume, from_=0.0, to=1.0, resolution=0.01,
            orient=tk.HORIZONTAL, bg="#121212", fg="#FFFFFF",
            troughcolor="#333333", highlightthickness=0, command=self.set_volume
        )
        volume_scale.place(relx=0.25, rely=0.78, relwidth=0.65)

    def load_folder(self):
        """Escolhe uma pasta com músicas MP3."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = sorted([
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith(".mp3")
            ])
            self.listbox.delete(0, tk.END)
            for song in self.playlist:
                self.listbox.insert(tk.END, os.path.basename(song))
            if self.playlist:
                self.load_album_art(folder_path)
                self.btn_play.config(state=tk.NORMAL)

    def load_and_play_selected(self, event):
        """Carrega e toca a música escolhida."""
        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            song_path = self.playlist[self.current_index]
            self.load_music(song_path)
            self.play_music()
            self.load_album_art(os.path.dirname(song_path))

    def load_music(self, file_path):
        """Carrega o arquivo MP3 selecionado."""
        try:
            pygame.mixer.music.load(file_path)
            self.current_song_label.config(text=os.path.basename(file_path))
            self.btn_play.config(state=tk.NORMAL)
            self.btn_pause.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.NORMAL)
        except pygame.error as e:
            tk.messagebox.showerror("Erro", f"Não foi possível carregar: {e}")

    def play_music(self):
        """Toca ou retoma a música."""
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.paused = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_music(self):
        """Pausa a reprodução."""
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        """Interrompe a música."""
        pygame.mixer.music.stop()
        self.paused = False

    def set_volume(self, val):
        """Ajusta o volume."""
        volume = float(val)
        pygame.mixer.music.set_volume(volume)


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
