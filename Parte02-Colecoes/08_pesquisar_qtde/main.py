paises = [
    "Brasil",
    "Estados Unidos",
    "México",
    "Argentina",
    "Brasil",
    "Argentina",
    "Arábia Saudita",
    "Irã",
    "Brasil",
    "México",
    "Estados Unidos",
    "Brasil"
]

pais = input("Informe o país a ser pesquisado: ").strip().title()

# armazena a quantidade de ocorrências na lista
qtde = paises.count(pais)

print(f"{pais} foi encontrado {qtde} vezes na lista.")