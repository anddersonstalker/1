from rich import print

class Caneta():

    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = '[blue]'
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampa = False


    def destampar(self):
        self.tampa = True


    def tampar(self):
        self.tampa = False
    

    def escrever(self, msg):
        if self.tampa:
            print(f"{self.cor}{msg}[/]", end='')
        else:
            print(f":prohibited: A {self.cor}caneta[/] não esta destampada.")

    def quebrar_linha(self, linhas = 1):
        print('\n' * linhas, end='')


c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()


c1.escrever('Olá, tudo bem? ')
c1.quebrar_linha(1)
c2.escrever('Olá, tudo bem? ')
c1.quebrar_linha(2)
c3.escrever('Olá, tudo bem? ')
