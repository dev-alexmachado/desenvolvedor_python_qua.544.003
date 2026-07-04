# importação da biblioteca
import os

# laço de repetição
while True:
    # limpa tela do terminal
    os.system("cls" if os.name == "nt" else "clear")

    # entrada de dados
    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe a idade: "))
    cpf = input("Informe o CPF: ").strip()
    email = input("Informe o e-mail: ").strip().lower()

    os.system("cls" if os.name == "nt" else "clear")

    # saída de dados
    print(f"Nome: {nome}.")
    print(f"Idade: {idade}.")
    print(f"CPF: {cpf}.")
    print(f"E-mail: {email}.")

    # menu
    print("1 - Informar dados de outro usuário")
    print("2 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case "1":
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")