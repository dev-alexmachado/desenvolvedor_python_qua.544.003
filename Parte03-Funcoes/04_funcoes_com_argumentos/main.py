import math
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def area_quadrilatero(b, h):
    return b*h

def area_triangulo(b, h):
    return (b*h)/2

def area_circulo(r):
    return math.pi*(r**2)


# algoritmo principal
limpar()

while True:
    print("1 - Calcular área do quadrilátero.")
    print("2 - Calcular área do triângulo.")
    print("3 - Calcular área do círculo.")
    print("4 - Sair do programa.")
    opcao = input("Informe a opção desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do quadrilátero é {area_quadrilatero(b, h)}.")
            continue
        case "2":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do triângulo é {area_triangulo(b, h)}.")
            continue
        case "3":
            r = float(input("Informe o valor do raio: ").replace(",","."))
            print(f"Área do círculo é {area_circulo(r)}.")
            continue
        case "4":
            break
        case _:
            print("Opção inválida.")
            continue