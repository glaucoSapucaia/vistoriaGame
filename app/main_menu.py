import pygame
import sys
import os

# Garante que o Python ache a pasta raiz (onde estão 'app' e 'engine')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as configurações de níveiis
try:
    from app.niveis import FASE_CASA_CONFIG, FASE_COMERCIAL_CONFIG # <-- Adicionado aqui
except ImportError:
    from niveis import FASE_CASA_CONFIG, FASE_COMERCIAL_CONFIG

from engine.scene_manager import executar_fase

# Inicialização
pygame.init()
pygame.mixer.init()

# Tela
info = pygame.display.Info()
LARGURA, ALTURA = info.current_w, info.current_h
tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.RESIZABLE)
pygame.display.set_caption("Simulação de Vistorias em Imóveis")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
MARROM_ESCURO = (60, 40, 30)
CINZA = (30, 30, 30)

tamanho_fonte = int(ALTURA * 0.025)
fonte = pygame.font.SysFont("arial", tamanho_fonte)

# Música
pygame.mixer.music.load("assets/music/ambiente.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Fundo
try:
    fundo = pygame.image.load("assets/images/menu/Código de Vistoria.png").convert()
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
except:
    fundo = None

# Botão iniciar
botao_largura = int(LARGURA * 0.15)
botao_altura = int(ALTURA * 0.05)
botao_x = (LARGURA - botao_largura) // 2
botao_y = int(ALTURA * 0.75)
botao_iniciar = pygame.Rect(botao_x, botao_y, botao_largura, botao_altura)

# Botão sair
espaco_entre_botoes = int(ALTURA * 0.02)
botao_sair = pygame.Rect(
    botao_x, botao_y + botao_altura + espaco_entre_botoes, botao_largura, botao_altura
)

volume = 0.3


def desenhar():
    if fundo:
        tela.blit(fundo, (0, 0))
    else:
        tela.fill(CINZA)

    # Botão Iniciar
    pygame.draw.rect(tela, MARROM_ESCURO, botao_iniciar, border_radius=10)
    texto_iniciar = fonte.render("Iniciar", True, BRANCO)
    texto_iniciar_rect = texto_iniciar.get_rect(center=botao_iniciar.center)
    tela.blit(texto_iniciar, texto_iniciar_rect)

    # Botão Sair
    pygame.draw.rect(tela, MARROM_ESCURO, botao_sair, border_radius=10)
    texto_sair = fonte.render("Sair", True, BRANCO)
    texto_sair_rect = texto_sair.get_rect(center=botao_sair.center)
    tela.blit(texto_sair, texto_sair_rect)

    texto_volume = fonte.render(f"Volume: {int(volume * 100)}%", True, BRANCO)
    tela.blit(texto_volume, (int(LARGURA * 0.02), int(ALTURA * 0.02)))
    instrucoes = fonte.render("Use ↑ ↓ para ajustar", True, BRANCO)
    tela.blit(instrucoes, (int(LARGURA * 0.02), int(ALTURA * 0.06)))

    pygame.display.flip()


def menu():
    global volume
    while True:
        desenhar()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_iniciar.collidepoint(evento.pos):
                    selecao_fases()
                elif botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_UP:
                    volume = min(1.0, volume + 0.1)
                    pygame.mixer.music.set_volume(volume)
                elif evento.key == pygame.K_DOWN:
                    volume = max(0.0, volume - 0.1)
                    pygame.mixer.music.set_volume(volume)


def selecao_fases():
    fases = [
        {"nome": "Casa", "imagem": "assets/images/menu/casa.png"},
        {
            "nome": "Apartamento - em construção",
            "imagem": "assets/images/menu/casa2pav.jpg",
        },
        {
            "nome": "Prédio Antigo - em construção",
            "imagem": "assets/images/menu/casa2pav.jpg",
        },
        {
            "nome": "Condomínio - em construção",
            "imagem": "assets/images/menu/casa2pav.jpg",
        },
        {
            
            "nome": "Galpão Comercial", 
            "imagem": "assets/images/fases/galpao/frente.jpg",
        },
        {
            "nome": "Abandonado - em construção",
            "imagem": "assets/images/menu/casa2pav.jpg",
        },
    ]

    cols, rows = 2, 3
    grid_width = LARGURA * 0.7
    grid_height = ALTURA * 0.6
    espacamento_x = grid_width * 0.05
    espacamento_y = grid_height * 0.05
    largura_fase = (grid_width - espacamento_x * (cols - 1)) / cols
    altura_fase = (grid_height - espacamento_y * (rows - 1)) / rows

    # Centralização de grid na tela
    grid_x = (LARGURA - grid_width) / 2
    grid_y = (ALTURA - grid_height) / 2

    botoes_fases = []
    imagens_fases = []
    for i, fase in enumerate(fases):
        col = i % cols
        row = i // cols
        x = grid_x + col * (largura_fase + espacamento_x)
        y = grid_y + row * (altura_fase + espacamento_y)
        rect = pygame.Rect(x, y, largura_fase, altura_fase)
        botoes_fases.append((rect, fase["nome"]))

        try:
            img = pygame.image.load(fase["imagem"])
            img = pygame.transform.scale(
                img, (int(largura_fase), int(altura_fase * 0.7))
            )
        except:
            img = None
        imagens_fases.append(img)

    # Botão de voltar ao menu
    largura_voltar = LARGURA * 0.15
    altura_voltar = ALTURA * 0.05
    voltar_botao = pygame.Rect(
        (LARGURA - largura_voltar) // 2, ALTURA * 0.9, largura_voltar, altura_voltar
    )

    while True:
        if fundo:
            tela.blit(fundo, (0, 0))
        else:
            tela.fill(CINZA)

        titulo = fonte.render("Selecione uma fase", True, BRANCO)
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ALTURA * 0.03))

        for i, (rect, nome) in enumerate(botoes_fases):
            pygame.draw.rect(tela, MARROM_ESCURO, rect, border_radius=12)

            if imagens_fases[i]:
                tela.blit(imagens_fases[i], (rect.x, rect.y))

            nome_texto = fonte.render(nome, True, BRANCO)
            texto_x = rect.x + (rect.width - nome_texto.get_width()) // 2
            texto_y = rect.y + rect.height * 0.75
            tela.blit(nome_texto, (texto_x, texto_y))

        pygame.draw.rect(tela, MARROM_ESCURO, voltar_botao, border_radius=10)
        voltar_texto = fonte.render("Voltar ao Menu", True, BRANCO)
        voltar_rect = voltar_texto.get_rect(center=voltar_botao.center)
        tela.blit(voltar_texto, voltar_rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # Checa botões de Fase
                for i, (rect, nome) in enumerate(botoes_fases):
                    if rect.collidepoint(evento.pos):
                        
                        def resetar_musica():
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("assets/music/ambiente.mp3")
                            pygame.mixer.music.set_volume(volume)
                            pygame.mixer.music.play(-1)

                        if nome == "Casa":
                            executar_fase(tela, fonte, LARGURA, ALTURA, FASE_CASA_CONFIG, resetar_musica)
                            
                        elif nome == "Galpão Comercial":
                            executar_fase(tela, fonte, LARGURA, ALTURA, FASE_COMERCIAL_CONFIG, resetar_musica)
                            
                if voltar_botao.collidepoint(evento.pos):
                    return # Volta ao menú principal


if __name__ == "__main__":
    menu()