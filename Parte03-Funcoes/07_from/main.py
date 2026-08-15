from modulo import limpar, somar, subtrair

def main():
    limpar()
    x = int(input("Informe o valor de X: "))
    y = int(input("Informe o valor de Y: "))
    limpar()
    print(f"O valor da soma é : {somar(x, y)}")
    print(f"O valor da subtração é : {subtrair(x, y)}")

if __name__ == "__main__":
    main()