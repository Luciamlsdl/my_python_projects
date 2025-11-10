"""
Music Player 4.3 PRO (Português) - Tema escuro
- Shuffle ON/OFF
- Próxima / Anterior
- Scrollbar na lista de músicas
- Barra de progresso interativa (seek quando suportado)
- Equalizador visual leve (reactivo)
- Mostra capa do álbum (cover*, folder*, albumart*, any image fallback)
- Salva último diretório e volume em player_config_v43.json
- Comentado para estudo
"""

import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import pygame
import threading
import time
import os
import json
import random
import numpy as np

# ---------- CONFIGURAÇÃO ----------
CONFIG_FILE = "player_config_v43.json"
WINDOW_W, WINDOW_H = 880, 600
ALBUM_SIZE = 220
EQ_BARS = 14
EQ_HEIGHT = 140
UPDATER_INTERVAL = 0.35  # segundos
# -----------------------------------

# utilitário para formatar tempo mm:ss
def fmt_time(seconds):
    try:
        s = int(seconds)
        m = s // 60
        sec = s % 60
        return f"{m:02d}:{sec:02d}"
    except:
        return "--:--"


# tenta obter duração usando mutagen; retorna None se não disponível
def obter_duracao_mp3(path):
    try:
        from mutagen import File
        f = File(path)
        if f and hasattr(f.info, "length"):
            return float(f.info.length)
    except Exception:
        pass
    # fallback: tentar carregar como Sound (pode ser pesado)
    try:
        s = pygame.mixer.Sound(path)
        return s.get_length()
    except Exception:
        return None


