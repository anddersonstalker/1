def testa_arquivo(nome):
    try:
        a = open(nome)
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('\033[31mERRO ao criar o arquivo!\033[m')
    else:
        print(f'\033[32mO arquivo {nome} foi criado com sucesso!\033[m')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler o arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:-<34}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'DESCONHECIDO', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mERRO ao escrever no arquivo!\033[m')
        else:
            print(f'\033[32mO aluno {nome} foi cadastrado com sucesso!\033[m')
    finally:
        a.close()


def verifica_int(msg):
    while True:
        n = input(msg).strip()
        try:
            n = int(n)
        except:
            print('\033[31mO valor informado é invalido! Tente novamente!\033[m')
        else:
            return n