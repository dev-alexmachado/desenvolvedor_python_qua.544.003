import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="",email="",telefone="")

    limpar()

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()

    limpar()

    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    limpar()

    print(f"Nome do usuário: {usuario.nome}")
    print(f"CPF do usuário: {usuario.cpf}")
    print(f"E-mail do usuário: {usuario.email}")
    print(f"Telefone do usuário: {usuario.telefone}")

    print(f"Nome da empresa: {empresa.nome_fantasia}")
    print(f"CNPJ da empresa: {empresa.cnpj}")
    print(f"E-mail da empresa: {empresa.email}")
    print(f"Telefone da empresa: {empresa.telefone}")


if __name__ == "__main__":
    main()