class MusicPlayerPRO:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player 4.3 PRO")
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.configure(bg="#0d0f15")

        # inicializa pygame mixer
        pygame.mixer.init()

        # estado
        self.playlist = []          # lista de caminhos
        self.current_index = 0
        self.playing = False
        self.paused = False
        self.shuffle = False
        self.volume = tk.DoubleVar(value=0.6)
        self.audio_duration = None  # em segundos (float) se conhecido
        self.album_art = None
        self.eq_rects = []

        # carregar configuração (último diretório + volume)
        self.config = {"last_dir": None, "volume": 0.6}
        self._load_config()
        self.volume.set(self.config.get("volume", 0.6))

        # construir interface
        self._build_ui()

        # iniciar thread de atualização (progress + visual)
        self._stop_flag = False
        self._updater = threading.Thread(target=self._updater_loop, daemon=True)
        self._updater.start()

        # garantir fechamento limpo
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---------------- UI ----------------
    def _build_ui(self):
        # top: capa e informações
        top = tk.Frame(self.root, bg="#0d0f15")
        top.pack(fill=tk.X, pady=8, padx=10)

        # label da capa
        self.album_label = tk.Label(top, bg="#0d0f15")
        self.album_label.pack(side=tk.LEFT, padx=12)
        self._show_default_album()

        info = tk.Frame(top, bg="#0d0f15")
        info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.label_song = tk.Label(info, text="Nenhuma música selecionada", fg="#e8f0ff",
                                   bg="#0d0f15", font=("Segoe UI", 13, "bold"), anchor="w")
        self.label_song.pack(fill=tk.X, pady=(6,4))

        # botões
        btn_frame = tk.Frame(info, bg="#0d0f15")
        btn_frame.pack(anchor="w", pady=4)

        btn_style = {"bg":"#2070ff", "fg":"white", "relief":"flat", "activebackground":"#1a5fd6"}

        tk.Button(btn_frame, text="Abrir Arquivo", command=self.abrir_arquivo, **btn_style).grid(row=0, column=0, padx=4)
        tk.Button(btn_frame, text="Abrir Pasta", command=self.abrir_pasta, **btn_style).grid(row=0, column=1, padx=4)
        tk.Button(btn_frame, text="Anterior", command=self.anterior, **btn_style).grid(row=0, column=2, padx=4)

        self.btn_play = tk.Button(btn_frame, text="Play", command=self.toggle_play, **btn_style, width=8)
        self.btn_play.grid(row=0, column=3, padx=6)

        tk.Button(btn_frame, text="Pause", command=self.pausar, **btn_style).grid(row=0, column=4, padx=4)
        tk.Button(btn_frame, text="Próxima", command=self.proxima, **btn_style).grid(row=0, column=5, padx=4)

        self.btn_shuffle = tk.Button(btn_frame, text="Shuffle: OFF", command=self.toggle_shuffle, bg="#444", fg="white", relief="flat")
        self.btn_shuffle.grid(row=0, column=6, padx=8)

        # volume
        vol_frame = tk.Frame(info, bg="#0d0f15")
        vol_frame.pack(anchor="w", pady=(6,0))
        tk.Label(vol_frame, text="Volume", fg="#cfe8ff", bg="#0d0f15").pack(side=tk.LEFT, padx=(0,6))
        vol_scale = tk.Scale(vol_frame, variable=self.volume, from_=0.0, to=1.0, orient=tk.HORIZONTAL,
                             resolution=0.01, command=self._set_volume, bg="#0d0f15", fg="white", troughcolor="#2070ff", length=300)
        vol_scale.pack(side=tk.LEFT)

        # middle: listbox com scrollbar + equalizador
        mid = tk.Frame(self.root, bg="#0d0f15")
        mid.pack(fill=tk.BOTH, expand=True, padx=10, pady=6)

        # listbox e scrollbar
        list_frame = tk.Frame(mid, bg="#0d0f15")
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(list_frame, bg="#0a0c12", fg="white", selectbackground="#2070ff", activestyle="none")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # equalizador (à direita)
        eq_frame = tk.Frame(mid, bg="#0d0f15")
        eq_frame.pack(side=tk.RIGHT, padx=12)
        tk.Label(eq_frame, text="Equalizador", fg="#cfe8ff", bg="#0d0f15").pack()
        self.eq_canvas = tk.Canvas(eq_frame, width=260, height=EQ_HEIGHT, bg="#05060a", highlightthickness=0)
        self.eq_canvas.pack(pady=6)
        self._init_eq()

        # bottom: barra de progresso interativa + tempo
        bottom = tk.Frame(self.root, bg="#0d0f15")
        bottom.pack(fill=tk.X, padx=10, pady=(0,10))

        self.elapsed_label = tk.Label(bottom, text="00:00", fg="#cfe8ff", bg="#0d0f15")
        self.elapsed_label.pack(side=tk.LEFT)

        # progress scale interativo
        self.progress = tk.Scale(bottom, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0,
                                 bg="#0d0f15", troughcolor="#2644a8", highlightthickness=0, command=self._seek_ui, length=620)
        self.progress.pack(side=tk.LEFT, padx=8)

        self.total_label = tk.Label(bottom, text="--:--", fg="#cfe8ff", bg="#0d0f15")
        self.total_label.pack(side=tk.LEFT)

    # ---------------- UI helpers ----------------
    def _show_default_album(self):
        self.album_label.config(text="🎵", image="", width=ALBUM_SIZE, height=ALBUM_SIZE, font=("Segoe UI", 40), fg="#cfe8ff", bg="#0d0f15")

    def _load_album_art(self, folder):
        try:
            # procura por nomes comuns
            candidates = [f for f in os.listdir(folder)
                          if f.lower().endswith(('.jpg', '.jpeg', '.png')) and f.lower().startswith(('cover','folder','albumart','front'))]
            if not candidates:
                any_img = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                candidates = any_img[:1] if any_img else []
            if candidates:
                path = os.path.join(folder, candidates[0])
                img = Image.open(path).resize((ALBUM_SIZE, ALBUM_SIZE))
                self.album_art = ImageTk.PhotoImage(img)
                self.album_label.config(image=self.album_art, text="")
            else:
                self._show_default_album()
        except Exception as e:
            print("Erro carregar capa:", e)
            self._show_default_album()

    def _init_eq(self):
        self.eq_rects = []
        w = 260
        bar_w = w / EQ_BARS
        pad = 3
        for i in range(EQ_BARS):
            x1 = i * bar_w + pad
            x2 = (i+1) * bar_w - pad
            rect = self.eq_canvas.create_rectangle(x1, EQ_HEIGHT, x2, EQ_HEIGHT, fill="#2070ff", outline="")
            self.eq_rects.append(rect)

    # ---------------- Playlist e carregamento ----------------
    def abrir_pasta(self):
        initial = self.config.get("last_dir") or os.path.expanduser("~")
        folder = filedialog.askdirectory(initialdir=initial)
        if not folder:
            return
        self.config["last_dir"] = folder
        self._save_config()
        files = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".mp3")])
        self.playlist = files
        self._refresh_list()
        if self.playlist:
            self.current_index = 0
            self._prepare_and_play(0)

    def abrir_arquivo(self):
        initial = self.config.get("last_dir") or os.path.expanduser("~")
        path = filedialog.askopenfilename(initialdir=initial, filetypes=[("MP3 files","*.mp3"),("All files","*.*")])
        if not path:
            return
        folder = os.path.dirname(path)
        self.config["last_dir"] = folder
        self._save_config()
        self.playlist = [path]
        self._refresh_list()
        self.current_index = 0
        self._prepare_and_play(0)

    def _refresh_list(self):
        self.listbox.delete(0, tk.END)
        for p in self.playlist:
            self.listbox.insert(tk.END, os.path.basename(p))

    def _on_select(self, event):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            self.current_index = idx
            self._prepare_and_play(idx)

    # ---------------- Preparar e tocar ----------------
    def _prepare_and_play(self, idx):
        path = self.playlist[idx]
        # carrega capa
        self._load_album_art(os.path.dirname(path))
        # tenta obter duração
        self.audio_duration = obter_duracao_mp3(path)
        if self.audio_duration:
            self.progress.config(to=int(self.audio_duration))
            self.total_label.config(text=fmt_time(self.audio_duration))
        else:
            self.progress.config(to=100)
            self.total_label.config(text="--:--")
        # tocar em thread
        threading.Thread(target=self._play_thread, args=(path,), daemon=True).start()

    def _play_thread(self, path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            self._update_labels(path)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível reproduzir:\n{e}")
            self.playing = False

    def _update_labels(self, path):
        self.label_song.config(text=os.path.basename(path))
        self.listbox.selection_clear(0, tk.END)
        if self.playlist:
            self.listbox.selection_set(self.current_index)

    # ---------------- Controles ----------------
    def toggle_play(self):
        if not self.playlist:
            return
        if self.playing and not self.paused:
            self.pausar()
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self._prepare_and_play(self.current_index)

    def pausar(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def parar(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False

    def proxima(self):
        if not self.playlist:
            return
        if self.shuffle:
            self.current_index = random.randint(0, len(self.playlist)-1)
        else:
            self.current_index = (self.current_index + 1) % len(self.playlist)
        self._prepare_and_play(self.current_index)

    def anterior(self):
        if not self.playlist:
            return
        if self.shuffle:
            self.current_index = random.randint(0, len(self.playlist)-1)
        else:
            self.current_index = (self.current_index - 1) % len(self.playlist)
        self._prepare_and_play(self.current_index)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        self.btn_shuffle.config(text=f"Shuffle: {'ON' if self.shuffle else 'OFF'}",
                                bg=("#2f7df7" if self.shuffle else "#444"))
        self._flash_status("Shuffle ativado" if self.shuffle else "Shuffle desativado")

    # ---------------- Volume ----------------
    def _set_volume(self, val):
        try:
            v = float(val)
        except:
            v = self.volume.get()
        pygame.mixer.music.set_volume(v)
        self.config["volume"] = v
        self._save_config()

    # ---------------- Seek (barra de progresso interativa) ----------------
    def _seek_ui(self, val):
        try:
            sec = float(val)
        except:
            return
        try:
            # tentar usar set_pos (nem sempre suportado)
            pygame.mixer.music.set_pos(sec)
        except Exception:
            try:
                pygame.mixer.music.play(start=sec)
            except Exception:
                self._flash_status("Seek não suportado nesta instalação/codec")

        if self.paused:
            pygame.mixer.music.pause()

    # ---------------- Loop de atualização ----------------
    def _updater_loop(self):
        while not self._stop_flag:
            try:
                if self.playing and not self.paused:
                    pos_ms = pygame.mixer.music.get_pos()
                    pos = None
                    if pos_ms >= 0:
                        pos = pos_ms / 1000.0
                    # atualizar UI
                    if pos is not None:
                        # proteger contra exceções se usuário estiver arrastando
                        try:
                            self.progress.set(int(pos))
                        except:
                            pass
                        self.elapsed_label.config(text=fmt_time(pos))
                    # detectar fim pela duração conhecida
                    if self.audio_duration:
                        if pos is not None and pos >= (self.audio_duration - 0.4):
                            self.proxima()
                    else:
                        # fallback: se mixer não está busy, tocar próxima
                        if not pygame.mixer.music.get_busy() and self.playing and not self.paused:
                            self.proxima()
                # atualizar equalizador (reactivo)
                self._update_eq()
            except Exception:
                pass
            time.sleep(UPDATER_INTERVAL)

    # ---------------- Equalizador reactivo ----------------
    def _update_eq(self):
        base = pygame.mixer.music.get_volume() if pygame.mixer.music.get_busy() else 0.0
        vals = np.clip(np.array([base + random.random()*0.6 for _ in range(EQ_BARS)]), 0.0, 1.0)
        h = EQ_HEIGHT
        for i, rect in enumerate(self.eq_rects):
            mag = float(vals[i])
            height = 6 + mag * (h - 12)
            coords = self.eq_canvas.coords(rect)
            x1, _, x2, _ = coords
            self.eq_canvas.coords(rect, x1, h - height, x2, h)

    # ---------------- Status e config ----------------
    def _flash_status(self, txt, timeout=1.2):
        if not hasattr(self, "status_label"):
            self.status_label = tk.Label(self.root, text=txt, fg="#cfe8ff", bg="#0d0f15")
            self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            self.status_label.config(text=txt)
        self.root.after(int(timeout*1000), lambda: self.status_label.config(text=""))

    def _load_config(self):
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, "r") as f:
                    self.config = json.load(f)
        except Exception:
            self.config = {"last_dir": None, "volume": 0.6}

    def _save_config(self):
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump(self.config, f)
        except Exception:
            pass

    def _on_close(self):
        self._stop_flag = True
        self.config["volume"] = self.volume.get()
        self._save_config()
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        self.root.destroy()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerPRO(root)
    root.mainloop()
