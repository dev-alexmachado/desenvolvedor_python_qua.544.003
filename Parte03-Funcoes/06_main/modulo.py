import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def maioridade(idade):
    return "maior de idade." if idade >= 18 else "menor de idade."