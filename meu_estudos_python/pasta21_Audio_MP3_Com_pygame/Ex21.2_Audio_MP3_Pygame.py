"""
Faça um programa em python que abra um o audio de um arquivo MP3.
"""

# Este código esta em sua forma avançada usando a biblioteca pygame (para arquivos locais)
# ESte código mostra como um código pode ir de um código simples a um código bem complexo  


import tkinter as tk
from tkinter import filedialog, Listbox, Button, Label, Scale, DoubleVar
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")

        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0
        self.paused = False
        self.volume = DoubleVar(value=0.5)

        self.create_widgets()

    def create_widgets(self):
        # Lista de músicas
        self.listbox = Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.load_and_play_selected)

        # Label para a música atual
        self.current_song_label = Label(self.root, text="Nenhuma música selecionada")
        self.current_song_label.pack()

        # Controles
        controls_frame = tk.Frame(self.root)
        controls_frame.pack()

        Button(controls_frame, text="Abrir Pasta", command=self.load_folder).pack(side=tk.LEFT, padx=5)
        self.play_button = Button(controls_frame, text="Play", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=5)
        self.pause_button = Button(controls_frame, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = Button(controls_frame, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Controle de volume
        volume_frame = tk.Frame(self.root)
        volume_frame.pack(pady=5)
        Label(volume_frame, text="Volume:").pack(side=tk.LEFT)
        volume_scale = Scale(volume_frame, variable=self.volume, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, command=self.set_volume)
        volume_scale.pack(side=tk.LEFT)

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".mp3")])
            self.listbox.delete(0, tk.END)
            for song in self.playlist:
                self.listbox.insert(tk.END, os.path.basename(song))
            if self.playlist:
                self.play_button.config(state=tk.NORMAL)

    def load_and_play_selected(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            self.load_music(self.playlist[self.current_index])
            self.play_music()

    def load_music(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            self.current_song_label.config(text=os.path.basename(file_path))
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
        except pygame.error as e:
            tk.messagebox.showerror("Erro ao carregar", f"Não foi possível carregar o arquivo: {e}")

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.paused = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False

    def set_volume(self, val):
        volume = float(val)
        pygame.mixer.music.set_volume(volume)

# Programa principal

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()