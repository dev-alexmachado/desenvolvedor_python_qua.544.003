import os

from models import Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    usuario = Pessoa(nome="",cpf="",email="",telefone="")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()

    limpar()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")


if __name__ == "__main__":
    main()