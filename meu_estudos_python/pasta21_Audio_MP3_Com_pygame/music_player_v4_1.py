"""
🎵 Music Player 4.1 (Versão em Português)
----------------------------------------
Reproduz músicas MP3 com interface Tkinter e Pygame.
Mostra a capa do álbum automaticamente (se existir na pasta),
permite escolher músicas de qualquer diretório e ajustar o volume.

Desenvolvido para fins de estudo e aprimoramento.
"""

# ========== IMPORTAÇÕES ==========
import tkinter as tk
from tkinter import filedialog, Listbox, Button, Label, Scale, DoubleVar, Canvas
from PIL import Image, ImageTk
import pygame
import os
import warnings

# Ignorar avisos do pygame sobre pkg_resources
warnings.filterwarnings("ignore", category=UserWarning)


# ========== CLASSE PRINCIPAL ==========
class MusicPlayer:
    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("🎶 Tocador de Músicas 4.1")
        self.root.geometry("420x340")
        self.root.config(bg="#f4f4f4")  # Tema claro

        # Inicializa o mixer do pygame (módulo de som)
        pygame.mixer.init()

        # Variáveis de controle
        self.playlist = []           # Lista de músicas
        self.current_index = 0       # Índice da música atual
        self.paused = False          # Controle de pausa
        self.volume = DoubleVar(value=0.5)  # Volume inicial
        self.background_image = None # Capa do álbum
        self.bg_label = None         # Label que exibe a capa

        # Cria os elementos gráficos
        self.create_background()
        self.create_widgets()

    # ========== FUNÇÃO PARA CRIAR FUNDO ==========
    def create_background(self):
        """Cria o canvas onde será exibida a capa do álbum."""
        self.canvas = Canvas(self.root, width=420, height=340)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.config(bg="#e8e8e8")  # cor padrão se não houver capa

    # ========== FUNÇÃO PARA CARREGAR CAPA DO ÁLBUM ==========
    def load_album_art(self, folder_path):
        """Procura e exibe uma imagem de capa na pasta da música."""
        cover_files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            and f.lower().startswith(('cover', 'folder', 'albumart'))
        ]

        if cover_files:
            try:
                image_path = os.path.join(folder_path, cover_files[0])
                image = Image.open(image_path)
                image = image.resize((420, 340))
                self.background_image = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
            except Exception as e:
                print(f"⚠️ Erro ao carregar capa: {e}")
                self.canvas.config(bg="#e8e8e8")
        else:
            self.canvas.config(bg="#e8e8e8")

    # ========== FUNÇÃO PARA CRIAR OS WIDGETS ==========
    def create_widgets(self):
        """Cria os botões, lista e controles de volume."""

        # Lista de músicas
        self.listbox = Listbox(
            self.canvas, selectmode=tk.SINGLE, bg="#ffffff", fg="#333", relief="flat"
        )
        self.listbox.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)
        self.listbox.bind('<<ListboxSelect>>', self.load_and_play_selected)

        # Nome da música atual
        self.current_song_label = Label(
            self.canvas, text="Nenhuma música selecionada",
            bg="#f4f4f4", fg="#222", font=("Arial", 10, "bold")
        )
        self.current_song_label.place(relx=0.05, rely=0.52)

        # Botões principais
        self.btn_open = Button(
            self.canvas, text="📂 Abrir Pasta", bg="#4CAF50", fg="white",
            relief="flat", command=self.load_folder
        )
        self.btn_open.place(relx=0.05, rely=0.65, relwidth=0.25)

        self.btn_play = Button(
            self.canvas, text="▶️ Play", bg="#2196F3", fg="white",
            relief="flat", command=self.play_music, state=tk.DISABLED
        )
        self.btn_play.place(relx=0.35, rely=0.65, relwidth=0.15)

        self.btn_pause = Button(
            self.canvas, text="⏸️ Pause", bg="#FF9800", fg="white",
            relief="flat", command=self.pause_music, state=tk.DISABLED
        )
        self.btn_pause.place(relx=0.52, rely=0.65, relwidth=0.18)

        self.btn_stop = Button(
            self.canvas, text="⏹️ Stop", bg="#F44336", fg="white",
            relief="flat", command=self.stop_music, state=tk.DISABLED
        )
        self.btn_stop.place(relx=0.73, rely=0.65, relwidth=0.18)

        # Controle de volume
        Label(self.canvas, text="🔊 Volume", bg="#f4f4f4", fg="#333").place(relx=0.05, rely=0.80)
        volume_scale = Scale(
            self.canvas, variable=self.volume, from_=0.0, to=1.0, resolution=0.01,
            orient=tk.HORIZONTAL, bg="#f4f4f4", command=self.set_volume
        )
        volume_scale.place(relx=0.25, rely=0.78, relwidth=0.65)

    # ========== FUNÇÃO PARA CARREGAR PASTA ==========
    def load_folder(self):
        """Abre um diálogo para escolher uma pasta com músicas MP3."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Cria uma lista com os arquivos MP3 da pasta
            self.playlist = sorted([
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith(".mp3")
            ])

            # Atualiza a lista visual
            self.listbox.delete(0, tk.END)
            for song in self.playlist:
                self.listbox.insert(tk.END, os.path.basename(song))

            # Se houver músicas, ativa os botões e carrega capa
            if self.playlist:
                self.load_album_art(folder_path)
                self.btn_play.config(state=tk.NORMAL)

    # ========== FUNÇÃO PARA TOCAR A MÚSICA SELECIONADA ==========
    def load_and_play_selected(self, event):
        """Carrega e toca a música selecionada na lista."""
        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_index = selected_index[0]
            song_path = self.playlist[self.current_index]
            self.load_music(song_path)
            self.play_music()
            self.load_album_art(os.path.dirname(song_path))

    # ========== FUNÇÃO PARA CARREGAR MÚSICA ==========
    def load_music(self, file_path):
        """Carrega uma música específica."""
        try:
            pygame.mixer.music.load(file_path)
            self.current_song_label.config(text=os.path.basename(file_path))
            self.btn_play.config(state=tk.NORMAL)
            self.btn_pause.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.NORMAL)
        except pygame.error as e:
            tk.messagebox.showerror("Erro", f"Não foi possível carregar o arquivo: {e}")

    # ========== CONTROLES DE REPRODUÇÃO ==========
    def play_music(self):
        """Inicia ou retoma a reprodução da música."""
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.paused = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_music(self):
        """Pausa a música em reprodução."""
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        """Interrompe completamente a música."""
        pygame.mixer.music.stop()
        self.paused = False

    def set_volume(self, val):
        """Ajusta o volume."""
        volume = float(val)
        pygame.mixer.music.set_volume(volume)


# ========== EXECUÇÃO ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
