"""
Faça um programa em python que abra um o audio de um arquivo MP3.
"""

# Este código esta em sua forma um pouco mais avançado usando a biblioteca pygame (para arquivos locais)


import tkinter as tk
from tkinter import filedialog, Listbox, Button, Label, Scale, DoubleVar, Canvas
from PIL import Image, ImageTk
import pygame
import os
import random
import threading
import time

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
        self.background_image = None
        self.background_label = None

        self.create_background()
        self.create_widgets()

    def create_background(self):
        self.background_canvas = Canvas(self.root, width=400, height=300)
        self.background_canvas.pack(fill="both", expand=True)

    def load_album_art(self, folder_path):
        cover_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f.lower().startswith(('cover', 'folder', 'albumart'))]
        if cover_files:
            try:
                image = Image.open(os.path.join(folder_path, cover_files[0]))
                resized_image = image.resize((self.root.winfo_width(), self.root.winfo_height()))
                self.background_image = ImageTk.PhotoImage(resized_image)
                self.background_canvas.create_image(0, 0, image=self.background_image, anchor="nw")
            except Exception as e:
                print(f"Erro ao carregar a capa do álbum: {e}")
        else:
            # Se não houver capa, pode definir um fundo padrão ou deixar sem imagem
            self.background_canvas.config(bg="lightgray") # Exemplo de fundo padrão

    def create_widgets(self):
        # Lista de músicas (agora criada no canvas)
        self.listbox = Listbox(self.background_canvas, selectmode=tk.SINGLE)
        self.listbox.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.5)
        self.listbox.bind('<<ListboxSelect>>', self.load_and_play_selected)

        # Label para a música atual (no canvas)
        self.current_song_label = Label(self.background_canvas, text="Nenhuma música selecionada", bg=self.background_canvas['bg'])
        self.current_song_label.place(relx=0.05, rely=0.57, relwidth=0.9, anchor="nw")

        # Controles (no canvas)
        controls_frame = tk.Frame(self.background_canvas, bg=self.background_canvas['bg'])
        controls_frame.place(relx=0.5, rely=0.65, anchor="n")

        Button(controls_frame, text="Abrir Pasta", command=self.load_folder).pack(side=tk.LEFT, padx=5)
        self.play_button = Button(controls_frame, text="Play", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=5)
        self.pause_button = Button(controls_frame, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = Button(controls_frame, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Controle de volume (no canvas)
        volume_frame = tk.Frame(self.background_canvas, bg=self.background_canvas['bg'])
        volume_frame.place(relx=0.5, rely=0.8, anchor="n")
        Label(volume_frame, text="Volume:", bg=self.background_canvas['bg']).pack(side=tk.LEFT)
        volume_scale = Scale(volume_frame, variable=self.volume, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, command=self.set_volume, bg=self.background_canvas['bg'])
        volume_scale.pack(side=tk.LEFT)

        # Bind para redimensionar a janela (para redimensionar o fundo)
        self.root.bind("<Configure>", self.resize_background)

    def resize_background(self, event):
        if self.background_image:
            resized_image = self.background_image._PhotoImage__photo.resize((event.width, event.height))
            self.background_image = ImageTk.PhotoImage(resized_image)
            self.background_canvas.create_image(0, 0, image=self.background_image, anchor="nw")
            # É importante reconfigurar os outros widgets para que fiquem visíveis sobre o novo fundo
            self.listbox.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.5)
            self.current_song_label.place(relx=0.05, rely=0.57, relwidth=0.9, anchor="nw")
            controls_frame = self.root.winfo_children()[2] # Encontrar o frame de controles (pode precisar ajuste)
            controls_frame.place(relx=0.5, rely=0.65, anchor="n")
            volume_frame = self.root.winfo_children()[3] # Encontrar o frame de volume (pode precisar ajuste)
            volume_frame.place(relx=0.5, rely=0.8, anchor="n")

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".mp3")])
            self.listbox.delete(0, tk.END)
            for song in self.playlist:
                self.listbox.insert(tk.END, os.path.basename(song))
            if self.playlist:
                self.load_album_art(folder_path)
                self.play_button.config(state=tk.NORMAL)

    def load_and_play_selected(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            current_song_path = self.playlist[self.current_index]
            self.load_music(current_song_path)
            self.play_music()
            self.load_album_art(os.path.dirname(current_song_path)) # Carrega a capa da pasta da música selecionada

    def load_music(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            self.current_song_label.config(text=os.path.basename(file_path), bg=self.background_canvas['bg'])
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