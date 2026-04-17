# def leiaint(msg):
#     while True:
#         n = input(msg)
#         if n == '':
#             print('\033[31mUsuário preferiu não digitar esse número.\033[0m')
#             return 0
#         else:
#             try:
#                 n = float(n.strip())
#             except:
#                 print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
#             else:
#                 return n


# def leiafloat(msg):
#     while True:
#         n = input(msg).replace(',', '.')
#         if n == '':
#             print('\033[31mUsuário preferiu não digitar esse número.\033[0m')
#             return 0
#         else:
#             try:
#                 n = float(n.strip())
#             except:
#                 print('\033[31mERRO! Digite um número real válido.\033[0m')
#             else:
#                 n = str(n)
#                 return n.replace('.', ',')



# n_int = leiaint('Digite um inteiro: ')
# n_float = leiafloat('Digite um Real: ')
# print(f'O valor inteiro digitado foi {n_int} e o real foi {n_float}')


# import urllib
# import urllib.request

# def verificar_url(url):
#     try:
#         site = urllib.request.urlopen(url)
#     except urllib.error.URLError:
#         return '\033[31mO site Pudim não está acessível no momento.\033[m'
#         site.read
#     else:
#         return '\033[32mConsegui acessar o site Pudim com sucesso!\033[m'
#         site.read
    

# site = verificar_url('https://pudim.com.br/')
# print(site)
# site.read


