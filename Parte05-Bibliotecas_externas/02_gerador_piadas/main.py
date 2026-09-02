import pyjokes
from deep_translator import GoogleTranslator

import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_piada():
    tradutor = GoogleTranslator(source="auto", target="pt")
    piada = pyjokes.get_joke()
    return tradutor.translate(piada)

def main():
    limpar()
    while True:
        print("0 - Sair do programa")
        print("1 - Gerar nova piada")
        opcao = input("Informe a opção desejada: ").strip()
        limpar()
        if opcao == "0":
            break
        elif opcao == "1":
            nova_piada = gerar_piada()
            print(nova_piada)
            continue
        else:
            print("Opção inválida.")
            continue


if __name__ == "__main__":
    main()