from rich import print
from time import sleep


class Livro():

    def __init__(self, titulo, paginas, cont= 1):
        self.titulo = titulo
        self.paginas = paginas
        self.cont = cont
        print(f":book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.paginas} páginas[/] no total. Você agora está na página {cont}")


    def avancar_paginas(self, quant):
        passo = 0
        for c in range(0, quant):
            if self.cont < self.paginas:
                self.cont += 1
                print(f"Pág{self.cont} ", end='> ')
                passo +=1
                sleep(0.3)
        print(f"[blue]Você avançou {passo} páginas e agora está na [yellow]página {self.cont}")
        if self.cont == self.paginas:
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")



l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(20)

