class Churrasco():

    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas


    def analizar(self):
        from rich.panel import Panel
        from rich import print
        quant = 0.4 * self.pessoas
        valorkg = 82.4
        valortot = quant * valorkg
        custo = valortot / self.pessoas
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]\n"
        conteudo += f"Cada participante comerá 0.4kg e cada Kg custa R${valorkg:.2f}\n"
        conteudo += f"Recomendo [blue]comprar {quant:.3f}Kq[/] de carne\n"
        conteudo += f"O custo total será de [green]R${valortot:.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${custo}[/] para participar."
        painel = Panel(conteudo, title=self.titulo, width=60)
        print(painel)
        

c1 = Churrasco('Churras dos Amigos', 15)
c1.analizar()