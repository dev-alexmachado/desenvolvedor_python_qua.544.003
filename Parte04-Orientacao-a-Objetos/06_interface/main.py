import os
import datetime
from datetime import date

from models import Conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def hoje():
    return date.today().strftime("%d/%m/%Y")

def agora():
    return datetime.datetime.now().strftime("%H:%M:%S")

def main():
    cc = Conta(titular="",cpf="",agencia="1234-5",n_conta="10123-4",saldo=0.0)

    limpar()

    cc.titular = input("Informe o nome do titular da conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular da conta: ").strip()

    limpar()
    print(f"Conta criada no dia {hoje()} às {agora()}.")

    while True:
        print("0 - Sair do programa")
        print("1 - Consultar dados da conta")
        print("2 - Fazer depósito")
        print("3 - Fazer saque")
        opcao = input("Informe a opcao desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                break
            case "1":
                print(f"Data da consulta: {hoje()}")
                print(f"Hora da consulta: {agora()}")
                cc.consultar_conta()
                continue
            case "2":
                valor = float(input("Informe o valor a ser depositado: R$ ").replace(",","."))
                if valor >= 0:
                    print(f"Depósito efetuado com sucesso, às {agora()} do dia {hoje()}.")
                    print(f"Saldo atual: R$ {cc.fazer_deposito(valor):.2f}")
                else:
                    print("Depósito não pôde ser efetuado.")
                continue
            case "3":
                valor = float(input("Informe o valor do saque: R$ ").replace(",","."))
                if valor >= 0:
                    if valor <= cc.saldo:
                        print(f"Saque efetuado com sucesso às {agora()} do dia {hoje()}.")
                        print(f"Saldo atual: R$ {cc.fazer_saque(valor):.2f}")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Valor não pode ser sacado.")
                continue
            case _:
                print("Opção inválida.")
                continue


if __name__ == "__main__":
    main()