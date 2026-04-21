def linha(tam = 42):
    print('-' * tam)


def titulo(msg):
    linha()
    print(msg.center(42))
    linha()


def menu(lista):
    from mundo4.aula03.Escola.pacotes.dados import verifica_int

    titulo('MENU DO SISTEMA')
    for pos, c in enumerate(lista):
        print(f'{pos + 1:<4}{c:<38}')
    linha()
    while True:
        opc = verifica_int('Digite a opção desejada: ')
        if opc < 1 or opc > len(lista):
            linha()
            print('\033[031mOpção invalida! Escolha entre as opções fornecidas!\033[m')
        else:
            break
    return opc

