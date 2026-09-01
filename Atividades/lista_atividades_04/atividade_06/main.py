# TODO: atividade 06
import os

from models import Conta, Pessoa


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    usuario = Pessoa(nome="", cpf="")
    cc = Conta(titular=usuario, agencia="1234", n_conta="56789-0", saldo=0.0)

    limpar()

    cc.usuario.nome = input("Digite o nome do titular da conta: ").strip().title()
    cc.usuario.cpf = input("Digite o CPF do titular da conta: ").strip()

    limpar()

    while True:
        print("=== MENU ===")
        print("1. Consultar dados da conta")
        print("2. Gerar extrato")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        limpar()

        if opcao == "1":
            cc.consultar_dados()
        elif opcao == "2":
            cc.gerar_extrato()
        elif opcao == "3":
            valor = float(input("Digite o valor a ser depositado: "))
            print(cc.depositar(valor))
        elif opcao == "4":
            valor = float(input("Digite o valor a ser sacado: "))
            print(cc.sacar(valor))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()