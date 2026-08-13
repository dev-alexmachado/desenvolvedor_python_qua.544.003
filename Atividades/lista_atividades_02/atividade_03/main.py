import os
import json

alunos = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Informa dados")
    print("2 - Sair do programa")
    opcao = input("Informe a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            aluno = {}
            notas = [0,0,0]
            aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
            for i in range(len(notas)):
                notas[i] = float(input(f"Informe a {i+1}ª nota: ").replace(",","."))
            aluno['notas'] = notas
            aluno['média'] = sum(notas)/len(notas)
            aluno['resultado'] = "aprovado" if aluno['média'] >= 7 else "reprovado"
            alunos.append(aluno)

            # FIXME: verifique o encoding
            with open("atividade_03/arquivo.json","w",encoding="utf-8") as f:
                json.dump(alunos, f)
            print("Dados do aluno gravados com sucesso!")
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")
            continue

# TODO: atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# O programa deve calcular a média do aluno e informar se
# o aluno está aprovado (média mínima = 7) ou reprovado.
# O programa deve gravar esses dados em um JSON.
# Ao final, o usuário deverá escolher se deseja inserir as
# notas de outro aluno, que deverão ser gravadas no mesmo
# arquivo JSON.