"""
Music Player 4.2 PRO (Português, comentado)
- Tema escuro moderno
- Shuffle (alternável)
- Próxima / Anterior
- Scrollbar na lista
- Barra de progresso interativa (tenta buscar posição)
- Equalizador visual leve
- Salva último diretório aberto em player_config_v42.json

Observações:
- A função de "seek" (pular para x segundos) usa pygame.mixer.music.set_pos ou play(start=seconds).
  Nem todas as builds do SDL_mixer/pygame suportam seek preciso em MP3. Se não funcionar, o app avisa.
- Para duração confiável das MP3, instalar mutagen (pip install mutagen).
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pygame
import os
import threading
import time
import json
import random
import numpy as np

# Nome do arquivo de configuração (salva último diretório e volume)
CONFIG_FILE = "player_config_v42.json"

# Constantes de UI
WINDOW_W, WINDOW_H = 820, 560
ALBUM_SIZE = 200
EQ_BARS = 12
EQ_HEIGHT = 120

# ------------------------------- UTILITÁRIOS -------------------------------

def carregar_duracao_mp3(path):
    """Tenta obter a duração (segundos) usando mutagen; retorna None se falhar."""
    try:
        from mutagen import File
        f = File(path)
        if f and hasattr(f.info, "length"):
            return float(f.info.length)
    except Exception:
        pass
    # Fallback: tentar carregar como Sound (consome memória)
    try:
        s = pygame.mixer.Sound(path)
        return s.get_length()
    except Exception:
        return None

# ------------------------------- CLASSE PRINCIPAL -------------------------------

class MusicPlayerPRO:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player 4.2 PRO")
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.configure(bg="#0f0f14")  # fundo escuro

        # Inicializa áudio
        pygame.mixer.init()

        # Estado do player
        self.playlist = []            # lista de caminhos completos
        self.current_index = 0
        self.playing = False
        self.paused = False
        self.shuffle = False
        self.volume = tk.DoubleVar(value=0.6)
        self.album_art = None
        self.audio_duration = None   # duração em segundos da faixa atual (float ou None)
        self._stop_updater = False

        # Tenta carregar config (último diretório e volume)
        self.config = {"last_dir": None, "volume": 0.6}
        self._load_config()
        self.volume.set(self.config.get("volume", 0.6))

        # Construir interface
        self._build_ui()

        # Lógica de atualização (progress + visual)
        self._updater_thread = threading.Thread(target=self._updater_loop, daemon=True)
        self._updater_thread.start()

    # ---------------- UI ----------------
    def _build_ui(self):
        # Top: capa + título
        top = tk.Frame(self.root, bg="#0f0f14")
        top.pack(fill=tk.X, pady=8, padx=10)

        # Frame da capa
        self.album_label = tk.Label(top, bg="#0f0f14")
        self.album_label.pack(side=tk.LEFT, padx=10)
        self._show_default_album()

        # Info e controles de arquivo
        info_frame = tk.Frame(top, bg="#0f0f14")
        info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.label_song = tk.Label(info_frame, text="Nenhuma música selecionada", fg="#e6eef8", bg="#0f0f14", font=("Segoe UI", 12, "bold"), anchor="w")
        self.label_song.pack(fill=tk.X, pady=(8,4))

        # Botões principais
        btn_frame = tk.Frame(info_frame, bg="#0f0f14")
        btn_frame.pack(anchor="w", pady=4)

        btn_style = {"bg":"#2f7df7", "fg":"white", "relief":"flat", "activebackground":"#2467d9"}

        tk.Button(btn_frame, text="Abrir Arquivo", command=self.abrir_arquivo, **btn_style).grid(row=0, column=0, padx=4)
        tk.Button(btn_frame, text="Abrir Pasta", command=self.abrir_pasta, **btn_style).grid(row=0, column=1, padx=4)
        tk.Button(btn_frame, text="Anterior", command=self.anterior, **btn_style).grid(row=0, column=2, padx=4)

        self.btn_play = tk.Button(btn_frame, text="Play", command=self.toggle_play, **btn_style, width=8)
        self.btn_play.grid(row=0, column=3, padx=6)

        tk.Button(btn_frame, text="Pause", command=self.pausar, **btn_style).grid(row=0, column=4, padx=4)
        tk.Button(btn_frame, text="Próxima", command=self.proxima, **btn_style).grid(row=0, column=5, padx=4)

        # Shuffle toggle
        self.btn_shuffle = tk.Button(btn_frame, text="Shuffle: OFF", command=self.toggle_shuffle, bg="#444", fg="white", relief="flat")
        self.btn_shuffle.grid(row=0, column=6, padx=8)

        # Volume
        vol_frame = tk.Frame(info_frame, bg="#0f0f14")
        vol_frame.pack(anchor="w", pady=(6,0))
        tk.Label(vol_frame, text="Volume", fg="#cfe8ff", bg="#0f0f14").pack(side=tk.LEFT, padx=(0,6))
        vol_scale = tk.Scale(vol_frame, variable=self.volume, from_=0.0, to=1.0, orient=tk.HORIZONTAL, resolution=0.01, command=self._set_volume, bg="#0f0f14", fg="white", troughcolor="#2f7df7", highlightthickness=0, length=250)
        vol_scale.pack(side=tk.LEFT)

        # Middle: Listbox com scrollbar
        mid = tk.Frame(self.root, bg="#0f0f14")
        mid.pack(fill=tk.BOTH, expand=True, padx=10, pady=6)

        list_frame = tk.Frame(mid, bg="#0f0f14")
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(list_frame, bg="#12121a", fg="white", selectbackground="#2f7df7", activestyle="none")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Right: equalizador visual
        eq_frame = tk.Frame(mid, bg="#0f0f14")
        eq_frame.pack(side=tk.RIGHT, padx=12)
        tk.Label(eq_frame, text="Equalizador", fg="#cfe8ff", bg="#0f0f14").pack()
        self.eq_canvas = tk.Canvas(eq_frame, width=300, height=EQ_HEIGHT, bg="#081018", highlightthickness=0)
        self.eq_canvas.pack(pady=6)
        self._init_eq()

        # Bottom: barra de progresso interativa + tempo
        bottom = tk.Frame(self.root, bg="#0f0f14")
        bottom.pack(fill=tk.X, padx=10, pady=(0,10))

        self.elapsed_label = tk.Label(bottom, text="00:00", fg="#cfe8ff", bg="#0f0f14")
        self.elapsed_label.pack(side=tk.LEFT)

        self.progress = tk.Scale(bottom, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, command=self._seek_ui, length=600, bg="#0f0f14", troughcolor="#2644a8", highlightthickness=0)
        self.progress.pack(side=tk.LEFT, padx=6)

        self.total_label = tk.Label(bottom, text="--:--", fg="#cfe8ff", bg="#0f0f14")
        self.total_label.pack(side=tk.LEFT)

    # ---------------- UI helpers ----------------
    def _show_default_album(self):
        """Mostra ícone padrão (nota musical) quando não há capa."""
        self.album_label.config(text="🎵", image="", width=ALBUM_SIZE, height=ALBUM_SIZE, font=("Segoe UI", 40), fg="#cfe8ff", bg="#0f0f14")

    def _load_album_art(self, folder):
        """Procura capa na pasta (cover*, folder*, albumart* ou qualquer imagem)."""
        try:
            candidates = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.jpeg','.png')) and f.lower().startswith(('cover','folder','albumart','front'))]
            if not candidates:
                # pega qualquer imagem como fallback
                any_img = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.jpeg','.png'))]
                candidates = any_img[:1] if any_img else []
            if candidates:
                path = os.path.join(folder, candidates[0])
                img = Image.open(path).resize((ALBUM_SIZE, ALBUM_SIZE))
                self.album_art = ImageTk.PhotoImage(img)
                self.album_label.config(image=self.album_art, text="")
            else:
                self._show_default_album()
        except Exception as e:
            print("Erro ao carregar capa:", e)
            self._show_default_album()

    def _init_eq(self):
        """Inicializa retângulos no canvas do equalizador."""
        self.eq_rects = []
        w = 300
        bar_w = w / EQ_BARS
        pad = 4
        for i in range(EQ_BARS):
            x1 = i * bar_w + pad
            x2 = (i+1) * bar_w - pad
            rect = self.eq_canvas.create_rectangle(x1, EQ_HEIGHT, x2, EQ_HEIGHT, fill="#2f7df7", outline="")
            self.eq_rects.append(rect)

    # ---------------- Gerenciamento de playlist ----------------
    def abrir_pasta(self):
        """Seleciona uma pasta com MP3s; salva último diretório."""
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
            self._prepare_and_play(self.current_index)

    def abrir_arquivo(self):
        """Abre arquivo único (MP3) e toca."""
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
        """Atualiza o Listbox com os nomes das faixas."""
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
        """Carrega dados da faixa (capa, duração) e inicia reprodução em thread."""
        path = self.playlist[idx]
        # carregar capa
        self._load_album_art(os.path.dirname(path))
        # tentar obter duração (mutagen fallback)
        self.audio_duration = carregar_duracao_mp3(path)
        if self.audio_duration:
            self.progress.config(to=int(self.audio_duration))
            self.total_label.config(text=self._fmt_time(self.audio_duration))
        else:
            self.progress.config(to=100)
            self.total_label.config(text="--:--")
        # tocar em thread para não travar UI
        threading.Thread(target=self._play_thread, args=(path,), daemon=True).start()

    def _play_thread(self, path):
        """Thread que carrega e toca a faixa (usa pygame)."""
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            self._update_labels(path)
        except Exception as e:
            messagebox.showerror("Erro ao reproduzir", str(e))
            self.playing = False

    def _update_labels(self, path):
        """Atualiza o label da música atual e seleção na lista."""
        self.label_song.config(text=os.path.basename(path))
        # marca no listbox
        self.listbox.selection_clear(0, tk.END)
        if self.playlist:
            self.listbox.selection_set(self.current_index)

    # ---------------- Controles de reprodução ----------------
    def toggle_play(self):
        """Play / unpause / se nada tocar, inicia a atual."""
        if not self.playlist:
            return
        if self.playing and not self.paused:
            # está tocando -> pausar
            self.pausar()
        elif self.paused:
            # está pausado -> retomar
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            # não está tocando -> tocar atual
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
        self.btn_shuffle.config(text=f"Shuffle: {'ON' if self.shuffle else 'OFF'}", bg=("#2f7df7" if self.shuffle else "#444"))
        # feedback pequeno
        msg = "Modo aleatório ativado" if self.shuffle else "Modo aleatório desativado"
        self._flash_status(msg)

    # ---------------- Volume ----------------
    def _set_volume(self, val):
        try:
            v = float(val)
        except:
            v = self.volume.get()
        pygame.mixer.music.set_volume(v)
        self.config["volume"] = v
        self._save_config()

    # ---------------- Seek / Barra de progresso ----------------
    def _seek_ui(self, val):
        """Chamado quando o usuário interage com a barra. Tenta buscar na música."""
        # val é string; convert
        try:
            sec = float(val)
        except:
            return
        # Tenta usar set_pos ou play(start=)
        try:
            # preferir set_pos (mais intuitivo)
            pygame.mixer.music.set_pos(sec)
        except Exception:
            try:
                # play a partir do segundo (algumas builds aceitam)
                pygame.mixer.music.play(start=sec)
            except Exception:
                # não suportado - avisar e retornar
                self._flash_status("Seek não suportado pela sua versão do pygame/codec")
        # se pausado, manter pausa após seek
        if self.paused:
            pygame.mixer.music.pause()

    # ---------------- Updater (progress + monitor fim de faixa + visual) ----------------
    def _updater_loop(self):
        """Loop que atualiza a UI: tempo decorrido, progress, visualizer e detecta fim da faixa."""
        while not self._stop_updater:
            try:
                if self.playing and not self.paused:
                    pos_ms = pygame.mixer.music.get_pos()
                    if pos_ms < 0:
                        # às vezes get_pos retorna -1 quando não sabe
                        pos = None
                    else:
                        pos = pos_ms / 1000.0
                    # atualizar progress e label de tempo
                    if pos is not None:
                        # atualiza escala (se usuário nao estiver arrastando)
                        try:
                            self.progress.set(int(pos))
                        except Exception:
                            pass
                        self.elapsed_label.config(text=self._fmt_time(pos))
                    # detectar fim (se duração conhecida)
                    if self.audio_duration:
                        # se passou do fim (por segurança) -> próxima
                        if pos is not None and pos >= (self.audio_duration - 0.5):
                            self.proxima()
                    else:
                        # se mixer diz que não está tocando -> avançar
                        if not pygame.mixer.music.get_busy() and self.playing and not self.paused:
                            self.proxima()
                # atualizar equalizador (reactive)
                self._update_eq()
            except Exception as e:
                # não travar o loop por causa de erro
                # print("Updater:", e)
                pass
            time.sleep(0.4)

    # ---------------- Equalizador (visual simples) ----------------
    def _update_eq(self):
        """Desenha barras reativas; se análise de áudio não disponível, usa volume + ruído."""
        base = pygame.mixer.music.get_volume() if pygame.mixer.music.get_busy() else 0.0
        # gera valores entre 0 e 1 para cada barra
        vals = np.clip(np.array([base + random.random()*0.6 for _ in range(EQ_BARS)]), 0.0, 1.0)
        h = EQ_HEIGHT
        for i, rect in enumerate(self.eq_rects):
            mag = float(vals[i])
            height = 6 + mag * (h - 12)
            coords = self.eq_canvas.coords(rect)
            x1, _, x2, _ = coords
            self.eq_canvas.coords(rect, x1, h - height, x2, h)

    # ---------------- Helpers ----------------
    def _fmt_time(self, sec):
        """Formata segundos em MM:SS."""
        try:
            sec = int(sec)
            m = sec // 60
            s = sec % 60
            return f"{m:02d}:{s:02d}"
        except:
            return "--:--"

    def _flash_status(self, txt, timeout=1.2):
        """Mostra uma mensagem curta na status_label (temporária)."""
        old = getattr(self, "_last_status", "")
        self._last_status = txt
        # criar/mostrar widget temporário
        if not hasattr(self, "status_label"):
            self.status_label = tk.Label(self.root, text=txt, fg="#cfe8ff", bg="#0f0f14")
            self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            self.status_label.config(text=txt)
        # agendar limpeza
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
        """Chamada ao fechar: salva config e finaliza pygame."""
        self._stop_updater = True
        self.config["volume"] = self.volume.get()
        self._save_config()
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        self.root.destroy()

# ----------------- EXECUÇÃO -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerPRO(root)
    root.protocol("WM_DELETE_WINDOW", app._on_close)
    root.mainloop()
