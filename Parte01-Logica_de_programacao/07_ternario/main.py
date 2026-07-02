# declaração de variáveis
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

# saída de dados com operador ternário
print(f"{nome} é maior de idade." if idade >= 18 else f"{nome} é menor de idade.")