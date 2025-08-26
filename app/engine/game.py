from engine.audio import play_music
from engine.scenes import cena_escritorio
import os


def iniciar_jogo():
    os.system("cls" if os.name == "nt" else "clear")
    print("🎮 SIMULAÇÃO DE VISTORIAS EM IMÓVEIS\n")
    play_music("assets/music/ambiente.mp3")
    cena_escritorio()
