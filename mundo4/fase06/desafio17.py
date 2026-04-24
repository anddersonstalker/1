class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    
    def etiqueta(self):
        from rich.panel import Panel
        from rich import print
        preco_formatado = f'R${self.preco:,.2f}'
        caixa = Panel(f"{self.nome:^41}\n{'':-^41}\n{preco_formatado:.^41}", title='PRODUTO', width=45)
        print(caixa)


    # def etiqueta(self):
    #     from rich.panel import Panel
    #     from rich import print
    #     conteudo = f"{self.nome.center(41, ' ')}"
    #     conteudo += f"{'-' * 41}"
    #     precof = f"R${self.preco:,.2f}"
    #     conteudo += f"{precof.center(41, '.')}"
    #     etiqueta = Panel(conteudo, title='Produto', width=45)
    #     print(etiqueta)
    


p1 = Produto("Iphone 17 pro max", 25000)
p1.etiqueta()