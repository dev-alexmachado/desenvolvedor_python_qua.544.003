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
            nome = input("Informe o nome a ser pesquisado: ").strip().title()
            for usuario in usuarios:
                if nome in usuario['nome']:
                    # 2º menu
                    print("nome")
                    print("cpf")
                    print("email")
                    print("cancelar")
                    alterar = input("Qual chave deseja alterar? ").strip().lower()
                    if alterar in usuario:
                        usuario[alterar] = input("Informe o novo valor: ").strip()
                        print("Alterado com sucesso.")
                else:
                    # REVIEW: mensagem bugada
                    print("Usuário não encontrado.")
            continue
        case "4":
            nome = input("Informe o nome a ser deletado: ").strip().title()
            for usuario in usuarios:
                if nome in usuario['nome']:
                    usuarios.remove(usuario)
                    print("Usuário deletado com sucesso!")
                else:
                    # REVIEW: mensagem bugada
                    print("Usuário não encontrado.")
            continue
        case "5":
            break
        case _:
            print("Opção inválida.")
            continue