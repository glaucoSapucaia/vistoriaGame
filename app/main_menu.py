import pygame
import sys

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

# Fonte
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

# Botão sair (abaixo do iniciar)
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
                    selecao_fases()  # vai para seleção de fases
                elif botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()  # Sai do jogo
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
            "nome": "Comercial - em construção",
            "imagem": "assets/images/menu/casa2pav.jpg",
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

    # Centralizar grid na tela
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

        # Botão Voltar
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
                for i, (rect, nome) in enumerate(botoes_fases):
                    if rect.collidepoint(evento.pos):
                        if nome == "Casa":
                            fase_apartamento()
                if voltar_botao.collidepoint(evento.pos):
                    return  # volta ao menu


def fase_apartamento():
    visoes = {
        "Frente": "assets/images/fases/apartamento/frente.png",
        "Lateral": "assets/images/fases/apartamento/lateral.png",
        "Jardim": "assets/images/fases/apartamento/jardim.png",
    }

    mao_esquerda = pygame.image.load("assets/images/fases/prancheta.png")

    icone_telhado = pygame.image.load("assets/images/fases/iconeInterrogacao.png")
    icone_janela = pygame.image.load("assets/images/fases/iconeInterrogacao.png")
    icone_parede = pygame.image.load("assets/images/fases/iconeInterrogacao.png")

    icone_telhado = pygame.transform.scale(icone_telhado, (40, 40))
    icone_janela = pygame.transform.scale(icone_janela, (40, 40))
    icone_parede = pygame.transform.scale(icone_parede, (40, 40))

    pos_telhado = (int(LARGURA * 0.65), int(ALTURA * 0.15))
    pos_parede = (int(LARGURA * 0.32), int(ALTURA * 0.38))
    pos_janela = (int(LARGURA * 0.5), int(ALTURA * 0.55))

    ret_telhado = pygame.Rect(pos_telhado[0], pos_telhado[1], 40, 40)
    ret_janela = pygame.Rect(pos_janela[0], pos_janela[1], 40, 40)
    ret_parede = pygame.Rect(pos_parede[0], pos_parede[1], 40, 40)

    prancheta_rect = pygame.Rect(
        int(LARGURA * 0.05), int(ALTURA * 0.55), int(LARGURA * 0.18), int(ALTURA * 0.3)
    )

    visao_atual = "Frente"
    mostrar_blac = False
    texto_ativo = ""

    botoes = []
    margem = 30
    botao_largura = LARGURA * 0.15
    botao_altura = ALTURA * 0.06
    espacamento = botao_largura * 0.1
    total_largura = (botao_largura + espacamento) * len(visoes) - espacamento
    inicio_x = (LARGURA - total_largura) // 2
    y_botao = ALTURA - botao_altura - margem

    for i, nome in enumerate(visoes.keys()):
        x = inicio_x + i * (botao_largura + espacamento)
        botoes.append((pygame.Rect(x, y_botao, botao_largura, botao_altura), nome))

    # *** Música da fase ***
    pygame.mixer.music.load("assets/music/apartamento.mp3")
    pygame.mixer.music.play(-1)

    rodando = True

    # Estado do documento interativo
    respostas = [None, None, None]
    mensagem_resultado = ""
    mostrar_mensagem = False
    tempo_mensagem = 0
    op_botoes = []

    TIPOS_ACABAMENTO = [
        "pintura convencional",
        "ceramica esmaltada",
        "revestimento especial",
    ]
    TIPOS_ESQUADRIA = [
        "madeira simples",
        "madeira trabalhada",
        "madeira padrão com veneziana",
    ]
    TIPOS_TELHADO = [
        "ceramica esmaltada",
        "ceramica colonial",
        "fibro cimento ondulada",
    ]

    while rodando:
        doc_largura = int(LARGURA * 0.5)
        doc_altura = int(ALTURA * 0.65)
        doc_x = int((LARGURA - doc_largura) / 2)
        doc_y = int((ALTURA - doc_altura) / 2)
        doc_rect = pygame.Rect(doc_x, doc_y, doc_largura, doc_altura)

        botao_x_tam = 30
        botao_x_pos = (doc_x + doc_largura - botao_x_tam - 10, doc_y + 10)
        botao_x_rect = pygame.Rect(
            botao_x_pos[0], botao_x_pos[1], botao_x_tam, botao_x_tam
        )

        terminar_largura = 180
        terminar_altura = 40
        terminar_x = doc_rect.right - terminar_largura - 20
        terminar_y = doc_rect.bottom - terminar_altura - 20
        terminar_rect = pygame.Rect(
            terminar_x, terminar_y, terminar_largura, terminar_altura
        )

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if sair_rect.collidepoint(evento.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/music/ambiente.mp3")
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1)
                    menu()
                    return

                for rect, nome in botoes:
                    if rect.collidepoint(evento.pos):
                        visao_atual = nome
                        texto_ativo = ""

                if mostrar_blac:
                    if botao_x_rect.collidepoint(evento.pos):
                        mostrar_blac = False
                        mensagem_resultado = ""
                        op_botoes = []
                    elif terminar_rect.collidepoint(evento.pos):
                        if respostas == [
                            "revestimento especial",
                            "madeira trabalhada",
                            "ceramica colonial",
                        ]:
                            mensagem_resultado = "✅ Vistoria concluída com sucesso!"
                            mostrar_mensagem = True
                            tempo_mensagem = pygame.time.get_ticks()
                            # Mantém o documento aberto para mostrar a mensagem
                        else:
                            mensagem_resultado = (
                                "❌ Respostas incorretas. Tente novamente."
                            )
                            mostrar_mensagem = True
                            tempo_mensagem = pygame.time.get_ticks()
                    else:
                        # NOVO: Fechar documento se clicar fora dele (e fora dos botões dentro do documento)
                        if not doc_rect.collidepoint(evento.pos):
                            mostrar_blac = False
                            mensagem_resultado = ""
                            op_botoes = []
                        else:
                            for rect, pergunta_idx, opcao in op_botoes:
                                if rect.collidepoint(evento.pos):
                                    respostas[pergunta_idx] = opcao

                elif prancheta_rect.collidepoint(evento.pos):
                    mostrar_blac = True
                elif visao_atual == "Frente":
                    if ret_telhado.collidepoint(evento.pos):
                        texto_ativo = "Hunn, parecem telhas convencionais. Me faz lembrar de casas antigas, da época de reis e colônias."
                    elif ret_janela.collidepoint(evento.pos):
                        texto_ativo = "Que bela janela. Sem dúvidas é de madeira, mas eu nunca vi antes uma madeira tão lisa e brilhante. Também percebi desenhos na madeira, provavelmente feito por um artista."
                    elif ret_parede.collidepoint(evento.pos):
                        texto_ativo = "Essa pintura parece ser densa e grossa. Também é bem áspera. Algo com textura."
                    else:
                        texto_ativo = ""
                else:
                    texto_ativo = ""

        # Fundo da visão atual
        try:
            imagem_visao = pygame.image.load(visoes[visao_atual])
            imagem_visao = pygame.transform.scale(imagem_visao, (LARGURA, ALTURA))
            tela.blit(imagem_visao, (0, 0))
        except:
            tela.fill(PRETO)

        # Prancheta (mão esquerda)
        prancheta = pygame.transform.scale(
            mao_esquerda, (int(LARGURA * 0.18), int(ALTURA * 0.3))
        )
        tela.blit(prancheta, (prancheta_rect.x, prancheta_rect.y))

        # Ícones clicáveis — mostrar apenas se visão for "Frente"
        if visao_atual == "Frente":
            tela.blit(icone_telhado, pos_telhado)
            tela.blit(icone_janela, pos_janela)
            tela.blit(icone_parede, pos_parede)

        # Documento BLAC — desenha por cima de tudo, com botão "X"
        if mostrar_blac:
            pygame.draw.rect(tela, (245, 245, 220), doc_rect, border_radius=8)
            pygame.draw.rect(tela, (50, 50, 50), doc_rect, 2, border_radius=8)

            # Botão X
            pygame.draw.rect(tela, (200, 50, 50), botao_x_rect, border_radius=5)
            pygame.draw.line(
                tela,
                (255, 255, 255),
                (botao_x_rect.left + 6, botao_x_rect.top + 6),
                (botao_x_rect.right - 6, botao_x_rect.bottom - 6),
                3,
            )
            pygame.draw.line(
                tela,
                (255, 255, 255),
                (botao_x_rect.left + 6, botao_x_rect.bottom - 6),
                (botao_x_rect.right - 6, botao_x_rect.top + 6),
                3,
            )

            perguntas = [
                ("1. Identificar o tipo de acabamento da fachada.", TIPOS_ACABAMENTO),
                ("2. Identificar o tipo de esquadria.", TIPOS_ESQUADRIA),
                ("3. Identificar o tipo de telhado.", TIPOS_TELHADO),
            ]

            espacamento = 50
            inicio_y = doc_y + 60
            op_botoes = []

            for i, (pergunta, opcoes) in enumerate(perguntas):
                tela.blit(
                    fonte.render(pergunta, True, (0, 0, 0)), (doc_x + 20, inicio_y)
                )
                for j, opcao in enumerate(opcoes):
                    rect_op = pygame.Rect(doc_x + 40, inicio_y + 30 + j * 30, 20, 20)
                    pygame.draw.rect(tela, (255, 255, 255), rect_op)
                    pygame.draw.rect(tela, (0, 0, 0), rect_op, 2)
                    if respostas[i] == opcao:
                        pygame.draw.circle(tela, (0, 0, 0), rect_op.center, 7)
                    tela.blit(
                        fonte.render(opcao, True, (0, 0, 0)),
                        (rect_op.right + 10, rect_op.top - 2),
                    )
                    op_botoes.append((rect_op, i, opcao))
                inicio_y += len(opcoes) * 30 + espacamento

            # Botão "Finalizar Vistoria"
            pygame.draw.rect(tela, (0, 120, 0), terminar_rect, border_radius=8)
            texto_botao = fonte.render("Finalizar Vistoria", True, (255, 255, 255))
            texto_rect = texto_botao.get_rect(center=terminar_rect.center)
            tela.blit(texto_botao, texto_rect)

            # Mensagem de resultado
            if mostrar_mensagem:
                caixa_largura = int(doc_largura * 0.9)
                caixa_altura = 60
                caixa_x = doc_x + (doc_largura - caixa_largura) // 2
                caixa_y = doc_y + doc_altura - caixa_altura - 80

                cor_fundo = (
                    (200, 230, 200)
                    if mensagem_resultado.startswith("✅")
                    else (250, 180, 180)
                )
                cor_texto = (
                    (0, 80, 0) if mensagem_resultado.startswith("✅") else (120, 0, 0)
                )

                pygame.draw.rect(
                    tela,
                    cor_fundo,
                    (caixa_x, caixa_y, caixa_largura, caixa_altura),
                    border_radius=8,
                )
                pygame.draw.rect(
                    tela,
                    (50, 50, 50),
                    (caixa_x, caixa_y, caixa_largura, caixa_altura),
                    2,
                    border_radius=8,
                )

                texto_msg = fonte.render(mensagem_resultado, True, cor_texto)
                texto_msg_rect = texto_msg.get_rect(
                    center=(doc_x + doc_largura // 2, caixa_y + caixa_altura // 2)
                )
                tela.blit(texto_msg, texto_msg_rect)

                # Oculta mensagem após 3 segundos e reseta respostas se sucesso
                if pygame.time.get_ticks() - tempo_mensagem > 3000:
                    mostrar_mensagem = False
                    if mensagem_resultado.startswith("✅"):
                        respostas = [None, None, None]
                        mostrar_blac = False  # Fecha documento após sucesso
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets/music/ambiente.mp3")
                        pygame.mixer.music.set_volume(0.3)
                        pygame.mixer.music.play(-1)
                        menu()  # Volta para o menu principal
                        return

        # Caixa de texto explicativa
        if texto_ativo:
            largura_caixa = int(LARGURA * 0.5)
            altura_caixa = int(ALTURA * 0.2)
            x_caixa = (LARGURA - largura_caixa) // 2
            y_caixa = int(ALTURA * 0.1)

            pygame.draw.rect(
                tela,
                (250, 250, 240),
                (x_caixa, y_caixa, largura_caixa, altura_caixa),
                border_radius=8,
            )
            pygame.draw.rect(
                tela,
                (60, 60, 60),
                (x_caixa, y_caixa, largura_caixa, altura_caixa),
                2,
                border_radius=8,
            )

            palavras = texto_ativo.split()
            linhas = []
            linha = ""

            for palavra in palavras:
                teste_linha = linha + palavra + " "
                if fonte.size(teste_linha)[0] < largura_caixa - 40:
                    linha = teste_linha
                else:
                    linhas.append(linha)
                    linha = palavra + " "
            linhas.append(linha)

            for i, linha in enumerate(linhas):
                texto = fonte.render(linha, True, (20, 20, 20))
                tela.blit(texto, (x_caixa + 20, y_caixa + 20 + i * 28))

        # Botões de visão
        for rect, nome in botoes:
            cor = MARROM_ESCURO if visao_atual == nome else CINZA
            pygame.draw.rect(tela, cor, rect, border_radius=8)
            texto = fonte.render(nome, True, BRANCO)
            texto_rect = texto.get_rect(center=rect.center)
            tela.blit(texto, texto_rect)

        # Botão "Sair da fase"
        sair_texto = fonte.render("Sair da fase", True, BRANCO)
        sair_rect = sair_texto.get_rect()
        sair_rect.width += 20
        sair_rect.height += 10
        sair_rect.bottomright = (LARGURA - 30, ALTURA - 30)

        pygame.draw.rect(tela, (180, 50, 50), sair_rect, border_radius=8)
        tela.blit(sair_texto, sair_texto.get_rect(center=sair_rect.center))

        pygame.display.flip()


if __name__ == "__main__":
    menu()
