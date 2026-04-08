# # Exercicio 72 - Aula 16
# numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
# num = int(input('Digite um numero emtre 0 e 20: '))
# while num < 0 or num > 20:
#     num = int(input('Tente novamente. Digite um numero emtre 0 e 20: '))
# print(numeros[num])


# # Exercicio 73 - Aula 16
# time = ('Palmeiras', 'São Paulo', 'Fluminense', 'Flamengo', 'Bahia', 'Athletico-PR', 'Coritiba', 'Atlético-MG', 'Bragantino', 'Botafogo', 'Grêmio', 'Vasco da Gama', 'Internacional', 'EC Vitória', 'Santos', 'Corinthians', 'Chapecoense', 'Remo', 'Cruzeiro', 'Mirassol')
# print(f'Os 5 primeiros colocados são:')
# for pos , c in enumerate(time[0:5]):
#     print(f'{pos + 1} colocado: {c}')
# print(f'Os 4 ultimos colocados são:')
# for c in time[-4:]:
#     print(f'{c}')
# print('Lista de times em ordem alfabetica:')
# print(sorted(time))
# for pos2, c2, in enumerate(time):
#     if c2 == 'Chapecoense':
#         print(f'O Chapecoense está na {pos2 + 1} posição')


# # Exercicio 74 - Aula 16
# from random import randint
# numeros = (randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999))
# print('Os numeros gerados foram:')
# print(numeros)
# maior = menor = 0
# for c in numeros:
#     if menor == 0 and maior == 0:
#         maior = c
#         menor = c
#     elif c > maior:
#         maior = c
#     elif c < menor:
#         menor = c
# print(f'''O maior numero foi: {maior}
# O menor numero foi: {menor}''')


# # Exercicio 75 - Aula 16
# numeros = (int(input('Digite o 1º numero: ')), 
#            int(input('Digite o 2º numero: ')), 
#            int(input('Digite o 3º numero: ')), 
#            int(input('Digite o 4º numero: ')))
# print(f'Voce digitou os valores: {numeros}')
# print(f'A quantidade de numeros 9 é de: {numeros.count(9)}')
# for pos, c in enumerate(numeros):
#     if c == 3:
#         print(f'O primeiro valor 3 apareceu na posição: {pos + 1}')
#         break
# if 3 not in numeros:
#     print('O valor 3 não foi digitado em nenhuma posição')
# print('Os numeros pares foram: ', end='')
# for c in numeros:
#     if c % 2 == 0:
#         print(c, end=' ')


# # Exercicio 76 - Aula 16
# materiais = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
#              'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 
#              'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
# print('-'*40)
# print(f"{'LISTAGEM DE PREÇOS': ^40}")
# print('-'*40)
# cont = len(materiais)
# for c in range(0, cont):
#     if c % 2 == 0:
#         print(f'{materiais[c]:.<31}R${materiais[c + 1]: >7.2f}')


# # Exercicio 77 - Aula 16
lista = ('aprender', 'programar', 'linguagem', 
         'python', 'curso', 'gratis', 'estudar', 
         'praticar', 'trabalhar', 'mercado', 
         'programador', 'futuro')
for palavra in lista:
    print(f'Na palavra {palavra.upper()} temos', end=' ')
    for letras in palavra:
        if letras in 'aeiou':
            print(letras, end=' ')
    print('')