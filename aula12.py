#Exercicio 36 - Aula 12
# print('Vamos verificar a possibilidade de um emprestimo! e o valor da prestação!')
# valor_casa = float(input('Digite o valor da casa: R$'))
# salario = float(input('Digite o valor do seu salario mensal: R$'))
# anos = int(input('Digite em quantos anos quer pagar o financiamento: '))
# valor_prestacao = valor_casa / (anos * 12)
# if valor_prestacao < salario * 0.3:
#     print('Emprestimo aprovado!')
#     print(f'O valor das prestações é de R${valor_prestacao:.2f}')
# else:
#     print('Emprestimo negado!')
#     print(f'O valor das prestações excede 30% do seu salario.')


#Exercicio 37 - Aula 12
# print('Vamos converter um numero inteiro em binario, octal e hexadecimal!')
# n1 = int(input('Digite um numero inteiro: '))
# tipo_conversao = int(input('Digite 1 para converter para binario, 2 para octal e 3 para hexadecimal: '))
# if tipo_conversao == 1:
#     print(f'O valor do numero em binario é: {bin(n1)[2:]}')
# elif tipo_conversao == 2:
#     print(f'O valor do numero em octal é: {oct(n1)[2:]}')
# elif tipo_conversao == 3:
#     print(f'O valor do numero em hexadecimal é: {hex(n1)[2:].upper()}')
# else:
# 	print('Valor de conversão invalida!')


#Exercicio 38 - Aula 12
# print('-='*50)
# print('Vamos verificar qual numero é o maior!')
# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digite o segundo numero: '))
# if n1 > n2:
#     print('O primeiro valor é o maior!')
# elif n1 == n2:
#     print('Os Valores são iguais!')
# else:
#     print('O segundo valor é o maior!')


# #Exercicio 39 - Aula 12
# import time
# ano_nasc = int(input('Digite o ano do seu nascimento: '))
# ano_atual = time.localtime().tm_year
# idade = ano_atual - ano_nasc
# if idade == 18:
#     print('Voce tem ou faz 18 anos esse ano!')
#     print('Está na hora de se alistar!')
# elif idade > 18:
#     print('Você tem mais de 18 anos e já deveria ter se alistado!')
#     print(f'ja se passou {idade - 18} anos da data do seu alistamento')
#     print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
# else:
#     print('Você ainda não tem 18 anos!')
#     print(f'Faltam {18 - idade} anos para o seu alistamento!')
#     print(f'Seu alistamento será em {ano_atual + (18 - idade)}')


#Exercicio 40 - Aula 12
# print('Vamos verificar a media de um aluno')
# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# media = (n1 + n2) / 2

# if media < 5:
# 	print('REPROVADO')
# elif media >= 5 and media <= 6.9:
# 	print('RECUPERAÇÃO')
# else:
# 	print('APROVADO')
	

#Exercicio 41 - Aula 12
# from time import localtime
# print('Vamos verificar a categoria do atleta pela sua idade')
# ano_nasc = int(input('Digite o ano do seu nascimento: '))
# ano_atual = localtime().tm_year
# idade = ano_atual - ano_nasc
# if idade >= 1 and idade <= 9:
# 	print('Categoria: MIRIM')
# elif idade >=10 and idade <= 14:
# 	print('Categoria: INFANTIL')
# elif idade >= 15 and idade <= 19:
# 	print('Categoria: JUNIOR')
# elif idade == 20:
# 	print('Categoria: SÊNIOR')
# elif idade <= 0:
# 	print('A IDADE DIGITADA É INVALIDA')
# else:
# 	print('Categoria: MASTER')


