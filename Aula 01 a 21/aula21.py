# # Exercicio 101 - Aula 21
# def voto(nasc):
#     from datetime import date
#     ano = date.today().year
#     idade = ano - nasc
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA'
#     elif 16 <= idade < 18  or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    

# nasc = int(input('Em que ano você nasceu? '))
# print(voto(nasc))


# # Exercicio 102 - Aula 21
# def fatorial(num, show=False):
#     """
#     --> Calcula o Fatorial de um número.
#     :param num: O número a ser calculade.
#     :param show: (opcional) Mostrar ou não a conta.
#     :return: O valor do Fatorial de um número n.
#     """
#     from time import sleep
#     a = 1
#     for c in range(num, 0, -1):
#         a *= c
#         if show:
#             if c > 1:
#                 print(c, end=' x ', flush = True)
#                 sleep(0.5)
#             else:
#                 print(f'{c} =', end=' ')
#     return a


# def set_opc(opc):
#     global show
#     if opc == 'S':
#         show = True
#     else:
#         show = False


# num = int(input('Digite o numero que deseja consultar o fatorial: ').strip())
# show = str(input('Deseja ver o processo de calculo? [S/N] ').strip().upper()[0])
# set_opc(show)
# print(fatorial(num, show))
# help(fatorial)


# # Exercicio 103 - Aula 21
# def ficha(a= False, b= False):
#     if not a:
#         a = 'DESCONHECIDO'
#     return f'O jogador {a} fez {b} gol(s) no campeonato.'


# nome = str(input('Nome do Jogador: '))
# gols = input('Número de Gols: ')
# if gols.isnumeric():
#     gols = int(gols)
# else:
#     gols = 0
# print(ficha(nome, gols))


# # Exercicio 104 - Aula 21
# def leiaint(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
#         if ok:
#             break
#     return valor


# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')


# def leiaint(msg):
#     while True:
#         if msg.isnumeric():
#             return int(msg)
#         else:
#             print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
#             msg = input('Digite um número: ').strip()


# n = leiaint(input('Digite um número: ').strip())
# print(f'Você acabou de digitar o número {n}')



# def leiaint(msg):
#     while True:
#         n = input(msg).strip() 
#         if n.isnumeric():
#             return int(n)
#         print('\033[31mERRO! Digite um número inteiro válido.\033[0m')


# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')


# # Exercicio 105 - Aula 21
# def notas(* n, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param n: uma ou mais notas dos alunos (aceita várias)
#     :param sit: valor opcional, indicando se deve ou não adicionar a situação
#     :return: dicionário com várias informações sobre a situação da turma.
#     """
#     ficha = dict()
#     ficha['Total'] = len(n)
#     ficha['Maior'] = max(n)
#     ficha['Menor'] = min(n)
#     ficha['Média'] = sum(n) / len(n)
#     if sit:
#         if ficha['Média'] < 5:
#             ficha['Situação'] = 'RUIM'
#         elif 5 < ficha['Média'] < 7:
#             ficha['Situação'] = 'RAZOÁVEL'
#         else:
#             ficha['Situação'] = 'BOA'
#     return ficha


# resp = (notas(5.5, 9.5, 10, 6.5, sit=True))
# print(resp)


# # Exercicio 106 - Aula 21
# def PyHELP():
#     while True:
#         msg = 'SISTEMA DE AJUDA PyHELP'
#         print('\033[30;42m')
#         print('-' * (len(msg) + 4))
#         print(f'  {msg}  ')
#         print(('-' * (len(msg) + 4)))
#         print('\033[0m')

#         ajuda = str(input('Função ou Biblioteca > ').strip().lower())
#         msg = f"Acessando o manual do comando '{ajuda}'"
#         if ajuda == 'fim':
#             msg = 'ATÉ LOGO!'
#             print('\033[30;41m', end='')
#             print('-' * (len(msg) + 4))
#             print(f'  {msg}  ')
#             print(('-' * (len(msg) + 4)))
#             print('\033[0m')
#             break
#         else:
#             print('\033[30;44m', end='')
#             print('-' * (len(msg) + 4))
#             print(f'  {msg}')
#             print(('-' * (len(msg) + 4)))
#             print('\033[0m')
#             print('\033[47;30m', end='')
#             help(ajuda)
#             print('\033[0m')


# PyHELP()



# from time import sleep
# c = ('\033[m',        #0 - sem cores
#      '\033[0;30;41m', #1 - vermelho
#      '\033[0;30;42m',  #2 - verde
#      '\033[0;30;43m',  #3 - amarelo
#      '\033[0;30;44m', #4 - azul
#      '\033[0;30;45m', #5 - roxo
#      '\033[7;30m' #6 - branco
#      );



# def ajuda (com):
#     título (f'Acessando o manual do comando \'{com}\'', 4)
#     print(c[6], end='')
#     help(com)
#     print(c[0], end='')
#     sleep(2)


# def título (msg, cor=0):
#     tam = len(msg) + 4
#     print(c[cor], end='')
#     print('~' * tam)
#     print(f'  {msg}')
#     print('~' * tam)
#     print(c[0], end='')
#     sleep(1)


# #Programa Principal
# comando = ''
# while True:
#     título ('SISTEMA DE AJUDA PYHELP', 2)
#     comando = str(input("Funcão ou Biblioteca > "))
#     if comando.upper() == 'FIM':
#         break
#     else:
#         ajuda (comando)
# título('ATÉ LOGO!', 1)