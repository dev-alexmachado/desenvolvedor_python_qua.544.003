# importa biblioteca os
import os

# limpa tela do terminal
os.system("cls" if os.name == "nt" else "clear")

# entrada de dados
nome = input("Digite seu nome: ").strip()
peso = float(input("Digite seu peso (em kg): ").replace(",", "."))
altura = float(input("Digite sua altura (em metros): ").replace(",", "."))

# calcula o IMC
imc = peso/(altura**2)

os.system("cls" if os.name == "nt" else "clear")

# informa o IMC na tela
print(f"Olá {nome}, seu IMC é: {imc:.2f}")

# verifica o valor do IMC e informa o diagnóstico
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade grau I.")
elif imc < 40:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade mórbida.")

# TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário, e informe na tela o seu IMC o seu diagnóstico com base no valor do IMC.
"""
# NOTE: imc = peso/(altura**2)
