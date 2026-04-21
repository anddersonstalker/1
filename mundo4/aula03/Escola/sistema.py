from mundo4.aula03.Escola.pacotes.interface import *
from mundo4.aula03.Escola.pacotes.dados import *


arq = 'dados_alunos.txt'
teste = testa_arquivo(arq)
if not teste:
    criar_arquivo(arq)

while True:
    resp = menu(('VER ALUNOS CADASTRADOS', 'CADASTRAR ALUNOS', 'SAIR DO SISTEMA'))
    if resp == 1:
        titulo('LISTA DE ALUNOS CADASTRADOS')
        ler_arquivo(arq)
    elif resp == 2:
        titulo('CADASTRO DE ALUNOS')
        nome = str(input('Nome do aluno: '))
        idade = verifica_int('Idade do aluno: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        linha()
        print('SAINDO DO SISTEMA... VOLTE SEMPRE!'.center(42))
        break