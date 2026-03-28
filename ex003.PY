valor1= (input('Digite algo: '))

print('O tipo primitivo deste valor é: {}'.format(type(valor1)))
print('Só tem espaços?', valor1.isspace())
print('O tipo primitivo deste valor é:', type(valor1))

print('o tipo é: {}, o valor é numerico? {}, o valor é alpha? {}, o valor é alpha numerico? {}, o valor é decimal? {}' .format(type(valor1), valor1.isnumeric(), valor1.isalpha(), valor1.isalnum(), valor1.isdecimal()))

print('esta em capitalizada:', valor1.istitle())


print('O tipo primitivo deste valor é:', type(valor1))
print('O tipo primitivo deste valor é: {}'.format(type(valor1)))
print(f'O tipo primitivo deste valor é: {type(valor1)}')