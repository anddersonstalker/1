# # Exercicio 96 - Aula 20
# def área(a, b):
#     area = a * b
#     print(f'A área de um terreno {a:.1f}x{b:.1f} é de {area:.1f}m². ')


# print('Controle de Terrenos')
# print('-'*20)
# área(float(input('LARGURA (m): ')), 
#      float(input('COMPRIMENTO (M): ')))


# # Exercicio 97 - Aula 20
# def escreva(a):
#     b = len(a)+4
#     print('-'*b)
#     print(f'{a:^{b}}')
#     print('-'*b)


# frase = 'Curso de Python no youtube'
# escreva(frase)


# # Exercicio 98 - Aula 20
# from time import sleep
# def contador(a, b, c):
#     if c == 0:
#         c = 1
#     if c < 0:
#         c*= -1
#     print('-='*20)
#     print(f'Contagem de {a} até {b} de {c} em {c}')
#     if a > b:
#         for c in range(a, b-1, c*-1):
#             print(c, end=' ', flush=True)
#             sleep(0.5)
#     else:
#         for c in range(a, b+1, c):
#             print(c, end=' ', flush=True)
#             sleep(0.5)
#     print('FIM!')


# contador(1, 10, 1)
# contador(10, 1, -2)
# print('Agora é sua vez de personalizar a contagem!')
# contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))


# # Exercicio 99 - Aula 20
# from time import sleep
# def maior(* num):
#     print('-='*20)
#     print('Analisando so valores passados...')
#     sleep(1)
#     for c in num:
#         print(c, end=' ')
#     print(f'Foram informados {len(num)} valores ao todo.')
#     if num == ():
#         print(f'O maior valor informado foi 0')
#     else:
#         print(f'O maior valor informado foi {max(num)}')


# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()


# # Exercicio 100 - Aula 20
# from random import randint
# from time import sleep


# def sorteia(lista):
#     print('Sorteando 5 valores da lista:', end=' ')
#     for c in range(0,5):
#         lista.append(randint(0, 999))
#         print(lista[c], end=' ', flush=True)
#         sleep(0.5)
#     print('PRONTO!')


# def somaPar(lista):
#     tot = 0
#     for c in lista:
#         if c % 2 ==0:
#             tot += c
#     print(f'Somando os valores pares de {lista}, temos {tot}')


# numeros = list()
# sorteia(numeros)
# somaPar(numeros)
