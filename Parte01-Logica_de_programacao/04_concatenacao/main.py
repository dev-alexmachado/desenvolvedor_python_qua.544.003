# declaração de variáveis
nome = input("Informe seu nome: ")
telefone = input("Informe seu telefone: ")

# saída de dados
print("Olá ", nome, ", e meu telefone é ", telefone, ".")
print("Olá " + nome + ", e meu telefone é " + telefone + ".")
print("Olá {}, e meu telefone é {}.".format(nome, telefone))
print(f"Olá {nome}, e meu telefone é {telefone}.")