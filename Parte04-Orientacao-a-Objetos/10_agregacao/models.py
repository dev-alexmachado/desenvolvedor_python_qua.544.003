class Departamento:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome


class Empresa:
    def __init__(self,nome,departamento):
        self.__nome = nome
        self.__departamento = departamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self,departamento):
        self.__departamento = departamento

    def detalhes(self):
        return f"Empresa: {self.__nome}\nDepartamento: {self.__departamento.nome}"