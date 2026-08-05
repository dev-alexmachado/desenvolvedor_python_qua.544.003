cidades = [
    "Brasília",
    "Rio de Janeiro",
    "São Paulo",
    "Belo Horizonte",
    "Goiânia",
    "Manaus",
    "Fortaleza",
    "Florianópolis"
]

cidade = input("Informe a cidade a ser pesquisada: ").strip().title()

# mostra a posição do item na lista
if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"Índice de {cidade} na lista é {indice}.")
else:
    print("Cidade não encontrada.")