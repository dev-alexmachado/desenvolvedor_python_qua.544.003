# classe Pessoa
class Pessoa:
    # método construtor
    def __init__(self,nome,idade,email,altura):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura

    # método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"E-mail: {self.email}")
        print(f"Altura: {self.altura} metros")


def main():
    # instancia a classe (cria o objeto)
    usuario = Pessoa(nome="",idade=0,email="",altura=0.0)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.altura = float(input("Informe a altura em metros: ").replace(",","."))

    usuario.exibir_dados()


if __name__ == "__main__":
    main()