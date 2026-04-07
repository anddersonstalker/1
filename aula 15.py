# # Exercicio 66 - Aula 15
# c = a = 0
# while True:
#     n = int(input('Digite um numero: '))
#     if n == 999:
#         break
#     c += 1
#     a += n
# print(f'A quantidade de numeros digitados foi: {c}, e a soma desses numeros é igual a: {a}')


# # Exercicio 67 - Aula 15
# while True:
#     n = int(input('Quer ver a Tabuada de qual valor: '))
#     if n <= 0:
#         break
#     c = 1
#     while c < 11:
#         print(f'{n} x {c} = {n * c}')
#         c += 1
# print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


# # Exercicio 68 - Aula 15
# from random import randint
# print('-='*20)
# print('Vamos jogar PAR ou IMPAR')
# print('-='*20)
# c = 0
# while True:
#     j1 = int(input('Digite o valor: '))
#     opcao = str(input('PAR ou IMPAR? [P/I] ').upper().strip()[0])
#     print('-='*20)
#     pc = randint(1, 10)
#     total = pc + j1
#     if total % 2 == 0:
#         print(f'Voce jogou {j1} e o computador {pc}. total de {total} DEU PAR!')
#     else:
#         print(f'Voce jogou {j1} e o computador {pc}. total de {total} DEU IMPAR!')
#     print('-='*20)
#     if opcao in 'Pp' and total % 2 == 0:
#         print('Voce VENCEU! \nVamos jogar Novamente...')
#         c += 1
#     elif opcao in 'Ii' and (total) % 2 !=0:
#         print('Voce VENCEU! \nVamos jogar Novamente...')
#         c += 1
#     elif opcao in 'Pp' and total % 2 != 0:
#         print('Voce PERDEU!')
#         break
#     elif opcao in 'Ii' and (total) % 2 ==0:
#         print('Voce PERDEU!')
#         break
#     print('-='*20)
# print(f'GAME OVER! Voce venceu {c} vezes.')


# # Exercicio 69 - Aula 15
# p = 1
# c = h = m = mais18 = 0
# while True:
#     idade = int(input(f'Digite a idade da {p}ª pessoa: '))
#     if idade > 18:
#         mais18 += 1
#     sexo = ' '
#     while sexo not in 'FfMm':
#         sexo = str(input(f'Informe o sexo da {p}ª pessoa: [F/M] ').upper().strip()[0])
#     if sexo in 'Mm':
#         h += 1
#     elif sexo in 'Ff' and idade < 20:
#         m += 1
#     c += 1
#     p += 1
#     opcao = ' '
#     while opcao not in 'SsNn':
#         opcao = str(input('Deseja informar mais alguma pessoa: [S/N] ').upper().strip()[0])
#     if opcao in 'Nn':
#         print('-='*20)
#         break
#     print('-='*20)
# print(f'''Foram adicionadas {c} pessoas.
# Dessas {c} pessoas {h} são Homens.
# Dessas {c} pessoas {m} são mulheres com menos de 20 anos.
# Dessas {c} pessoas {mais18} tem mais de 18 anos.''')


# # Exercicio 70 - Aula 15
# c_prod = a = mil = preco_barato = 0
# while True:
#     nome_prod = str(input(f'Digite o nome do {c_prod}º produto: ' ).title().strip())
#     preco_prod = float(input(f'Digite o preço do {c_prod}º produto: ').strip())
#     c_prod += 1
#     a += preco_prod
#     if c_prod == 1 or preco_barato > preco_prod:
#         nome_barato = nome_prod
#         preco_barato = preco_prod
#     if preco_prod > 1000:
#         mil += 1
#     opcao = ' '
#     while opcao not in 'SsNn':
#         opcao = str(input('Deseja adcionar mais produtos: [S/N] ').upper().strip()[0])
#     if opcao in 'Nn':
#         print('-='*20)
#         break
#     print('-='*20)
# print(f'''O Valor total da compra foi de R${a:.2f}
# Tinham {mil} produtos com valor acima de R$1000.00
# O produto mais barato foi: {nome_barato} e custou R${preco_barato:.2f}''')


# # Exercicio 71 - Aula 15 / while true
# n = int(input('DIGITE O VALOR QUE GOSTARIA DE SACAR: '))
# cedulas = [50, 20, 10, 1]
# c = 0
# while True:
#     if n // cedulas[c] != 0:
#         print(f'Voce sacou {n // cedulas[c]} cedula de R${cedulas[c]}' if n // cedulas[c] == 1 
#             else f'Voce sacou {n // cedulas[c]} cedulas de R${cedulas[c]}')
#         n = n % cedulas[c]
#     c += 1
#     if c >= 4:
#         break


# # Exercicio 71 - Aula 15 / for
# n = int(input('DIGITE O VALOR QUE GOSTARIA DE SACAR: '))
# cedulas = [50, 20, 10, 1]
# for c in cedulas:
#     if n // c != 0:
#         print(f'Voce sacou {n // c} cedula de R${c}' if n // c == 1 
#             else f'Voce sacou {n // c} cedulas de R${c}')
#         n = n % c
