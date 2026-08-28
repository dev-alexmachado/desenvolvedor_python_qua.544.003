import os

from models import Pedido


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pedido = Pedido(valor1=0.0,valor2=0.0)

    limpar()

    pedido.valor1 = float(input("Informe o valor 1: ").replace(",","."))
    pedido.valor2 = float(input("Informe o valor 2: ").replace(",","."))

    limpar()

    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    operador = input("Informe a operação desejada: ").strip()
    print(pedido.calcular_total(operador=operador))


if __name__ == "__main__":
    main()