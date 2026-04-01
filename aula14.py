# # Exercicio 57 - Aula 14
# nome = str(input('Digite seu nome: ')).strip().title()
# idade = int(input('Digite a sua idade: ').strip())
# sexo = str(input('Informe seu sexo [M/F]: ').strip())
# while sexo not in 'MmFf':
#     print('Opção escolhida invalida, tente novamente!')
#     sexo = str(input('Informe seu sexo [M/F]: ').strip())
# print(nome)
# print(idade)
# print(sexo)


# # Exercicio 58 - Aula 14
# from random import randint
# pc = randint(0, 10)
# tentativas = 1
# player = int(input('Escolha um numero: ').strip())
# while player < 0 or player > 10:
#     player = int(input('Valor digitado invalidao, digite novamente: '))
# while player != pc:
#     tentativas += 1
#     player = int(input('Voce errou, tente novamente: ').strip())
#     while player < 0 or player > 10:
#         player = int(input('Valor digitado invalidao, digite novamente: ').strip())
# print(f'Voce acertou, o numero que escolhi foi {pc}, e voce precisou de {tentativas} tentativas validas para adivinhar.')


# # Exercicio 59 - Aula 14
# n1 = int(input('Digite o primeiro valor: ').strip())
# n2 = int(input('Digite o segundo valor valor: ').strip())
# menu = '0'
# while menu == '0':
#     print('''ESCOLHA O QUE DESEJA FAZER COM ESSES NUMEROS:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NUMEROS
# [5] SAIR''')
#     menu = str(input('Opção escolhida: ').strip())
#     while menu not in '12345':
#         menu = str(input('Opçao selecionada invalida, tente novamente: ').strip())
#     if menu == '1':
#         print(f'A soma de {n1} + {n2} é: {n1 + n2} ')
#     elif menu == '2':
#         print(f'A multiplicaçao de {n1} por {n2} é: {n1 * n2} ')
#     elif menu == '3' and n1 > n2:
#         print(f'O primeiro numero é o maior: {n1}')
#     elif menu == '3' and n2 > n1:
#         print(f'O segundo numero é o maior: {n2}')
#     elif menu == '4':
#         n1 = int(input('Digite o primeiro valor: ').strip())
#         n2 = int(input('Digite o segundo valor valor: ').strip())
#         menu = '0'


# # Exercicio 60 - Aula 14
# n = int(input('Digite um numero para verificar o seu fatorial: ').strip())
# f = n - 1
# a = 0
# print(f'{n}!={n}', end='x')
# while f != 0:
#     if f == n - 1:
#         a = f * n
#         print(f, end='x')
#         f -= 1
#     elif f == 1:
#         a = f * a 
#         print(f, end='')
#         f -= 1
#     else:
#         a = f * a 
#         print(f, end='x')
#         f -= 1
# print(f'={a}')


# n = int(input('Digite um numero para verificar o seu fatorial: ').strip())
# f = n - 1
# a = 0
# print(f'{n}!={n}', end='x')
# for c in range(n - 1, 0, -1):
#     if c == n - 1:
#         a = c * n
#         print(c, end='x')
#     elif c == 1:
#         a = c * a 
#         print(c, end='')
#     else:
#         a = c * a 
#         print(c, end='x')
# print(f'={a}')


# # Exercicio 61 - Aula 14
# termo1 = int(input('Digite o primeiro termo da PA: '))
# razão = int(input('Digite a razão da PA: '))
# a = termo1
# contador = 9
# print(f'Os 10 primeiros digitos dessa PA é: {termo1}', end='-> ')
# while contador != 0:
#     if contador == 1:
#         a += razão
#         contador -= 1
#         print(a, end='')
#     else:
#         a += razão
#         contador -= 1
#         print(a, end='-> ')



# # Exercicio 62 - Aula 14
# termo1 = int(input('Digite o primeiro termo da PA: '))
# razão = int(input('Digite a razão da PA: '))
# a = termo1
# contador = 9
# opção = 'S'
# print(f'Os 10 primeiros digitos dessa PA é: {termo1}', end='-> ')
# while opção == 'S':
#     while contador != 0:
#         if contador == 1:
#             a += razão
#             contador -= 1
#             print(a, end='')
#         else:
#             a += razão
#             contador -= 1
#             print(a, end='-> ')
#     if contador == 0:
#         print('\nDeseja verificar mais digitos da PA? \n[S] Sim \n[N] Não')
#         opção = input('Opção desejada: ').upper().strip()
#         while opção not in 'SN':
#             opção = input('A opção selecionada é invalida. \nDigite novamente a opção desejada: ').upper().strip()
#         if opção == 'S':
#             contador = int(input('Digite quantas a mais deseja verificar: ').strip())
#             print(f'Os {contador} proximos termos são:', end=' ')


# # Exercicio 63 - Aula 14
# limite = int(input('Digite quantos termos da sequencia de Fibonacci deseja vizualizar: '))
# anterior = 0
# proximo = 1
# contador = 0
# while limite <= 0:
#       limite = int(input("Por favor, digite um número inteiro positivo maior que zero: "))
# while contador < limite:
#         print(anterior, end=' ')
#         prov = anterior
#         proximo += anterior
#         anterior = proximo - prov
#         contador += 1


# # Exercicio 64 - Aula 14
# n = int(input('Digite um numero que gostaria de somar \nOu digite 999 para interromper: ').strip())
# a = 0
# c = 0
# while n != 999:
#     a += n
#     c += 1
#     print('-='*20)
#     n = int(input('Digite um numero que gostaria de somar \nOu digite 999 para interromper: ').strip())
# print('-='*20)
# print(f'Voce digitou {c} numeros e a soma deles é {a}')


# # Exercicio 65 - Aula 14
# a = 0
# c = 0
# menor = 0
# maior = 0
# opcao = 'S'
# while opcao == 'S':
#     n = int(input('Digite um numero para adcionar ao grupo: ').strip())
#     a += n
#     c += 1
#     if c == 1:
#         menor = n
#         maior = n
#     elif n > maior:
#         maior = n
#     elif menor > n:
#         menor = n
#     opcao = input('Digite [S] para continuar ou [N] para parar: ').upper().strip()
#     while opcao not in 'SN':
#         opcao = input('Opção invalida, digite [S] para continuar ou [N] para parar: ').upper().strip()
#     print('-='*20) 
# print(f'''Voce adcionou {c} numeros ao grupo.
# A soma desses numeros é: {a}
# A media desse grupo de numeros é: {a / c}
# O menor numero é: {menor}
# O Maior numero é: {maior}''')