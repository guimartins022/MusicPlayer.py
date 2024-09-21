import pygame
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Inicializando o Pygame
pygame.mixer.init()

# Caminho absoluto do diretório onde o script está localizado
base_dir = os.path.dirname(os.path.abspath(__file__))

# Funções de controle
def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def load_music():
    music_path = os.path.join(base_dir, "Hurt.mp3")
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
    else:
        print(f"Arquivo de música não encontrado: {music_path}")

def stop_music():
    pygame.mixer.music.stop()

# Configuração da janela principal
root = tk.Tk()
root.title("Player de Música")
root.geometry("400x400")  # Tamanho compacto da janela
root.configure(bg='#B0B0B0')  # Cor de fundo cinza suave
root.resizable(False, False)  # Impede a maximização da janela

# Configuração do estilo dos widgets
style = ttk.Style()

# Estilo para botões com cores e bordas personalizadas
style.configure("TButton",
                font=("Roboto", 12, "bold"),  # Fonte do texto dos botões
                padding=8,  # Ajuste do espaçamento interno dos botões
                background="#444444",  # Cor de fundo dos botões
                foreground="#000000",  # Cor do texto dos botões
                borderwidth=2,
                relief="flat")

# Mapear estados de interação dos botões (hover, pressionado)
style.map("TButton",
          background=[('active', '#555555')],
          foreground=[('pressed', '#000000'), ('active', '#000000')],
          bordercolor=[('hover', '#FF4500')])  # Cor da borda ao passar o mouse

# Carregar a imagem do álbum usando o caminho absoluto
image_path = os.path.join(base_dir, "AmericanIV.jpg")
album_photo = None

if os.path.exists(image_path):
    album_image = Image.open(image_path)
    album_image = album_image.resize((200, 200), Image.LANCZOS)
    album_photo = ImageTk.PhotoImage(album_image)
else:
    print(f"Imagem não encontrada: {image_path}")

# Frame principal para a imagem e os botões
main_frame = tk.Frame(root, bg="#B0B0B0")
main_frame.pack(expand=True, fill=tk.BOTH)

# Exibir a imagem na interface, se ela foi carregada
if album_photo:
    img_label = tk.Label(main_frame, image=album_photo, bg="#B0B0B0")
    img_label.pack(pady=10)
else:
    img_label = tk.Label(main_frame, text="Imagem não disponível", bg="#B0B0B0", fg="#FF0000")
    img_label.pack(pady=10)

# Exibir o nome da música abaixo da imagem
music_label = tk.Label(main_frame, text="Johnny Cash - Hurt", font=("Roboto", 14, "bold"), bg="#B0B0B0", fg="#000000")
music_label.pack()

# Frame para os botões de controle
button_frame = tk.Frame(main_frame, bg="#B0B0B0")
button_frame.pack(pady=10)

# Botões de controle com texto e emojis
play_button = ttk.Button(button_frame, text="▶ Play", command=play_music, style="TButton")
pause_button = ttk.Button(button_frame, text="⏸ Pause", command=pause_music, style="TButton")
stop_button = ttk.Button(button_frame, text="⏹ Stop", command=stop_music, style="TButton")
load_button = ttk.Button(button_frame, text="🔄 Carregar Música", command=load_music, style="TButton")

# Organização dos botões na janela
play_button.grid(row=0, column=0, padx=5, pady=5)
pause_button.grid(row=0, column=1, padx=5, pady=5)
stop_button.grid(row=0, column=2, padx=5, pady=5)
load_button.grid(row=1, column=0, columnspan=3, pady=5, ipadx=20)  # Ajuste para evitar que o botão seja cortado

# Iniciar a interface gráfica
root.mainloop()
