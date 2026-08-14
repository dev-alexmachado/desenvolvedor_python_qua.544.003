import modulo as m


def main():
    m.limpar()

    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe a idade: "))

    print(f"{nome} é {m.maioridade(idade)}")

if __name__ == "__main__":
    main()