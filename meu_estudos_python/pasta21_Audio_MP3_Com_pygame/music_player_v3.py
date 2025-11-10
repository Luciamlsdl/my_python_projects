"""
Music Player 3.0 🎨🎵
---------------------
Versão aprimorada com botões nomeados, capa do álbum,
janela colorida, e reprodução estável.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pygame
import os
import threading
import random
import json

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎶 Music Player Deluxe 🎶")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e2f")

        # Inicializa o mixer
        pygame.mixer.init()

        # Estado do player
        self.playlist = []
        self.current_index = 0
        self.paused = False
        self.playing = False
        self.random_mode = False
        self.volume = tk.DoubleVar(value=0.5)
        self.album_art = None

        # Arquivo de configuração
        self.config_file = "player_config.json"
        self.load_config()

        # Interface
        self.create_widgets()

        # Atualiza barra de progresso
        self.update_progress()

    # ---------------------------------------------------------------------
    # Interface
    def create_widgets(self):
        # Canvas de fundo (para cor e imagem)
        self.bg_canvas = tk.Canvas(self.root, width=600, height=500, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.bg_canvas.create_rectangle(0, 0, 600, 500, fill="#24243e", outline="")

        # Capa do álbum
        self.album_label = tk.Label(self.root, bg="#1e1e2f")
        self.album_label.place(relx=0.5, rely=0.15, anchor="center")

        # Lista de músicas
        self.listbox = tk.Listbox(self.root, bg="#2e2e48", fg="white", selectbackground="#5e5efc")
        self.listbox.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.35)
        self.listbox.bind("<<ListboxSelect>>", self.load_and_play_selected)

        # Música atual
        self.current_song_label = tk.Label(self.root, text="🎵 Nenhuma música tocando", bg="#1e1e2f", fg="white")
        self.current_song_label.place(relx=0.5, rely=0.83, anchor="center")

        # Controles
        controls = tk.Frame(self.root, bg="#1e1e2f")
        controls.place(relx=0.5, rely=0.9, anchor="center")

        btn_style = {"bg": "#5e5efc", "fg": "white", "relief": "flat", "width": 9, "height": 1}

        tk.Button(controls, text="Abrir Pasta", command=self.load_folder, **btn_style).grid(row=0, column=0, padx=5)
        tk.Button(controls, text="Anterior", command=self.prev_track, **btn_style).grid(row=0, column=1, padx=5)
        tk.Button(controls, text="Play", command=self.toggle_play, **btn_style).grid(row=0, column=2, padx=5)
        tk.Button(controls, text="Pause", command=self.pause_music, **btn_style).grid(row=0, column=3, padx=5)
        tk.Button(controls, text="Próxima", command=self.next_track, **btn_style).grid(row=0, column=4, padx=5)
        tk.Button(controls, text="Aleatória", command=self.toggle_random, **btn_style).grid(row=0, column=5, padx=5)

        # Volume
        volume_frame = tk.Frame(self.root, bg="#1e1e2f")
        volume_frame.place(relx=0.5, rely=0.75, anchor="center")
        tk.Label(volume_frame, text="🔊 Volume", bg="#1e1e2f", fg="white").pack(side=tk.LEFT)
        volume_scale = tk.Scale(volume_frame, variable=self.volume, from_=0.0, to=1.0, resolution=0.01,
                                orient=tk.HORIZONTAL, command=self.set_volume, bg="#1e1e2f", fg="white",
                                troughcolor="#5e5efc", highlightthickness=0)
        volume_scale.pack(side=tk.LEFT)
        self.set_volume(self.volume.get())

    # ---------------------------------------------------------------------
    # Configurações
    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    cfg = json.load(f)
                    self.volume.set(cfg.get("volume", 0.5))
            except:
                pass

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump({"volume": self.volume.get()}, f)

    # ---------------------------------------------------------------------
    # Músicas
    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        self.playlist = [os.path.join(folder_path, f)
                         for f in os.listdir(folder_path)
                         if f.lower().endswith(".mp3")]
        self.playlist.sort()

        self.listbox.delete(0, tk.END)
        for song in self.playlist:
            self.listbox.insert(tk.END, os.path.basename(song))

        if self.playlist:
            self.current_index = 0
            self.load_album_art(folder_path)
            self.play_song_threaded()

    def load_album_art(self, folder_path):
        cover_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))
                       and f.lower().startswith(('cover', 'folder', 'albumart'))]

        if cover_files:
            try:
                image = Image.open(os.path.join(folder_path, cover_files[0]))
                image = image.resize((180, 180))
                self.album_art = ImageTk.PhotoImage(image)
                self.album_label.config(image=self.album_art)
            except Exception as e:
                print(f"Erro ao carregar capa: {e}")
        else:
            self.album_label.config(image="", text="🎵")

    def load_and_play_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            self.current_index = selected[0]
            song_path = self.playlist[self.current_index]
            self.load_album_art(os.path.dirname(song_path))
            self.play_song_threaded()

    def play_song_threaded(self):
        threading.Thread(target=self.play_music, daemon=True).start()

    def play_music(self):
        try:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play(loops=0)
            self.playing = True
            self.paused = False
            song_name = os.path.basename(self.playlist[self.current_index])
            self.current_song_label.config(text=f"Tocando: {song_name}")
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(self.current_index)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao tocar música:\n{e}")

    def toggle_play(self):
        if not self.playlist:
            return
        if self.playing and not self.paused:
            self.pause_music()
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.play_song_threaded()

    def pause_music(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = random.randint(0, len(self.playlist) - 1) if self.random_mode else (self.current_index + 1) % len(self.playlist)
        self.play_song_threaded()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = random.randint(0, len(self.playlist) - 1) if self.random_mode else (self.current_index - 1) % len(self.playlist)
        self.play_song_threaded()

    def toggle_random(self):
        self.random_mode = not self.random_mode
        state = "ativado" if self.random_mode else "desativado"
        messagebox.showinfo("Modo Aleatório", f"Modo aleatório {state}")

    def set_volume(self, val):
        pygame.mixer.music.set_volume(float(val))
        self.save_config()

    # ---------------------------------------------------------------------
    # Atualizações contínuas
    def update_progress(self):
        if self.playing and not pygame.mixer.music.get_busy() and not self.paused:
            self.next_track()
        self.root.after(1000, self.update_progress)

# ---------------------------------------------------------------------
# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (app.save_config(), root.destroy()))
    root.mainloop()
