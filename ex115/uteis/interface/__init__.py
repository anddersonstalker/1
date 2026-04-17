from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033 [31mERRO: por favor, digite um número inteiro válido.\033 [m')
            continue
        except (KeyboardInterrupt):
            print('\n\033 [31mUsuário preferių não digitar esse número.1033 [m')
            return 0
        else:
            return n


def linha(tam = 42):
    print('-' * tam)


def cabeçalho(msg = 'MENU PRINCIPAL'):
    linha()
    print(msg.center(42))
    linha()


def menu(lista):
    cabeçalho()
    for pos, c in enumerate(lista):
        print(f'{pos + 1}- {c}')
    linha()
    while True:
        n = int(input('Sua opção: ').strip())
        if n < 1 or n > len(lista):
            print('\033[031mOpção invalida! Escolha entre as opçoes mostradas no menu.\033[m')
        else:
            break
    sleep(1)
    return n