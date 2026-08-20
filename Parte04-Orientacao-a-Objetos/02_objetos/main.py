import os

from models import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    homem = Pessoa(nome="",idade=0,email="",telefone="")
    mulher = Pessoa(nome="",idade=0,email="",telefone="")

    limpar()

    # informa os dados do homem
    homem.nome = input("Informe o nome do homem: ").strip().title()
    homem.idade = int(input("Informe a idade do homem: "))
    homem.email = input("Informe o e-mail do homem: ").strip().lower()
    homem.telefone = input("Informe o telefone do homem: ").strip()

    limpar()

    # informa os dados da mulher
    mulher.nome = input("Informe o nome da mulher: ").strip().title()
    mulher.idade = int(input("Informe a idade da mulher: "))
    mulher.email = input("Informe o e-mail da mulher: ").strip().lower()
    mulher.telefone = input("Informe o e-mail da mulher: ").strip()

    limpar()

    # execução dos métodos
    print(homem.apresentar())
    print(mulher.cumprimentar(homem.nome))
    print(homem.cumprimentar(mulher.nome))


if __name__ == "__main__":
    main()