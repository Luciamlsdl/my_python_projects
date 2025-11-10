"""
Music Player 4.0 — Deluxe with visual equalizer
- Plays mp3 files from any folder or individual file
- Shows album art (cover*.jpg/png) when present
- Visual equalizer using numpy + pygame.sndarray (attempts to analyze audio samples)
- Falls back to a reactive animated visual when sample analysis isn't available
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pygame
import os
import threading
import random
import json
import numpy as np
import time

# ---------- CONFIG ----------
CONFIG_FILE = "player_config_v4.json"
EQ_BARS = 12           # number of equalizer bars
EQ_WINDOW_MS = 200     # milliseconds of audio window to analyze per update
VIS_UPDATE_MS = 60     # how often to update visual (ms)
ALBUM_SIZE = 180
# ----------------------------

class MusicPlayerV4:
    def __init__(self, root):
        self.root = root
        self.root.title("🎶 Music Player 4.0 - Deluxe")
        self.root.geometry("720x540")
        self.root.configure(bg="#101018")

        # Pygame audio init
        pygame.mixer.init()
        self.freq, self.size, self.channels = pygame.mixer.get_init() or (44100, -16, 2)

        # state
        self.playlist = []
        self.current_index = 0
        self.playing = False
        self.paused = False
        self.random_mode = False
        self.volume = tk.DoubleVar(value=0.6)
        self.album_art = None
        self.snd_array = None       # numpy array with audio samples (if available)
        self.snd_sample_rate = self.freq
        self.snd_channels = self.channels
        self.snd_loaded = False
        self.visual_mode = "analyze"  # "analyze" or "fallback"

        # load config
        self._load_config()

        # build UI
        self._create_widgets()

        # start visual updater
        self._visual_updater_running = True
        self.root.after(VIS_UPDATE_MS, self._update_visual)

    # ---------------- UI ----------------
    def _create_widgets(self):
        # top frame for album art + title
        top = tk.Frame(self.root, bg="#101018")
        top.pack(fill=tk.X, pady=6)

        self.album_label = tk.Label(top, bg="#101018")
        self.album_label.pack(side=tk.LEFT, padx=12)
        self._show_default_album()

        title_frame = tk.Frame(top, bg="#101018")
        title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.current_song_label = tk.Label(title_frame, text="Nenhuma música tocando", fg="white", bg="#101018", font=("Helvetica", 12))
        self.current_song_label.pack(anchor="w", pady=6)

        # Controls row
        controls = tk.Frame(self.root, bg="#101018")
        controls.pack(pady=6)

        style = {"bg":"#3a3af7", "fg":"white", "relief":"flat", "width":10, "height":1}
        tk.Button(controls, text="Abrir Arquivo", command=self.load_file, **style).grid(row=0, column=0, padx=4)
        tk.Button(controls, text="Abrir Pasta", command=self.load_folder, **style).grid(row=0, column=1, padx=4)
        tk.Button(controls, text="Anterior", command=self.prev_track, **style).grid(row=0, column=2, padx=4)
        self.play_button = tk.Button(controls, text="Play", command=self.toggle_play, **style)
        self.play_button.grid(row=0, column=3, padx=4)
        tk.Button(controls, text="Pause", command=self.pause_music, **style).grid(row=0, column=4, padx=4)
        tk.Button(controls, text="Próxima", command=self.next_track, **style).grid(row=0, column=5, padx=4)
        tk.Button(controls, text="Aleatória", command=self.toggle_random, **style).grid(row=0, column=6, padx=4)

        # listbox
        self.listbox = tk.Listbox(self.root, bg="#151525", fg="white", selectbackground="#5e5efc")
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        # volume + visual canvas
        bottom = tk.Frame(self.root, bg="#101018")
        bottom.pack(fill=tk.X, pady=6)

        vol_frame = tk.Frame(bottom, bg="#101018")
        vol_frame.pack(side=tk.LEFT, padx=12)
        tk.Label(vol_frame, text="🔊 Volume", fg="white", bg="#101018").pack()
        vol_scale = tk.Scale(vol_frame, variable=self.volume, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, command=self._set_volume, bg="#101018", fg="white", troughcolor="#5e5efc")
        vol_scale.pack()

        # equalizer canvas
        self.eq_canvas = tk.Canvas(bottom, width=480, height=120, bg="#0f0f16", highlightthickness=0)
        self.eq_canvas.pack(side=tk.LEFT, padx=12)
        self._init_eq_bars()

        # status bar
        self.status_label = tk.Label(self.root, text="", fg="white", bg="#101018", anchor="w")
        self.status_label.pack(fill=tk.X, padx=12, pady=(0,8))

        # set volume initially
        self._set_volume(self.volume.get())

        # On close -> save config
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---------------- Playlist & Loading ----------------
    def load_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".mp3")]
        files.sort()
        self.playlist = files
        self._refresh_listbox()
        if self.playlist:
            self.current_index = 0
            self._try_load_sound_array(self.playlist[self.current_index], folder)
            self._play_current()

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("MP3 files","*.mp3"),("All files","*.*")])
        if not path:
            return
        self.playlist = [path]
        self.current_index = 0
        self._refresh_listbox()
        self._try_load_sound_array(path, os.path.dirname(path))
        self._play_current()

    def _refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for p in self.playlist:
            self.listbox.insert(tk.END, os.path.basename(p))

    def _on_select(self, event):
        sel = self.listbox.curselection()
        if sel:
            self.current_index = sel[0]
            path = self.playlist[self.current_index]
            self._try_load_sound_array(path, os.path.dirname(path))
            self._play_current()

    # ---------------- Playback ----------------
    def _play_current(self):
        if not self.playlist:
            return
        path = self.playlist[self.current_index]
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            self._show_current_song(path)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível tocar:\n{e}")
            self.playing = False

    def toggle_play(self):
        if not self.playlist:
            return
        if self.playing and not self.paused:
            self.pause_music()
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self._play_current()

    def pause_music(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False

    def next_track(self):
        if not self.playlist:
            return
        if self.random_mode:
            self.current_index = random.randint(0, len(self.playlist)-1)
        else:
            self.current_index = (self.current_index + 1) % len(self.playlist)
        path = self.playlist[self.current_index]
        self._try_load_sound_array(path, os.path.dirname(path))
        self._play_current()

    def prev_track(self):
        if not self.playlist:
            return
        if self.random_mode:
            self.current_index = random.randint(0, len(self.playlist)-1)
        else:
            self.current_index = (self.current_index - 1) % len(self.playlist)
        path = self.playlist[self.current_index]
        self._try_load_sound_array(path, os.path.dirname(path))
        self._play_current()

    def toggle_random(self):
        self.random_mode = not self.random_mode
        state = "ativado" if self.random_mode else "desativado"
        messagebox.showinfo("Modo Aleatório", f"Modo aleatório {state}")

    # ---------------- Volume ----------------
    def _set_volume(self, val):
        try:
            v = float(val)
        except:
            v = self.volume.get()
        pygame.mixer.music.set_volume(v)
        self._save_config()

    # ---------------- Album art ----------------
    def _show_default_album(self):
        # placeholder
        self.album_label.config(text="🎵", image="", width=ALBUM_SIZE, height=ALBUM_SIZE, font=("Helvetica", 36), fg="white")

    def _load_album_art(self, folder):
        # find typical cover files
        candidates = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f.lower().startswith(('cover','folder','albumart','front'))]
        if not candidates:
            # try any image file
            any_img = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            candidates = any_img[:1] if any_img else []
        if candidates:
            path = os.path.join(folder, candidates[0])
            try:
                img = Image.open(path).resize((ALBUM_SIZE, ALBUM_SIZE))
                self.album_art = ImageTk.PhotoImage(img)
                self.album_label.config(image=self.album_art, text="")
            except Exception as e:
                print("Erro capa:", e)
                self._show_default_album()
        else:
            self._show_default_album()

    def _show_current_song(self, path):
        self.current_song_label.config(text=f"Tocando: {os.path.basename(path)}")
        folder = os.path.dirname(path)
        self._load_album_art(folder)

    # ---------------- Sound array analysis ----------------
    def _try_load_sound_array(self, filepath, folder):
        """
        Attempt to load the audio into a numpy array using pygame.sndarray.
        This allows sample-level analysis. Not all SDL_mixer builds support
        converting mp3 to array; fallback to reactive animation if it fails.
        """
        self.snd_array = None
        self.snd_loaded = False
        try:
            # Try to create a Sound object (loads audio into memory)
            s = pygame.mixer.Sound(filepath)
            arr = pygame.sndarray.array(s)  # shape (samples, channels)
            # convert to float32 normalized between -1 and 1
            if arr.dtype != np.int16 and arr.dtype != np.int32:
                arr = arr.astype(np.int16)
            # Normalize depending on dtype
            if arr.dtype == np.int16:
                arr = arr.astype(np.float32) / 32768.0
            elif arr.dtype == np.int32:
                arr = arr.astype(np.float32) / 2147483648.0
            # if stereo, average to mono
            if arr.ndim == 2:
                arr = arr.mean(axis=1)
            self.snd_array = arr
            self.snd_sample_rate = self.freq
            self.snd_loaded = True
            self.visual_mode = "analyze"
            self.status_label.config(text="Visualizador: análise de áudio ativada")
        except Exception as e:
            # fallback
            self.snd_array = None
            self.snd_loaded = False
            self.visual_mode = "fallback"
            self.status_label.config(text="Visualizador: modo reativo (fallback).")
            # print for debug
            print("Não foi possível carregar array de áudio:", e)

    # ---------------- Visual equalizer ----------------
    def _init_eq_bars(self):
        self.eq_bars = []
        width = 480
        h = 120
        bar_w = width / EQ_BARS
        pad = 4
        for i in range(EQ_BARS):
            x1 = i * bar_w + pad
            x2 = (i+1) * bar_w - pad
            rect = self.eq_canvas.create_rectangle(x1, h, x2, h, fill="#5e5efc")
            self.eq_bars.append(rect)

    def _update_visual(self):
        if not self._visual_updater_running:
            return
        # if analyzing available audio
        if self.visual_mode == "analyze" and self.snd_loaded and self.playing and not self.paused:
            # get current playback position (ms)
            pos_ms = pygame.mixer.music.get_pos()
            if pos_ms < 0:
                pos_ms = 0
            # compute sample index
            start_idx = int(max(0, (pos_ms - EQ_WINDOW_MS) * self.snd_sample_rate / 1000.0))
            end_idx = int(min(len(self.snd_array), (pos_ms) * self.snd_sample_rate / 1000.0))
            if end_idx <= start_idx:
                # small window: pick a small range around current pos
                center = int(pos_ms * self.snd_sample_rate / 1000.0)
                start_idx = max(0, center - int(0.05 * self.snd_sample_rate))
                end_idx = min(len(self.snd_array), center + int(0.05 * self.snd_sample_rate))
            window = self.snd_array[start_idx:end_idx]
            if window.size == 0:
                mags = np.zeros(EQ_BARS)
            else:
                # FFT and split into bands
                fft = np.abs(np.fft.rfft(window * np.hanning(len(window))))
                freqs = np.fft.rfftfreq(len(window), d=1.0/self.snd_sample_rate)
                # define logarithmic bands
                freqs_max = freqs[-1] if freqs.size>0 else 1.0
                band_edges = np.logspace(np.log10(20), np.log10(max(1000, freqs_max)), num=EQ_BARS+1)
                mags = np.zeros(EQ_BARS)
                for i in range(EQ_BARS):
                    # indices in fft corresponding to band edges
                    idx = np.where((freqs >= band_edges[i]) & (freqs < band_edges[i+1]))[0]
                    if idx.size:
                        mags[i] = fft[idx].mean()
                    else:
                        mags[i] = 0.0
                # normalize mags for display
                mags = mags / (np.max(mags) + 1e-9)
        else:
            # fallback reactive visual: use volume + random jitter
            base = pygame.mixer.music.get_volume() if pygame.mixer.music.get_busy() else 0.0
            mags = np.clip(np.array([base + random.random()*0.4 for _ in range(EQ_BARS)]), 0.0, 1.0)

        # draw bars
        h = 120
        for i, rect in enumerate(self.eq_bars):
            mag = float(mags[i]) if mags.size>0 else 0.0
            height = 6 + mag * (h - 12)
            coords = self.eq_canvas.coords(rect)
            x1, _, x2, _ = coords
            self.eq_canvas.coords(rect, x1, h - height, x2, h)
        # schedule next update
        self.root.after(VIS_UPDATE_MS, self._update_visual)

    # wrapper that supports thread call
    def _update_visual_once(self):
        self._update_visual()

    # ---------------- Helpers ----------------
    def _load_config(self):
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, "r") as f:
                    cfg = json.load(f)
                    vol = cfg.get("volume", 0.6)
                    self.volume.set(vol)
        except Exception:
            pass

    def _save_config(self):
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump({"volume": self.volume.get()}, f)
        except Exception:
            pass

    def _on_close(self):
        self._visual_updater_running = False
        try:
            self._save_config()
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        self.root.destroy()


# ----------------- Entrypoint -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerV4(root)
    root.mainloop()
