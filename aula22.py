# # Exercicio 107 - Aula 22
# import moeda

# p = float(input('Digite o preço: R$'))
# print(f'A metade de {p} é {moeda.metade(p)}')
# print(f'O dobro de {p} é {moeda.dobro(p)}')
# print(f'Aumentando 10%, temos {moeda.aumentar (p, 10)}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')


# Exercicio 109 - Aula 22
# from modulos import moeda

# p = float(input('Digite o preço: R$'))
# print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
# print(f'Aumentando 10%, temos {moeda.aumentar (p, 10, True)}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')



# Exercicio 110 - Aula 22
# from utilidadesCeV import moeda

# p = float(input('Digite o preço: R$'))
# moeda.resumo(p, 10, 13)


# Exercicio 111 - Aula 22
from utilidadesCeV import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 10, 10)