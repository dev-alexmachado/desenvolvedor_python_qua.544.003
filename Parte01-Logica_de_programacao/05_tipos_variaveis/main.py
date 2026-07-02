# declaração de variáveis
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",","."))

# saída de dados
print(f"Seu nome é {nome}. {type(nome)}")
print(f"Sua idade é {idade}. {type(idade)}")
print(f"Sua altura é {altura} m. {type(altura)}")