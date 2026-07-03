# tratamento de exceção
try:
    # usuário informa número inteiro
    n = int(input("Informe um número inteiro: "))

    # laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except:
    print("Não foi possível exibir a contagem.")