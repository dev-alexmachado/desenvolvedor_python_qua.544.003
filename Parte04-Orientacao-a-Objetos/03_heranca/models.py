class Pessoa:
    def __init__(self,email,telefone,endereco):
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self,razao_social,nome_fantasia,cnpj,email,telefone,endereco):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"Nome jurídico: {self.razao_social}")
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ da empresa: {self.cnpj}")
        super().exibir_dados()