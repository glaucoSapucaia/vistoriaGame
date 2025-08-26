def cena_escritorio():
    print("\n🏚️  Você está no escritório de um imóvel para vistoria.\n")
    print("1. Examinar a sala")
    print("2. Consultar anotações")
    escolha = input("\nDigite sua escolha: ")

    if escolha == "1":
        print("\n📋 Você nota rachaduras nas paredes e cheiro de mofo.")
    elif escolha == "2":
        print("\n🗒️  As anotações indicam histórico de reformas em 2021.")
    else:
        print("\n❌ Escolha inválida.")
