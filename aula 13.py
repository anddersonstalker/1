# #Exercicio 46 - Aula 13
# from time import sleep
# import emoji
# print('-='*27)
# print('Contagem regressiva para o ano novo:')
# print('-='*27)
# for contagem in range(10, 0, -1):
#     print(contagem)
#     sleep(1)
# print(emoji.emojize(':fireworks: FELIZ ANO NOVO :fireworks:'))


# #Exercicio 47 - Aula 13
# print('-='*27)
# print('vamso ver todos os numeros pares entre 1 e 50')
# print('-='*27)
# for contagem in range(1, 51, 2):
#     print(contagem + 1)


# #Exercicio 48 - Aula 13
# print('-='*40)
# print('Vamos somar todos os numeros impares multiplos de 3 entre 1 e 500')
# print('-='*40)
# s = 0
# for impares in range(1, 501, 2):
#     if impares % 3 == 0:
#         s += impares
# print(f'A soma dos numeros impares multiplos de 3 entre 1 e 500 é de {s}')


# # Solução mais inteligente 1
# soma_impares = sum(i for i in range(1, 501) if i % 3 == 0 and i % 2 != 0)
# print(f"A soma dos ímpares múltiplos de 3 é: {soma_impares}")


# # Solução mais inteligente 2
# soma_impares = sum(range(3, 501, 6))
# print(f"A soma dos ímpares múltiplos de 3 é: {soma_impares}")


# #Exercicio 49 - Aula 13
# print('-='*27)
# print('Vamos consultar as tabuada de um numero')
# print('-='*27)
# n = int(input('Digite o numero que deseja consultar a tabuada: '))
# for multi in range(1, 11):
#     print(f'{n} x {multi} = {n * multi}')


# #Exercicio 50 - Aula 13
# print('-='*15)
# print('Vamos somar 6 numeros pares')
# print('-='*15)
# s = 0
# for numeros in range(0, 6):
#     n = int(input('Digite um numero PAR: '))
#     s += n
# if s % 2 != 0:
#     print('ALGUM DOS NUMEROS DIGITADOS NÃO É PAR')
# else:
#     print(f'A soma dos numeros pares é {s}')


# #Exercicio 51 - Aula 13
# print('Digite o 1º Termo e a Razão de uma PA \npara verificar seus 10 primeiros termos')
# termo1 = int(input('Digite o valor do primeiro termo: '))
# razao = int(input('Digite o valor da Razão: '))
# print(termo1)
# for pa in range(1, 10):
#     termo1 += razao
#     print(termo1)


# #Exercicio 52 - Aula 13
# print('-='*20)
# print('Vamos verificar se um numero é primo: ')
# print('-='*20)
# num = input('Digite o Numero que deseja verificar: ').strip()
# numint = int(num)
# print('-='*20)
# check = 'true'
# if numint == 1:
#     print('''O número 1 não é primo porque 
# a definição de número primo exige 
# que ele tenha exatamente dois divisores 
# distintos: o número 1 e ele mesmo. 
# O número 1 possui apenas um divisor 
# (ele mesmo), falhando nessa regra.''')
# else:
#     for verifica in range(2, numint):
#         if numint % verifica == 0:
#             check = 'false'
#     if check == 'false':
#         print('O numero não é primo')
#     else:
#         print('O numero é primo')


# #Exercicio 53 - Aula 13
# from unidecode import unidecode
# frase = str(input('Digite a frase: ')).strip().upper().replace(' ', '')
# frase_limpa = unidecode(frase)
# frase_invertida = ''
# for letra in frase_limpa:
#     frase_invertida = letra + frase_invertida
# if frase_invertida == frase_limpa:
#     print('A frase é um Palíndromo')
# else:
#     print('A frase não é um Palíndromo')


# # OUTRA FORMA DE FAZER / tinha a forma com split e join mais deletei
# from unidecode import unidecode
# frase = str(input('Digite a frase: ')).strip().upper().replace(' ', '')
# frase_limpa = unidecode(frase)
# tamanho = len(frase_limpa)
# frase_invertida = ''
# for teste in range(tamanho -1, -1, -1):
#     frase_invertida += frase_limpa[teste]
# if frase_invertida == frase_limpa:
#     print('A frase é um Palíndromo')
# else:
#     print('A frase não é um Palíndromo')


# #Exercicio 54 - Aula 13
# from datetime import date
# maiores = 0
# menores = 0
# data = date.today().year
# for loop in range(7):
#     nasc = input('Digite o ano de nascimento: ')
#     idade = int(data) - int(nasc)
#     if idade < 18:
#         menores += 1
#     else:
#         maiores += 1
# print(f'A quantidade de maiores de idade é de {maiores} pessoas')
# print(f'A quantidade de menores de idade é de {menores} pessoas')


# #Exercicio 55 - Aula 13
# maior = float(0)
# menor = float(0)
# for pessoas in range(5):
#     peso = float(input('Digite o peso da pessoa: '))
#     if menor == 0:
#         menor = peso
#     elif peso > maior:
#         maior = peso
#     elif peso < menor:
#         menor = peso
# print(f'O maior peso registrado foi de {maior} KG')
# print(f'O menor peso registrado foi de {menor} KG')


# #Exercicio 56 - Aula 13
# print('-='*30)
# print('''Vamos calcular a media de idade de um gruppo de pessoas
# Verificar o nome e idade do Homem mais velho
# E verificar quantas mulheres do grupo tem menos de 20 anos''')
# print('-='*30)
# idade_total = 0
# velho_idade = 0
# velho_nome = ''
# mulheres_20 = 0
# for pessoas in range(4):
#     nome = str(input('Digite o nome da pessoa: ')).strip().upper()
#     idade = int(input('Digite a idade da pessoa: '))
#     print('ESCOLHA O GENERO DA PESSOA: \n[1] MASCULINO \n[2] FEMININO')
#     sexo = int(input('Opção escolhida: '))
#     idade_total += idade
#     if sexo == 1 and velho_idade == 0:
#         velho_idade = idade
#         velho_nome = nome
#     elif sexo == 1 and velho_idade < idade:
#         velho_idade = idade
#         velho_nome = nome
#     elif sexo == 2 and idade < 20:
#         mulheres_20 += 1
#     print('-='*30)
# print(f'A media de idade desse grupo de pessoas é de {idade_total / 4}')
# print(f'O nome do homem mais velho do grupo é {velho_nome} e ele tem {velho_idade} anos')
# print(f'A quantidade de mulheres com menos de 20 anos é de {mulheres_20}')
# print('-='*30)
        
