class Pai:
    def __init__(self,nome,cpf,email,telefone,profissao):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__profissao = profissao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self,profissao):
        self.__profissao = profissao

    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"E-mail: {self.__email}")
        print(f"Telefone: {self.__telefone}")
        print(f"Profissão: {self.__profissao}")


class Mae:
    def __init__(self,peso,altura,olhos,cabelo):
        self.__peso = peso
        self.__altura = altura
        self.__olhos = olhos
        self.__cabelo = cabelo

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self,peso):
        self.__peso = peso
        
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self,altura):
        self.__altura = altura

    @property
    def olhos(self):
        return self.__olhos

    @olhos.setter
    def olhos(self,olhos):
        self.__olhos = olhos

    @property
    def cabelo(self):
        return self.__cabelo

    @cabelo.setter
    def cabelo(self,cabelo):
        self.__cabelo = cabelo

    def mostrar_fisico(self):
        print(f"Peso: {self.__peso} kg")
        print(f"Altura: {self.__altura} metros")
        print(f"Olhos: {self.__olhos}")
        print(f"Cabelo: {self.__cabelo}")

class Filho(Pai, Mae):
    def __init__(self,nome,cpf,email,telefone,profissao,peso,altura,olhos,cabelo):
        Pai.__init__(self,nome,cpf,email,telefone,profissao)
        Mae.__init__(self,peso,altura,olhos,cabelo)