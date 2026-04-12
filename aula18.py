# # Exercício Python 84
# pessoas = []
# dados = []
# opcao = 'S'
# maior = menor = 0
# while opcao == 'S':
#     dados.append(str(input('Nome: ')))
#     dados.append(float(input('Peso: ')))
#     if pessoas == []:
#         maior = menor = dados[1]
#     else:
#         if dados[1] > maior:
#             maior = dados[1]
#         elif dados[1] < menor:
#             menor = dados[1]
#     pessoas.append(dados[:])
#     dados.clear()
#     while True:
#         opcao = str(input('Quer continuar? [S/N] ').strip().upper())
#         if opcao in 'SsNn':
#             break
# print('-='*40)
# print(f'Ao todo voce cadastrou {len(pessoas)} pessoas.')
# print(f'O maior peso foi de {maior}Kg. Peso de:', end=' ')
# for pos, c in enumerate(pessoas):
#     if maior in c:
#         print(f'[{pessoas[pos][0]}]', end=' ')
# print('')
# print(f'O menor peso foi de {menor}Kg. Peso de: ', end='')
# for pos, c in enumerate(pessoas):
#     if menor in c:
#         print(f'[{pessoas[pos][0]}]', end=' ')
# print('')


# # Exercício Python 85
# lista = [[], []]
# for n in range(1, 8):
#     num = int(input(f'Digite o {n} numero: '))
#     lista[num % 2].append(num)
# print(f'Os numeros pares são: {sorted(lista[0])}')
# print(f'Os numeros impares são: {sorted(lista[1])}')


# # Exercício Python 86
# lista = [[], [], []]
# for c in range(0, 3):
#     for n in range(0, 3):
#         lista[c].append(int(input(f'Digite um falor para [{c}, {n}]: ')))
# for c in range(0, 3):
#     for n in lista[c]:
#         print(f'[{n:^5}]', end='')
#     print()


# # Exercício Python 87
# lista = [[], [], []]
# totpares = 0
# for c in range(0, 3):
#     for n in range(0, 3):
#         lista[c].append(int(input(f'Digite um falor para [{c}, {n}]: ')))
# print('-='*20)
# for c in range(0, 3):
#     for n in lista[c]:
#         print(f'[{n:^5}]', end='')
#         if n % 2 == 0:
#             totpares += n
#     print()
# print('-='*20)
# print(f'A soma dos numeros pares é: {totpares}')
# print(f'A soma dos valores da terceira coluna é: {lista[0][2] + lista[1][2] + lista[2][2]}')
# maior = lista[1]
# print(f'O maior valor da segunda linha é {max(maior)}')


# from random import randint
# from time import sleep
# jogos = [[]]
# pos = 0
# opcao = int(input('Digite quantos jogos deseja gerar: '))
# while pos < opcao:
#     if len(jogos[pos]) < 6:
#         num = randint(1, 60)
#         if num not in jogos[pos]:
#             jogos[pos].append(num)
#     if len(jogos[pos]) == 6:
#         if pos < opcao - 1:
#             pos += 1
#             jogos.append([])
#         else:
#             pos += 1
# for c in range(0, opcao):
#     print(f'Jogo {c + 1}: {sorted(jogos[c])}')
#     sleep(1)


# ficha = list()
# while True:
#     nome = str(input('Nome:'))
#     notal = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [notal, nota2], media])
#     resp = str(input('Quer continuar? [S/N]'))
#     if resp in 'Nn':
#         break
# print('=' * 30)
# print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
# print('-'* 26)
# for i, a in enumerate (ficha):
#     print(f'{i:<4}{a[0]: <10}{a[2]:>8.1f}')
# while True:
#     print('-'*35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) -1:
#         print(f'Notas de {ficha [opc] [0]} são {ficha [opc] [1]}')
# print('<<< VOLTE SEMPRE >>>')
