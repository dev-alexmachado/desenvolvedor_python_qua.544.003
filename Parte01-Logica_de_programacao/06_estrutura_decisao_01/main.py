# declaração de variáveis
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

# estrutura de decisão
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")