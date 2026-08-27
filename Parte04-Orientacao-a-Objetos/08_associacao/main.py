from models import Endereco, Pessoa


def main():
    endereco = Endereco(uf="",cidade="")
    usuario = Pessoa(nome="",endereco=endereco)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.endereco.uf = input("Informe o estado: ").strip().upper()
    usuario.endereco.cidade = input("Informe o nome da cidade: ").strip()

    usuario.apresentar_endereco()


if __name__ == "__main__":
    main()