#Exercicio 42 - Aula 12
# print('vamos verificar se 3 retas formam um triangulo')
# r1 = float(input('Digite o comprimento da primeira reta: '))
# r2 = float(input('Digite o comprimento da segunda reta: '))
# r3 = float(input('Digite o comprimento da terceira reta: '))
# # status = 'true' if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1 else 'false'
# if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
#     status = 'true'
# else:
#     status = 'false'
# if status == 'true' and r1 == r2 == r3:
# 	print('As retas formam um triangulo')
# 	print('O triangulo é Equilátero')
# elif status == 'true' and r1 == r2 != r3 or status == 'true' and r1 == r3 != r2 or status == 'true' and r2 == r3 != r1:
# 	print('As retas formam um triangulo')
# 	print('O triangulo é Isósceles')
# elif status == 'true' and r1 != r2 != r3:
# 	print('As retas formam um triangulo')
# 	print('O triangulo é Escaleno')
# elif status == 'false':
# 	print('As retas não formam um triangulo')
	

#Exercicio 42 OTIMIZADO- Aula 12
# print('vamos verificar se 3 retas formam um triangulo')
# r1 = float(input('Digite o comprimento da primeira reta: '))
# r2 = float(input('Digite o comprimento da segunda reta: '))
# r3 = float(input('Digite o comprimento da terceira reta: '))
# if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
#     print('As retas formam um triangulo')
#     if r1 == r2 == r3:
#           print('O triangulo é Equilátero')
#     elif r1 != r2 != r3 != r1:
#          print('O triangulo é Escaleno')
#     else:
#          print('O triangulo é Isósceles')
# else:
#     print('As retas não formam um triangulo')


#Exercicio 43 - Aula 12
# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# imc = peso / altura ** 2
# print(f'Seu IMC é: {imc:.2f}')
# if imc < 18.5 and imc > 0:
# 	print('Voce encontrasse: Abaixo do peso')
# elif imc >= 18.5 and imc <25:
# 	print('Voce encontrasse: No peso ideal')
# elif imc >= 25 and imc < 30:
# 	print('Voce encontrasse: Em sobrepeso')
# elif imc >= 30 and imc < 40:
# 	print('Voce encontrasse: Em obesidade')
# elif imc >= 40:
# 	print('Voce encontrasse: Em obesidade morbida')
# elif imc <= 0:
# 	print('Valor de peso ou altura invalido')


#Exercicio 43  OTIMIZADO- Aula 12
# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# imc = peso / altura ** 2
# print(f'Seu IMC é: {imc:.1f}')
# if imc <= 0:
# 	print('Valor de peso ou altura invalido')
# elif imc < 18.5:
# 	print('Voce encontrasse: Abaixo do peso')
# elif imc <25:
# 	print('Voce encontrasse: No peso ideal')
# elif imc < 30:
# 	print('Voce encontrasse: Em sobrepeso')
# elif imc < 40:
# 	print('Voce encontrasse: Em obesidade')
# elif imc >= 40:
# 	print('Voce encontrasse: Em obesidade morbida')


#Exercicio 44 - Aula 12
# preco_normal = float(input('Digite o valor do produto: R$'))
# forma_pagamento = str(input('Escolha a forma de pagamento entre DINHEIRO, CHEQUE e CARTÃO: ')).strip().upper()
# if forma_pagamento != 'DINHEIRO' and forma_pagamento != 'CHEQUE' and forma_pagamento !='CARTÃO':
#     print('Forma de pagamento invalida!')
# if forma_pagamento == 'CARTÃO':
# 	forma_pagamento = str(input('Digite o numero de parcelas: '))
# 	if forma_pagamento != '0' and forma_pagamento != '1' and forma_pagamento != '2' and  forma_pagamento != '3':
# 		print('Quantidade de parcelas invalida!')
# if forma_pagamento == 'DINHEIRO' or forma_pagamento == 'CHEQUE':
# 	preco_novo = preco_normal - preco_normal * 0.10
# 	print(f'O valor do produto com desconto de 10% para pagamentos em DINHEIRO ou CHEQUE ficou de: R${preco_novo}')
# elif forma_pagamento == '1' or forma_pagamento == '0':
# 	preco_novo = preco_normal - preco_normal * 0.05
# 	print(f'O valor do produto com desconto de 5% para pagamento a VISTA no CARTÃO ficou de: R${preco_novo}')
# elif forma_pagamento == '2':
# 	print(f'O valor do produto parcelado em 2X NO CARTÃO fica de: R${preco_normal}')
# 	print('Nesta forma de pagamento não tem desconto!')
# elif forma_pagamento == '3':
# 	preco_novo = preco_normal + preco_normal * 0.30
# 	print(f'O valor do produto parcelado em 3X NO CARTÃO fica de: R${preco_novo}')
# 	print('Nesta forma de pagamento entra 30% de juros no valor!')


