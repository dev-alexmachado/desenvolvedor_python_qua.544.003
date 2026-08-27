from models import Carro


def main():
    carro = Carro(modelo="",potencia=520)

    carro.modelo = input("Informe o modelo do carro: ")
    print(carro.detalhes())


if __name__ == "__main__":
    main()