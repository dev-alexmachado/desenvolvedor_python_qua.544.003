import json
import os

usuarios = []
abrir = ""

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Gravar novo arquivo JSON")
    print("2 - Gravar em arquivo JSON existente")
    print("3 - Ler arquivo JSON")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    if opcao == "1" or opcao == "2":
        usuario = {}
        usuario['nome'] = input("Informe o nome: ").strip().title()
        usuario['email'] = input("Informe o e-mail: ").strip().lower()

        usuarios.append(usuario)

        match opcao:
            case "1":
                arquivo = input("Informe o nome do arquivo: ")

                with open(f"23_json/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
            case "2":
                if abrir:
                    with open(f"23_json/{abrir}.json","w",encoding="utf-8") as f:
                        json.dump(usuarios, f)
    else:
        match opcao:
            case "3":
                abrir = input("Informe o nome do arquivo que deseja abrir: ")

                with open(f"23_json/{abrir}.json","r",encoding="utf-8") as f:
                    usuarios = json.load(f)

                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
            case "4":
                break
            case _:
                print("Opção inválida.")
                continue