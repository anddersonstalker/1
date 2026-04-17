def metade(n, format = False):
    res = n / 2
    return res if not format else moeda(res)


def dobro(n, format = False):
    res = n * 2
    if format:
         return moeda(res)
    return res


def aumentar(n, a, format = False):
    res = n + n * (a / 100)
    if format:
         return moeda(res)
    return res


def diminuir(n, a, format = False):
    res = n - n * (a / 100)
    if format:
         return moeda(res)
    return res


def moeda(n = 0, moeda = 'R$'):
          return f"{moeda}{n:.2f}".replace('.', ',')


def resumo(p, a, d):
     print('-'*29)
     print('       RESUMO DO VALOR')
     print('-'*29)
     print(f"{'Preço analisado:':<19}{moeda(p)}")
     print(f"{'Dobro do preço:':<19}{dobro(p, True)}")
     print(f"{'Metade do Preço:':<19}{metade(p, True)}")
     print(f"{a}% {'de aumento:':<15}{aumentar(p, a, True)}")
     print(f"{d}% {'de redução:':<15}{diminuir(p, d, True)}")
     print('-'*29)