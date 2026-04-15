# # Exercicio 90 - Aula 19

# ficha = {}
# ficha['Nome'] = str(input('Informe o nome do aluno: ').strip())
# ficha['Media'] = float(input(f'Informe a media de {ficha['Nome']}: '))
# if ficha['Media'] < 7:
#     ficha['Situação'] = 'Reprovado'
# else:
#     ficha['Situação'] = 'Aprovado'
# print('-='*20)
# print(f'Nome é igual a {ficha['Nome']}')
# print(f'Media é igual a {ficha['Media']}')
# print(f'Situação é igual a {ficha['Situação']}')

# # Exercicio 91 - Aula 19
# from random import randint
# from time import sleep
# from operator import itemgetter
# jogadores = {}
# for j in range(1, 5):
#     jogadores[f'Player {j}'] = randint(1, 6)
# ranking = []
# for k, v in jogadores.items():
#     print(f'O {k} tirou {v}')
#     sleep(1)
# ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# print('-='*15)
# for p, c in enumerate(ranking):
#     print(f'{p + 1}º Lugar: {c[0]} com {c[1]}')


# # Exercicio 92 - Aula 19
# from datetime import date
# ficha = dict()
# ficha['Nome'] = str(input('Nome: ').strip())
# ficha['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
# ficha['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
# if ficha['CTPS'] != 0:
#     ficha['Contratação'] = int(input('Ano de contratação: '))
#     ficha['Salario'] = float(input('Salário: '))
#     ficha['Aposentadoria'] = ficha['Contratação'] - (date.today().year - ficha['Idade']) + 35
# print('-='*30)
# for k, v in ficha.items():
#     print(f'{k} tem o valor {v}')


# # Exercicio 93 - Aula 19
# ficha = dict()
# gols = []
# ficha['Nome'] = str(input('Nome do Jogador: '))
# partidas = int(input(f'Quantas partidas {ficha['Nome']} jogou? '))
# for c in range(1, partidas + 1):
#     gols.append(int(input(f'Quantos Gols na partida {c}? ')))
# ficha['Gols'] = gols.copy()
# ficha['Total'] = sum(ficha['Gols'])
# print('-='*30)
# print(ficha)
# print('-='*30)
# for k, v in ficha.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-='*30)
# print(f'O jogador {ficha['Nome']} jogou {len(ficha['Gols'])} partidas.')
# for pos, c in enumerate(ficha['Gols']):
#     print(f'   => Na partida {pos + 1}, fez {c} gols.')
# print(f'Foi um total de {ficha['Total']} gols.')


# # Exercicio 94 - Aula 19
# dados = dict()
# pessoas = list()
# while True:
#     dados['Nome'] = str(input('Nome: ').strip())
#     dados['Sexo'] = str(input('Informe o sexo: [M/F] ').strip().upper())
#     dados['Idade'] = int(input('Idade: ').strip())
#     pessoas.append(dados.copy())
#     dados.clear
#     while True:
#         opção = str(input('Deseja adicionar mais pessoas: [S/N] ').strip().upper())
#         if opção in 'SsNn':
#             break
#     if opção in 'Nn':
#         break
# print('-='*30)
# print(f'O grupo tem {len(pessoas)} pessoas.')
# tot = 0
# mulheres = list()
# for c in pessoas:
#     tot += c['Idade']
#     if c['Sexo'] in 'Ff':
#         mulheres.append(c['Nome'])
# print(f'A media de idade é de {tot / len(pessoas):.2f} anos')
# print(f'As mulheres cadastradas foram: {mulheres}')
# print(f'Lista das pessoas que estão acima da media:')
# print()
# for c in pessoas:
#     if c['Idade'] > tot / len(pessoas):
#         print(c)
# print('<< ENCERRADO >>')


# # Exercicio 95 - Aula 19
jogadores = list()
ficha = dict()
gols = []
while True:
    gols.clear()
    ficha.clear()
    ficha['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {ficha['Nome']} jogou? '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos Gols na partida {c}? ')))
    ficha['Gols'] = gols.copy()
    ficha['Total'] = sum(ficha['Gols'])
    jogadores.append(ficha.copy())
    while True:
        opc = str(input('Quer continuar? [S/N] ').strip().upper()[0])
        if opc in 'SsNn':
            break
    if opc in 'Nn':
        break
print('-='*30)
print(f"{'Cod':<3} {'Nome':<15}{'Gols':<15}{'Total':<6}")
print('-'*40)
for pos, dic in enumerate(jogadores):
    print(f"{pos:>3} {dic['Nome']:<15}{str(dic['Gols']):<15}{dic['Total']:<6}")
print('-'*40)
while True:
    opt = int(input('Mostar dados de qual jogador [999 Sair]: ').strip())
    if opt == 999:
        break
    if opt >= len(jogadores) or opt < 0:
        print(f'ERRO! Não existe jogador com código {opt}! Tente novamente')
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[opt]['Nome']}:")
        for pos, c in enumerate(jogadores[opt]['Gols']):
            print(f'   => Na partida {pos + 1}, fez {c} gols.')
        print(f'Foi um total de {jogadores[opt]['Total']} gols.')
        print('-'*40)
        