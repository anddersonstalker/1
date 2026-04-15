# Exercicio 1
# nome= str(input('Digite o nome completo: ')).strip()
# print('Nome em Maiusculas:', nome.upper())
# print('Nome em Minusculas:', nome.lower())
# print(f'E tem {len(nome)-nome.count(' ')} caracteres')
# print(f'o primeiro nome tem {nome.find(' ')} letras.')

# lista= nome.split()
# print('Quantidade de caracteres:', len(''.join(lista)))
# print(f'O seu primeiro nome é: {lista[0]} e ele tem: {len(lista[0])} letras')


# #Exercicio 2 -
# num= input('Digite um numero entre 0 e 9999: ')[:4]
# print(num)
# print(f'unidade: {num[3]} \ndezena: {num[2]} \ncentena: {num[1]} \nmilhar: {num[0]}')


# #Exercicio 2 - Matematicamente
# num= int(input('Digite um numero entre 0 e 9999: ')[:4])
# print(num)
# print(f'unidades: {num//1%10} \ndezenas: {num//10%10} \ncentenas: {num//100%10} \nmilhares: {num//1000%10}')


#Exercicio 3 - soluçao do vscode
# cidade= str(input('Digite o nome da cidade: ')).strip()
# print(cidade[:5].upper() == 'SANTO')


#Exercicio 3 - soluçao propria
# cidade= str(input('Digite o nome da cidade: ')).strip()
# lista= cidade.split()
# print('SANTO' in lista[0].upper())


#Exercicio 4
# nome= str(input('Digite seu nome completo: ')).strip()
# print('SILVA' in nome.upper())


# #Exercicio 5
# frase= str(input('Digite uma frase: ')).strip()
# print(f'A letra A aparece {frase.upper().count('A')} vezes na frase')
# print(f'A primeira letra A aparece na posição: {frase.upper().find('A')+1}')
# print(f'A ultima letra A parece na posição: {frase.upper().rfind('A')+1}')


#Exercicio 6
# nome= str(input('Digite seu nome completo: ')).strip()
# lista= nome.split()
# print(lista)
# print(f'Seu primeiro nome é: {lista[0]}')
# print(f'Seu ultimo nome é: {lista[len(lista)-1]}')