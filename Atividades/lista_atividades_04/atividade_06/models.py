from abc import ABC, abstractmethod
from dataclasses import dataclass

class IConta(ABC):
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def gerar_extrato(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"

@dataclass
class Conta(IConta):
    titular: Pessoa
    agencia: str
    n_conta: str
    saldo: float

    def consultar_dados(self):
        print(f"Titular da conta: {self.titular.nome}")
        print(f"CPF da conta: {self.titular.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.n_conta}")
        print(f"Saldo: R${self.saldo:.2f}")

    def gerar_extrato(self):
        dados = {
            "Titular": self.titular.nome,
            "CPF": self.titular.cpf,
            "Agência": self.agencia,
            "Número da Conta": self.n_conta,
            "Saldo": self.saldo
        }
        with open("extrato.txt", "w") as arquivo:
            for chave, valor in dados.items():
                arquivo.write(f"{chave}: {valor}\n")
        print("Extrato gerado com sucesso no arquivo.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        else:
            return "Saldo insuficiente ou valor de saque inválido."