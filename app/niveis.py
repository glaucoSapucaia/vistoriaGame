
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