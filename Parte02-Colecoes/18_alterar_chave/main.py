usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# usuário informa a chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()

# verifica se a chave existe
if chave in usuario:
    # usuário informa o novo valor para a chave
    novo_valor = input(f"Informe o novo valor para '{chave}': ").strip()
    # altera o valor da chave
    usuario[chave] = novo_valor
    print(f"Chave '{chave}' alterada com sucesso!")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print(f"Chave '{chave}' não encontrada.")