# print('-=' * 34)
print('Vamos calcular o valor do produto de acordo com a forma de pagamento!')
print('-=' * 34)
preco_normal = float(input('Digite o valor do produto: R$'))
print('-=' * 34)
print('Escolha a forma de pagamento: \n[1] DINHEIRO \n[2] CHEQUE \n[3] CARTÃO')
print('-=' * 34)
forma_pagamento = str(input('Opção Desejada: ')).strip()
if forma_pagamento != '1' and forma_pagamento != '2' and forma_pagamento !='3':
    print('Forma de pagamento invalida!')
if forma_pagamento == '3':
	parcelas = str(input('Digite o numero de parcelas de 1x até 3x: ')).strip()
	if parcelas != '1' and parcelas != '2' and  parcelas != '3':
		print('Quantidade de parcelas invalida!')
if forma_pagamento == '1' or forma_pagamento == '2':
	preco_novo = preco_normal - preco_normal * 0.10
	print(f'O valor do produto com desconto de 10% para pagamentos em DINHEIRO ou CHEQUE ficou de: R${preco_novo}')
elif forma_pagamento == '3' and parcelas == '1':
	preco_novo = preco_normal - preco_normal * 0.05
	print(f'O valor do produto com desconto de 5% para pagamento a VISTA no CARTÃO ficou de: R${preco_novo}')
elif forma_pagamento == '3' and parcelas == '2':
	print(f'O valor do produto parcelado em 2X NO CARTÃO fica de: R${preco_normal}')
	print('Nesta forma de pagamento não tem desconto!')
elif forma_pagamento == '3' and parcelas == '3':
	preco_novo = preco_normal + preco_normal * 0.30
	print(f'O valor do produto parcelado em 3X NO CARTÃO fica de: R${preco_novo}')
	print('Nesta forma de pagamento entra 30% de juros no valor!')


# Exercicio 45 - Aula 12
# from random import choice
# from time import sleep
# print('-=' * 50)
# print('Vamos jogar pedra, papel ou tesoura!')
# print('-=' * 50)
# jogada_user = str(input('Digite sua jogada: ')).strip().upper()
# lista = ('PEDRA', 'PAPEL', 'TESOURA')
# print('PROCESSANDO .....')
# sleep(2)
# check = jogada_user in lista
# if check == False:
# 	print('A jogada escolhida é invalida')
# # if jogada_user != 'PEDRA' and jogada_user != 'PAPEL' and jogada_user != 'TESOURA':
# # 	print('A jogada escolhida é invalida')
# jogada_pc = choice(lista)
# if jogada_user == jogada_pc:
# 	print('Deu EMPATE')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# elif jogada_user == 'PEDRA' and jogada_pc == 'TESOURA':
# 	print('VOCE VENCEU')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# 	print('Pedra quebra tesoura!')
# elif jogada_user == 'PAPEL' and jogada_pc == 'PEDRA':
# 	print('VOCE VENCEU')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# 	print('Papel enrola pedra!')
# elif jogada_user == 'TESOURA' and jogada_pc == 'PAPEL':
# 	print('VOCE VENCEU')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# 	print('Tesoura corta pedra!')
# elif jogada_pc == 'PEDRA' and jogada_user == 'TESOURA':
# 	print('VOCE PERDEU')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# 	print('Pedra quebra tesoura!')
# elif jogada_pc == 'PAPEL' and jogada_user == 'PEDRA':
# 	print('VOCE PERDEU')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# 	print('Papel enrola pedra!')
# elif jogada_pc == 'TESOURA' and jogada_user == 'PAPEL':
# 	print('VOCE PERDEU')
# 	print(f'Voce escolheu {jogada_user} e eu escolhi {jogada_pc}.')
# 	print('Tesoura corta pedra!')