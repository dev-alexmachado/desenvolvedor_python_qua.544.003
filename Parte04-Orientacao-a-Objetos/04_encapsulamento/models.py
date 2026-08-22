class Pessoa:
    def __init__(self,nome,cpf,email,telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone

        # métodos de acesso
        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            self.__nome = nome
            
        @property
        def cpf(self):
            return self.__cpf

        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, email):
            self.__email = email

        @property
        def telefone(self):
            return self.__telefone

        @telefone.setter
        def telefone(self, telefone):
            self.__telefone = telefone
