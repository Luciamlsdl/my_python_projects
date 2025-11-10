"""
Music Player 2.0
----------------
Versão aprimorada do seu player: agora com thread de reprodução,
barra de progresso, botões de próxima/anterior, modo aleatório
e salvamento de volume.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pygame
import os
import threading
import time
import random
import json


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player 2.0 🎵")
        self.root.geometry("480x400")

        # Inicializa o mixer
        pygame.mixer.init()

        # Estado do player
        self.playlist = []
        self.current_index = 0
        self.paused = False
        self.playing = False
        self.random_mode = False
        self.volume = tk.DoubleVar(value=0.5)

        # Arquivo de configuração
        self.config_file = "player_config.json"
        self.load_config()

        # Cria a interface
        self.create_widgets()
        self.update_progress_bar()

    # ---------------------------------------------------------------------
    # Interface
    def create_widgets(self):
        # Lista de músicas
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="#f0f0f0")
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.load_and_play_selected)

        # Label da música atual
        self.current_song_label = tk.Label(self.root, text="Nenhuma música tocando", bg="#ddd")
        self.current_song_label.pack(fill=tk.X, pady=5)

        # Barra de progresso
        self.progress = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, command=self.seek)
        self.progress.pack(fill=tk.X, padx=10)

        # Controles
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(pady=5)

        tk.Button(controls_frame, text="⏮", width=4, command=self.prev_track).grid(row=0, column=0, padx=5)
        self.play_button = tk.Button(controls_frame, text="▶️", width=4, command=self.toggle_play)
        self.play_button.grid(row=0, column=1, padx=5)
        tk.Button(controls_frame, text="⏸", width=4, command=self.pause_music).grid(row=0, column=2, padx=5)
        tk.Button(controls_frame, text="⏹", width=4, command=self.stop_music).grid(row=0, column=3, padx=5)
        tk.Button(controls_frame, text="⏭", width=4, command=self.next_track).grid(row=0, column=4, padx=5)
        tk.Button(controls_frame, text="🔀", width=4, command=self.toggle_random).grid(row=0, column=5, padx=5)
        tk.Button(controls_frame, text="📁", width=4, command=self.load_folder).grid(row=0, column=6, padx=5)

        # Controle de volume
        volume_frame = tk.Frame(self.root)
        volume_frame.pack(pady=5)
        tk.Label(volume_frame, text="🔊 Volume").pack(side=tk.LEFT)
        volume_scale = tk.Scale(volume_frame, variable=self.volume, from_=0.0, to=1.0,
                                resolution=0.01, orient=tk.HORIZONTAL, command=self.set_volume)
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
        cfg = {"volume": self.volume.get()}
        with open(self.config_file, "w") as f:
            json.dump(cfg, f)

    # ---------------------------------------------------------------------
    # Funções de reprodução
    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        self.playlist = [os.path.join(folder_path, f)
                         for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]
        self.playlist.sort()

        self.listbox.delete(0, tk.END)
        for song in self.playlist:
            self.listbox.insert(tk.END, os.path.basename(song))

        if self.playlist:
            self.current_index = 0
            self.play_song_threaded()

    def load_and_play_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            self.current_index = selected[0]
            self.play_song_threaded()

    def play_song_threaded(self):
        threading.Thread(target=self.play_music, daemon=True).start()

    def play_music(self):
        try:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
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

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        self.progress.set(0)
        self.current_song_label.config(text="Parado")

    def next_track(self):
        if not self.playlist:
            return
        if self.random_mode:
            self.current_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_song_threaded()

    def prev_track(self):
        if not self.playlist:
            return
        if self.random_mode:
            self.current_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_song_threaded()

    def toggle_random(self):
        self.random_mode = not self.random_mode
        state = "ativado" if self.random_mode else "desativado"
        messagebox.showinfo("Modo aleatório", f"Modo aleatório {state}")

    # ---------------------------------------------------------------------
    # Volume e progresso
    def set_volume(self, val):
        pygame.mixer.music.set_volume(float(val))
        self.save_config()

    def update_progress_bar(self):
        if self.playing and not self.paused:
            try:
                pos = pygame.mixer.music.get_pos() / 1000  # milissegundos -> segundos
                self.progress.set(int(pos))
            except:
                pass
        self.root.after(500, self.update_progress_bar)

    def seek(self, val):
        if self.playing:
            pygame.mixer.music.play(start=int(val))

# -------------------------------------------------------------------------
# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (app.save_config(), root.destroy()))
    root.mainloop()
