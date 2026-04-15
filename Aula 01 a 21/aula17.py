# # Exercicio 78 - Aula 17
# numeros = []
# for c in range(0, 5):
#     numeros.append(int(input(f'Digite um valor para a Posição {c}: ')))
# print('-='*30)
# print(f'Voce digitou os valores: {numeros}')
# print(f'O maior numero foi {max(numeros)} e esta na posição ', end='')
# for pos, c in enumerate(numeros):
#     if max(numeros) == c:
#         print(pos, end='... ')
# print('')
# print(f'O menor numero foi {min(numeros)} e esta na posição ', end='')
# for pos, c in enumerate(numeros):
#     if min(numeros) == c:
#         print(pos, end='... ')


# # Exercicio 79 - Aula 17
# numeros = []
# opção = 'S'
# while opção == 'S':
#     num = int(input('Digite um numero que deseja adicionar: '))
#     if num not in numeros:
#         numeros.append(num)
#         print('Valor adicionado com sucesso...')
#     else:
#         print('Valor duplicado. Não vou adicionar')
#     while True:
#         opção = str(input('Deseja adicionar mais numeros? [S/N]: ').upper().strip()[0])
#         if opção in 'SsNn':
#             break
# numeros.sort()
# print(numeros)


# # Exercicio 80 - Aula 17
# numeros = []
# for c in range(0, 4):
#     if c == 0:
#         numeros.append(int(input('Digite um numero: ').strip()))
#     pos = 0
#     num = int(input('Digite mais um numero: ').strip())
#     for c in numeros:
#         if num > c:
#             pos += 1
#     numeros.insert(pos, num)
# print(numeros)


# # Exercicio 81 - Aula 17
# numeros = []
# opcao = 'S'
# while opcao in 'Ss':
#     numeros.append(int(input('Digite um numero: ').strip()))
#     while True:
#         opcao = str(input('Deseja adicionar mais? [S/N]: ').strip().upper()[0])
#         if opcao in 'SsNn':
#             break
# print('-='*30)
# print(f'Voce digitou {len(numeros)} elementos')
# numeros.sort(reverse = True)
# print('Os valores em ordem decrescente são:', numeros)
# if 5 in numeros:
#     print(f'O valor 5 faz parte da lista! e esta na poscisão {numeros.index(5)}')
# else:
#     print('O valor 5 não faz parte da lista!')


# # Exercicio 82 - Aula 17
# numeros = []
# pares = []
# impares = []
# opcao = 'S'
# while opcao in 'Ss':
#     numeros.append(int(input('Digite o numero que deseja adicionar: ').strip()))
#     while True:
#         opcao = str(input('Deseja adicionar mais? [S/N]: ').strip().upper()[0])
#         if opcao in 'SsNn':
#             break
# for c in numeros:
#     if c % 2 == 0:
#         pares.append(c)
#     else:
#         impares.append(c)
# print('Os numeros digitados foram:', numeros)
# print('Os numeros pares são:', pares)
# print('Os numeros impares são: ', impares)


# # Exercicio 82 - Aula 17 / Que eu fiz = Gambiarra funcional
# espressao = str(input('Digite a expressão: ')).replace(' ', '')
# lista = list(espressao)
# abre = []
# fecha = []
# validador = 'True'
# if '(' and ')' in lista:
#     openpa = lista.count('(')
#     closepa = lista.count(')')
#     if openpa != closepa:
#         print('A expresão é invalida')
#         validador = 'False'
#     else:
#         for pos, c in enumerate(lista):
#             if c == '(':
#                 abre.append(pos)
#             elif c == ')':
#                 fecha.append(pos)
#         for pos2, c2 in enumerate(fecha):
#             if c2 < abre[pos2]:
#                 print('A expresão é invalida')
#                 validador = 'False'
#                 break
#         if validador == 'True':
#             print('A expresão é valida')
# elif '(' in lista and ')' not in lista:
#     print('A expresão é invalida')
# elif ')' in lista and '(' not in lista:
#     print('A expresão é invalida')
# elif ')' and '()' not in lista:
#     print('A expressão digitada não tem parenteses')


# # Exercicio 82 - Aula 17 / soluçao do gemini, simplificada
# expressao = input('Digite a expressão: ')
# pilha = []
# valida = True

# for caractere in expressao:
#     if caractere == '(':
#         pilha.append('(')
#     elif caractere == ')':
#         if len(pilha) > 0:
#             pilha.pop()  # Remove o parêntese que foi aberto
#         else:
#             valida = False  # Encontrou um ")" sem ter um "(" aberto
#             break

# # Se a pilha não estiver vazia no final, faltou fechar algum parêntese
# if valida and len(pilha) == 0:
#     print('A expressão é válida')
# else:
#     print('A expressão é inválida')
