# tratamento de exceção
try:
    while True:
        nome = input("Informe o nome: ").strip().title()
        idade = int(input("Informe a idade: "))
        altura = float(input("Informe a altura em metros: ").replace(",", "."))

        if idade >= 12 and altura >= 1.25:
            print(f"{nome} está liberado.")
        else:
            print(f"Entrada de {nome} proibida.")
        
        print("1 - Passar novo pagante.")
        print("2 - Encerrar programa.")

        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue
except:
    print("Não foi possível registrar a entrada do pagante.")