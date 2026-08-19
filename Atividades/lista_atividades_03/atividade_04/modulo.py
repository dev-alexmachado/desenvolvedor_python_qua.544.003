import math
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def potencia(x, y):
    return x**y

def raiz(x):
    return math.sqrt(x)

def volume_cubico(b, l, h):
    return b*l*h

def volume_cilindro(r, h):
    return math.pi*r*h