usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# adiciona a chave telefone ao dicionário
usuario['telefone'] = input(f"Informe o telefone de {usuario.get('nome')}: ").strip()

# exibe o dicionário
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")