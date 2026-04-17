from uteis.interface import *
from uteis.arquivo import *


arq = 'dados.txt'
teste = arquivoExiste(arq)
if not teste:
    criarArquivo(arq)
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
