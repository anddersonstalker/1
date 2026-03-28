#Exercicio 1
print('Vamos verificar o antecessor e o sucessor de um numero')
print('')

n1=int(input('Digite o numero que você deseja verificar o antecessor e o sucessor:'))
print('')
print(f'O antecessor de {n1} é {n1-1} e o sucessor é {n1+1}')
print('')
print(f'O dobro desse numero é: {n1*2} \nO triplo deste numero é: {n1*3} \nA raiz quadrada deste numero é: {n1**(1/2):.2f} \nA raiz cubica deste numero é: {n1**(1/3):.2f}')

print('='*100)
print('')


#Exercicio 2
print('Agora vamos calcular a media entre duas notas de um aluno')
nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
media=(nota1+nota2)/2
print('')
print(f'A media das notas deste aluno é: {media:.2f}')

print('='*100)
print('')


#Exercicio 3
print('Agora vamos converter metros em centimetros e milimetros')
print('')
metros=float(input('Digite o valor em metros que deseja converter: '))
cm=int(metros*100)
mm=int(metros*1000)
print(f'O valor em centimetros é: {metros*100}cm \nO valor em milimetros é: {metros*1000}mm')
print(f'O valor em centimetros é: {cm}cm \nO valor em milimetros é: {mm}mm')

print('='*100)
print('')


#Exercicio 4
print('Agora vamos calcular a tabuada de um numero')
tabuada=int(input('Digite o numero para consultar sua tabuada: '))
print('')

print(f'{tabuada} x {1:2} = {tabuada*1}')
print(f'{tabuada} x {2:2} = {tabuada*2}')
print(f'{tabuada} x {3:2} = {tabuada*3}')
print(f'{tabuada} x {4:2} = {tabuada*4}')
print(f'{tabuada} x {5:2} = {tabuada*5}')
print(f'{tabuada} x {6:2} = {tabuada*6}')
print(f'{tabuada} x {7:2} = {tabuada*7}')
print(f'{tabuada} x {8:2} = {tabuada*8}')
print(f'{tabuada} x {9:2} = {tabuada*9}')
print(f'{tabuada} x {10:2} = {tabuada*10}')

print('='*100)
print('')


#Exercicio 5
print('Vamos calcular quantos dolares você pode comprar com uma quantia em reais')
reais=float(input('Digite quantos reais você tem disponivel pra compra de dolares: '))
print('')

print(f'Com esta quantia de R${reais} voce pode comprar US${reais/3.27:.2f} dolares')

print('='*100)
print('')


#Exercicio 6
print('Vamos calcular a qauntida de tinta necessaria para pintar uma parede')
print('')

altura=float(input('Primeiro digite a Altura da parede: '))
largura=float(input('Agora digite a Largura da parede: '))
area=altura*largura
print('')

print(f'A area desta parede é de: {area:.2f}m² \nE a quantidade de tinta necessaria para pintar esta parede é de: {area/2:.2f} litros')

print('='*100)
print('')


#Exercicio 7
print('Vamos calcular o valor com desconto de um produto')
print('')

preco=float(input('Digite o preço do produto: '))
desconto=float(input('Digite o valor do desconto em %: '))
print('')

print(f'O valor com desconto do produto é de: R${preco-(preco*(desconto/100)):.2f}')

print('='*100)
print('')


#Exercicio 8
print('Vamos calcular o valor do salario de um funcionario com aumento')
print('')
salario=float(input('Digite o valor do salario do funcionario: '))
aumento=float(input('Digite o valor do aumento em %: '))
print('')

print(f'O novo salario do funcionario é de: R${salario+(salario*(aumento/100)):.2f}')

print('='*100)
print('')


#Exercicio 9
print('Vamos calcular a temperatura de Celsius para Fahrenheit')
temp=float(input('Digite a temperatura em ºC: '))
print('')

print(f'A temperatura em Farenheit é de: {temp*1.8+32:.2f}ºF')

print('='*100)
print('')


#Exercicio 10
print('Vamos calcular o valor do aluguel de um carro')
dias=int(input('Digite a quantidade de dias que o carro foi alugado: '))
km=float(input('Agora digite a quantidade de km rodados: '))
print('')

print(f'O Valor total do aluguel é de {dias*60+km*0.15:.2f} reais')
