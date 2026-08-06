nomes = ["Fulano","Cicrano","Beltrano","João","Maria","José"]
nome = input("Informe o nome a ser separado: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)

    # separar o nome da lista
    nome_separado = nomes.pop(indice)

    # exibe lista
    for nome in nomes:
        print(nome)
    print(f"Nome separado da lista: {nome_separado}.")
else:
    print("Nome não encontrado.")