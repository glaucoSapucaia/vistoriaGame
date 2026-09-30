
import pygame
import sys

def executar_fase(tela, fonte, largura, altura, config, voltar_menu_callback):
    # Cores
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    MARROM_ESCURO = (60, 40, 30)
    CINZA = (30, 30, 30)

    # Inicialização de Mídia Dinâmica
    pygame.mixer.music.load(config["musica"])
    pygame.mixer.music.play(-1)

    visoes_imagens = {}
    for nome, caminho in config["visoes"].items():
        try:
            img = pygame.image.load(caminho).convert_alpha()
            visoes_imagens[nome] = pygame.transform.scale(img, (largura, altura))
        except:
            visoes_imagens[nome] = pygame.Surface((largura, altura))
            visoes_imagens[nome].fill(PRETO)

    mao_esquerda = pygame.image.load(config["mao_prancheta"]).convert_alpha()

    # Prepara os Rects dos Hotspots - pos_relativa
    hotspots_processados = []
    for hs in config["hotspots"]:
        icone = pygame.image.load(hs["icone"]).convert_alpha()
        icone = pygame.transform.scale(icone, hs["tamanho_icone"])
        x = int(largura * hs["pos_relativa"][0])
        y = int(altura * hs["pos_relativa"][1])
        rect = pygame.Rect(x, y, hs["tamanho_icone"][0], hs["tamanho_icone"][1])
        hotspots_processados.append({
            "visao": hs["visao"],
            "icone": icone,
            "rect": rect,
            "pos": (x, y),
            "texto": hs["texto"]
        })

    prancheta_rect = pygame.Rect(
        int(largura * 0.05), int(altura * 0.55), int(largura * 0.18), int(altura * 0.3)
    )

    # Lista de visões para os botões inferiores
    chaves_visao = list(config["visoes"].keys())
    visao_atual = chaves_visao[0]
    
    mostrar_blac = False
    texto_ativo = ""

    botoes_visao = []
    margem = 30
    botao_largura = largura * 0.15
    botao_altura = altura * 0.06
    espacamento = botao_largura * 0.1
    total_largura = (botao_largura + espacamento) * len(chaves_visao) - espacamento
    inicio_x = (largura - total_largura) // 2
    y_botao = altura - botao_altura - margem

    for i, nome in enumerate(chaves_visao):
        x = inicio_x + i * (botao_largura + espacamento)
        botoes_visao.append((pygame.Rect(x, y_botao, botao_largura, botao_altura), nome))

    # Estado do BLAC
    perguntas_config = config["blac"]["perguntas"]
    gabarito = config["blac"]["gabarito"]
    respostas = [None] * len(perguntas_config)
    mensagem_resultado = ""
    mostrar_mensagem = False
    tempo_mensagem = 0
    op_botoes = []

    sair_texto = fonte.render("Sair da fase", True, BRANCO)
    sair_rect = sair_texto.get_rect()
    sair_rect.width += 20
    sair_rect.height += 10
    sair_rect.bottomright = (largura - 30, altura - 30)

    rodando = True
    while rodando:
        doc_largura = int(largura * 0.5)
        doc_altura = int(altura * 0.65)
        doc_x = int((largura - doc_largura) / 2)
        doc_y = int((altura - doc_altura) / 2)
        doc_rect = pygame.Rect(doc_x, doc_y, doc_largura, doc_altura)

        botao_x_tam = 30
        botao_x_pos = (doc_x + doc_largura - botao_x_tam - 10, doc_y + 10)
        botao_x_rect = pygame.Rect(botao_x_pos[0], botao_x_pos[1], botao_x_tam, botao_x_tam)

        terminar_largura = 180
        terminar_altura = 40
        terminar_x = doc_rect.right - terminar_largura - 20
        terminar_y = doc_rect.bottom - terminar_altura - 20
        terminar_rect = pygame.Rect(terminar_x, terminar_y, terminar_largura, terminar_altura)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if sair_rect.collidepoint(evento.pos):
                    voltar_menu_callback()
                    return

                # Alternar Visões
                for rect, nome in botoes_visao:
                    if rect.collidepoint(evento.pos):
                        visao_atual = nome
                        texto_ativo = ""

                # Interação BLAC
                if mostrar_blac:
                    if botao_x_rect.collidepoint(evento.pos) or not doc_rect.collidepoint(evento.pos):
                        mostrar_blac = False
                        mensagem_resultado = ""
                        op_botoes = []
                    elif terminar_rect.collidepoint(evento.pos):
                        if respostas == gabarito:
                            mensagem_resultado = "✅ Vistoria concluída com sucesso!"
                            mostrar_mensagem = True
                            tempo_mensagem = pygame.time.get_ticks()
                        else:
                            mensagem_resultado = "❌ Respostas incorretas. Tente novamente."
                            mostrar_mensagem = True
                            tempo_mensagem = pygame.time.get_ticks()
                    else:
                        for rect, pergunta_idx, opcao in op_botoes:
                            if rect.collidepoint(evento.pos):
                                respostas[pergunta_idx] = opcao

                elif prancheta_rect.collidepoint(evento.pos):
                    mostrar_blac = True
                
                # Clique em Hotspots Dinâmicos
                else:
                    clicou_em_hotspot = False
                    for hs in hotspots_processados:
                        if hs["visao"] == visao_atual and hs["rect"].collidepoint(evento.pos):
                            texto_ativo = hs["texto"]
                            clicou_em_hotspot = True
                            break
                    if not clicou_em_hotspot:
                        texto_ativo = ""

        # --- Renderização ---
        tela.blit(visoes_imagens[visao_atual], (0, 0))

        prancheta = pygame.transform.scale(mao_esquerda, (int(largura * 0.18), int(altura * 0.3)))
        tela.blit(prancheta, (prancheta_rect.x, prancheta_rect.y))

        # Renderiza Hotspots Dinâmicos
        for hs in hotspots_processados:
            if hs["visao"] == visao_atual:
                tela.blit(hs["icone"], hs["pos"])

        # Renderiza Caixa de Texto Ativo
        if texto_ativo:
            largura_caixa = int(largura * 0.5)
            altura_caixa = int(altura * 0.2)
            x_caixa = (largura - largura_caixa) // 2
            y_caixa = int(altura * 0.1)

            pygame.draw.rect(tela, (250, 250, 240), (x_caixa, y_caixa, largura_caixa, altura_caixa), border_radius=8)
            pygame.draw.rect(tela, (60, 60, 60), (x_caixa, y_caixa, largura_caixa, altura_caixa), 2, border_radius=8)

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

        # Renderiza Documento BLAC
        if mostrar_blac:
            pygame.draw.rect(tela, (245, 245, 220), doc_rect, border_radius=8)
            pygame.draw.rect(tela, (50, 50, 50), doc_rect, 2, border_radius=8)

            pygame.draw.rect(tela, (200, 50, 50), botao_x_rect, border_radius=5)
            pygame.draw.line(tela, BRANCO, (botao_x_rect.left + 6, botao_x_rect.top + 6), (botao_x_rect.right - 6, botao_x_rect.bottom - 6), 3)
            pygame.draw.line(tela, BRANCO, (botao_x_rect.left + 6, botao_x_rect.bottom - 6), (botao_x_rect.right - 6, botao_x_rect.top + 6), 3)

            espacamento_y = 50
            inicio_y = doc_y + 60
            op_botoes = []

            for i, (pergunta, opcoes) in enumerate(perguntas_config):
                tela.blit(fonte.render(pergunta, True, PRETO), (doc_x + 20, inicio_y))
                for j, opcao in enumerate(opcoes):
                    rect_op = pygame.Rect(doc_x + 40, inicio_y + 30 + j * 30, 20, 20)
                    pygame.draw.rect(tela, BRANCO, rect_op)
                    pygame.draw.rect(tela, PRETO, rect_op, 2)
                    if respostas[i] == opcao:
                        pygame.draw.circle(tela, PRETO, rect_op.center, 7)
                    tela.blit(fonte.render(opcao, True, PRETO), (rect_op.right + 10, rect_op.top - 2))
                    op_botoes.append((rect_op, i, opcao))
                inicio_y += len(opcoes) * 30 + espacamento_y

            pygame.draw.rect(tela, (0, 120, 0), terminar_rect, border_radius=8)
            texto_botao = fonte.render("Finalizar Vistoria", True, BRANCO)
            tela.blit(texto_botao, texto_botao.get_rect(center=terminar_rect.center))

            if mostrar_mensagem:
                caixa_largura = int(doc_largura * 0.9)
                caixa_altura = 60
                caixa_x = doc_x + (doc_largura - caixa_largura) // 2
                caixa_y = doc_y + doc_altura - caixa_altura - 80

                cor_fundo = (200, 230, 200) if mensagem_resultado.startswith("✅") else (250, 180, 180)
                cor_texto = (0, 80, 0) if mensagem_resultado.startswith("✅") else (120, 0, 0)

                pygame.draw.rect(tela, cor_fundo, (caixa_x, caixa_y, caixa_largura, caixa_altura), border_radius=8)
                pygame.draw.rect(tela, (50, 50, 50), (caixa_x, caixa_y, caixa_largura, caixa_altura), 2, border_radius=8)

                texto_msg = fonte.render(mensagem_resultado, True, cor_texto)
                tela.blit(texto_msg, texto_msg.get_rect(center=(doc_x + doc_largura // 2, caixa_y + caixa_altura // 2)))

                if pygame.time.get_ticks() - tempo_mensagem > 3000:
                    mostrar_mensagem = False
                    if mensagem_resultado.startswith("✅"):
                        voltar_menu_callback()
                        return

        # Renderiza Botões Inferiores
        for rect, nome in botoes_visao:
            cor = MARROM_ESCURO if visao_atual == nome else CINZA
            pygame.draw.rect(tela, cor, rect, border_radius=8)
            texto = fonte.render(nome, True, BRANCO)
            tela.blit(texto, texto.get_rect(center=rect.center))

        # Renderiza Botão Sair da Fase
        pygame.draw.rect(tela, (180, 50, 50), sair_rect, border_radius=8)
        tela.blit(sair_texto, sair_texto.get_rect(center=sair_rect.center))

        pygame.display.flip()