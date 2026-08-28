class Pessoa:
    # construtor
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {len(self)} anos de idade e {float(self)} metros de altura."

    def __len__(self):
        return self.idade

    def __float__(self):
        return self.altura

    def __del__(self):
        print(f"Objeto {self} morreu com sucesso! ⚰️💀")