import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def equacao_primeiro_grau(a, b):
    # a*x+b = 0
    return -b/a
