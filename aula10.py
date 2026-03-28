#Desafio 28
# from random import randint
# n= randint(1,5)
# print('Tente adivinhar o numero que estou pensando entre 1 e 5')
# nu= int(input('Digite o numero que voce acha que é: '))
# if nu==n:
#     print('Parabens voce acertou!')
# else:
#     print(f'Voce errou! O numero que eu pensei foi: {n}')

# print('Parabens voce acertol!' if nu == n else f'Você errou o numero correto era: {n}')


#Desafio 29
# v=int(input('Digite a velocidade do veiculo: '))
# if v > 80:
#     print(f'Voce foi multado, por exceder o limite de velocidade da via! \nO valor da sua multa é de R${(v-80)*7:.2f}')
# else:
#     print('Parabens voce esta dentro do limite de velocidade da via!')


#Desafio 30
# print('Vamos verificar se um numero é par ou impar!')
# n= int(input('Digite o numero que deseja verificar: '))
# if n%2 == 0:
#     print(f'O numero {n} é par!')
# else:
#     print(f'O numero {n} é impar!')


#Desafio 31
# print('Vamos verificar o valor das passagens de acordo com a distancia da viagem!')
# km= float(input('Digite o valor da distancia da viagem em km: '))
# if km <= 200:
#     print(f'O valor da passagem é de R${km * 0.50:.2f}')
# else:
#     print(f'O valor da passagem é de R${km * 0.45:.2f}')


#Desafio 32
# print('Vamos verificar se um ano é bissexto ou não!')
# ano= int(input('Digite o ano que deseja verificar: '))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f'O ano de {ano} é bissexto!')
# else:
#     print(f'O ano de {ano} não é bissexto!')


#Desafio 33
# print('Vamos verificar qual é o maior e o menor numero entre 3 numeros!')
# n1= float(input('Digite o primeiro numero: '))
# n2= float(input('Digite o segundo numero: '))
# n3= float(input('Digite o terceiro numero: '))
# if n1 > n2 and n1 > n3:
#     print(f'O numero {n1} é o maior!')
# if n2 > n1 and n2 > n3:
#     print(f'O numero {n2} é o maior!')
# if n3 > n1 and n3 > n2:
#     print(f'O numero {n3} é o maior!')


#Desafio 34
# print('Vamos calcular o aumento salarial de um funcionario!')
# salario= float(input('Digite o salario do funcionario: R$'))
# if salario > 1250:
#     print(f'O salario do funcionario com aumento de 10% é de R${salario + (salario * 0.10):.2f}')
# else:
#     print(f'O salario do funcionario com aumento de 15% é de R${salario + (salario * 0.15):.2f}')


#Desafio 35
# print('Vamos verificar se as 3 retas formam um triangulo!')
# a= float(input('Digite o valor da primeira reta: '))
# b= float(input('Digite o valor da segunda reta: '))
# c= float(input('Digite o valor da terceira reta: '))
# if a + b > c and a + c > b and b + c > a:
#     print('As retas formam um triangulo!')
# else:
#     print('As retas não formam um triangulo!')