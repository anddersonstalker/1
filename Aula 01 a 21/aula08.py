# import math
from random import choice, shuffle
#import pygame
import pygame
import time

#tarefa 1
# #print('Vamos calcular a parte inteira de um numero!')
#num= float(input("Digite um número: "))
#print(f'O numero {num} tem a parte inteira {math.trunc(num)}')


#tarefa 2
#print('Vamos calcular a hipotenusa de um triângulo retângulo!')
#co= float(input('Digite o valor do cateto oposto: '))  
#ca= float(input('Digite o valor do cateto adjacente: '))
#hipotenusa= math.hypot(co, ca)
#hipotenusa2= math.sqrt(co**2 + ca**2)
#print(f'A hipotenusa do triângulo retângulo é: {hipotenusa}')
#print(f'A hipotenusa do triângulo retângulo é: {hipotenusa2}')


#tarefa 3
#print('Vamos calcular o seno, cosseno e tangente de um ângulo!')
#angulo= float(input('Digite o valor do ângulo: '))
#seno= math.sin(math.radians(angulo))
#cos= math.cos(math.radians(angulo))
#tan= math.tan(math.radians(angulo))
#print(f'O seno do ângulo é: {seno:.4f}')
#print(f'O cosseno do ângulo é: {cos:.4f}')
#print(f'A tangente do ângulo é: {tan:.4f}')


# #tarefa 4
print('Vamos sortear aleatoriamente o nome de um aluno!')
nomes= (input('Digite o nome do primeiro aluno: '),
input('Digite o nome do segundo aluno: '), 
input('Digite o nome do terceiro aluno: '), 
input('Digite o nome do quarto aluno: ') )
print(nomes)
print(f'O aluno sorteado foi: {choice(nomes)}')


# tarefa 5
# print('Vamos sortear a ordem de apresentação dos alunos!')
# nomes= [input('Digite o nome do primeiro aluno: '),
# input('Digite o nome do segundo aluno: '),
# input('Digite o nome do terceiro aluno: '),
# input('Digite o nome do quarto aluno: ')]
# random.shuffle(nomes)
# print(f'A ordem de apresentação dos alunos é: {nomes}')

#tarefa 6
# pygame.init()
# pygame.mixer.music.load('teste.mp3')
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     time.sleep(1)
# print("A música acabou e o programa foi encerrado com sucesso!")