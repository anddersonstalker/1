def leiaDinheiro(msg):
    valida = False
    while not valida:
        n = input(msg).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[31mERRO:"{n}" é um preço invalido!\033[0m')
        else:
            valida = True
            return float(n)
