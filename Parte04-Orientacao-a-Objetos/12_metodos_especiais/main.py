import os

from models import Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="",idade=0,altura=0.0)
    limpar()
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.altura = float(input("Informe a altura: ").replace(",","."))

    limpar()
    print(usuario)
    del(usuario)


if __name__ == "__main__":
    main()