# importação de biblioteca
import math

# tratamento de exceção
try:
    while True:
        # usuário informa valor do raio
        r = float(input("Informe o valor do raio em m²: ").replace(",","."))

        # calcula a área do círculo
        area = math.pi*r**2

        # imprime na tela a área do círculo
        print(f"Área do círculo: {area:.2f} m².")

        # usuário informa se deseja continuar ou não
        print("1 - Calcular área de outro círculo")
        print("2 - Sair do programa")

        opcao = input("Informe sua opção: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção inválida.")
                continue
except Exception as e:
    print(f"Não foi possível calcular. {e}.")