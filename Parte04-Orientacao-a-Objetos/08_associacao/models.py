class Endereco:
    def __init__(self,uf,cidade):
        self.__uf = uf
        self.__cidade = cidade

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self,uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self,cidade):
        self.__cidade = cidade

    def obter_endereco(self):
        return f"{self.__uf}, {self.__cidade}"


class Pessoa:
    def __init__(self,nome,endereco):
        self.__nome = nome
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,endereco):
        self.__endereco = endereco

    def apresentar_endereco(self):
        print(f"Nome: {self.__nome}")
        print(f"Endereço: {self.__endereco.obter_endereco()}")