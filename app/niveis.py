
FASE_CASA_CONFIG = {
    "musica": "assets/music/apartamento.mp3",
    "visoes": {
        "Frente": "assets/images/fases/apartamento/frente.png",
        "Lateral": "assets/images/fases/apartamento/lateral.png",
        "Jardim": "assets/images/fases/apartamento/jardim.png",
    },
    "mao_prancheta": "assets/images/fases/prancheta.png",
    "hotspots": [
        {
            "visao": "Frente",
            "pos_relativa": (0.65, 0.15), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Hunn, parecem telhas convencionais. Me faz lembrar de casas antigas, da época de reis e colônias."
        },
        {
            "visao": "Frente",
            "pos_relativa": (0.5, 0.55),
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Que bela janela. Sem dúvidas é de madeira, mas eu nunca vi antes uma madeira tão lisa e brilhante. Também percebi desenhos na madeira, provavelmente feito por um artista."
        },
        {
            "visao": "Frente",
            "pos_relativa": (0.32, 0.38),
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Essa pintura parece ser densa e grossa. Também é bem áspera. Algo com textura."
        }
    ],
    "blac": {
        "perguntas": [
            ("1. Identificar o tipo de acabamento da fachada.", ["pintura convencional", "ceramica esmaltada", "revestimento especial"]),
            ("2. Identificar o tipo de esquadria.", ["madeira simples", "madeira trabalhada", "madeira padrão com veneziana"]),
            ("3. Identificar o tipo de telhado.", ["ceramica esmaltada", "ceramica colonial", "fibro cimento ondulada"]),
        ],
        "gabarito": ["revestimento especial", "madeira trabalhada", "ceramica colonial"]
    }
}

FASE_COMERCIAL_CONFIG = {
    "musica": "assets/music/apartamento.mp3", 
    "visoes": {
        "Frente": "assets/images/fases/galpao/frente.jpg",
        "Interior": "assets/images/fases/galpao/interior.jpg",
        "Fundos": "assets/images/fases/galpao/fundos.jpg"
    },
    "visoes_botoes": ["Frente", "Interior"], 
    "mao_prancheta": "assets/images/fases/prancheta.png",
    
    "trena_icone": "assets/images/fases/trena.png",
    "mensagens_trena": {
        "Frente": "As pilhas de pneus e entulho bloqueiam a passagem e a medição externa da lateral. Vou ter que encontrar outra forma de medir a área construída.",
        "Interior": "10m de Largura, 30m de Profundidade. A área do galpão confere perfeitamente com a área declarada no sistema e na planta aprovada. A altura do pé-direito também bate com os 5.5m.",
        "Fundos": "Medindo o puxadinho que não consta na Baixa de Construção: tem 4m de largura, 3m de profundidade e pé-direito de 3m. Preciso calcular a área construída total."
    },
    
    "hotspots": [
        
        {
            "visao": "Frente",
            "pos_relativa": (0.28, 0.40), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Pelas características da fachada e laterais, o imóvel não parece ter nenhuma mureta e possui pelo menos três paredes de alvenaria completas (que vão até o teto)."
        },
        {
            "visao": "Frente",
            "pos_relativa": (0.85, 0.50), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Uma pilha de pneus velhos, tambores e tranqueiras bloqueiam o acesso lateral pelo lado de fora. Terei de encontrar outra forma de inspecionar a lateral e a parede dos fundos."
        },

        {
            "visao": "Interior",
            "pos_relativa": (0.48, 0.15), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "A sustentação do telhado é feita por perfis de aço comuns que formam um vão livre entre as paredes laterais. Parece uma estrutura metálica comum neste tipo de construção."
        },
        {
            "visao": "Interior",
            "pos_relativa": (0.65, 0.05), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Olhando bem para a cobertura por dentro, nota-se o formato de trapézio das grandes chapas metálicas galvanizadas."
        },
        {
            "visao": "Interior",
            "pos_relativa": (0.49, 0.65), 
            "icone": "assets/images/fases/iconeInterrogacao.png", 
            "tamanho_icone": (40, 40),
            "texto": "Hmm... Essa porta azul nos fundos não constava na planta original. Onde isso vai dar?",
            "destino": "Fundos",
            "invisivel": True 
        },
        {
            "visao": "Interior",
            "pos_relativa": (0.80, 0.60), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Muitas ferramentas espalhadas e bastante marcas de graxa. Parece que os mecânicos estão em horário de almoço. Segundo a Ordem de Serviço, este local tem ocupação não residencial ('NR')."
        },

        {
            "visao": "Fundos",
            "pos_relativa": (0.45, 0.50), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Mas que cheiro terrível! Fizeram um banheiro improvisado aqui atrás! Eu que não quero ficar aqui. Essa construção é posterior à Baixa e não foi declarada nem mesmo está representada na planta."
        },
        {
            "visao": "Fundos",
            "pos_relativa": (0.25, 0.70), 
            "icone": "assets/images/fases/iconeInterrogacao.png",
            "tamanho_icone": (40, 40),
            "texto": "Mais pneus e entulho bloqueando a passagem lateral. Além da área construída irregular, o proprietário acumulou pneus velhos e entulho no recuo do lote. Definitivamente, este espaço já viu melhores dias."
        }
    ],
    "blac": {
        "perguntas": [
            ("1. Campo 20: Tipo de Parede do Galpão?", ["Aberto", "Meia Parede", "Fechado"]),
            ("2. Campo 21: Estrutura da Cobertura?", ["Metálica Convencional", "Metálica Espacial", "Madeira"]),
            ("3. Campo 14: Material das Telhas?", ["Fibrocimento (Amianto)", "Cerâmica Colonial", "Chapa Galvanizada"]),
            ("4. Campo 05.3: Digite a Área Construída aferida (m²):", "INPUT_NUMERIC"),
        ],
        "gabarito": ["Fechado", "Metálica Convencional", "Chapa Galvanizada", "312"]
    }
}