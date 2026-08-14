# função com parâmetro
def boas_vindas(nome):
    print(f"Seja bem vindo, {nome}! 😎🐍")


# algoritmo principal
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)