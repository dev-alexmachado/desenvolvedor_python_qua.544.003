import os

# criar a lista
usuarios = []

# limpa a tela
os.system("cls" if os.name == "nt" else "clear")

while True:
    # menu
    print(f"{'-'*20} CRUDicionário {'-'*20}")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Alterar dados de um usuário")
    print("4 - Deletar usuário")
    print("5 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            # cria novo dicionário
            usuario = {}
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['email'] = input("Informe o e-mail: ").strip().lower()

            # adiciona dicionário na lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            continue
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            continue
        case "3":
            # TODO: fazer alterar usuário
            pass
        case "4":
            # TODO: excluir usuário
            pass
        case "5":
            break
        case _:
            print("Opção inválida.")
            continue