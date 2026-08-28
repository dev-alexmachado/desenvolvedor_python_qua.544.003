import os

from models import PessoaFisica, PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(
        nome="",cpf="",profissao="",idade=0,salario=0.0,
        telefone="",email=""
    )
    empresa = PessoaJuridica(
        razao_social="",nome_fantasia="",cnpj="",
        valor_mercado=0.0,telefone="",email=""
    )

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.profissao = input("Informe a profissão do usuário: ")
    usuario.idade = int(input("Informe a idade do usuário: "))
    usuario.telefone = input("Informe o telefone do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.salario = float(input("Informe o salário do usuário: R$ ").replace(",","."))

    empresa.nome_fantasia = input("Informe o nome da empresa: ")
    empresa.razao_social = input("Informe a razão social: ")
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
    empresa.valor_mercado = float(input("Informe o valor de mercado da empresa: R$ ").replace(",","."))

    limpar()
    print(usuario)
    print(empresa)

    del(usuario)
    del(empresa)


if __name__ == "__main__":
    main()