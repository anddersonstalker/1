from rich import print
from rich.panel import Panel


class Gamer():

    def __init__(self, nome, nick, jogos=list()):
        self.nome = nome
        self.nick = nick
        self.jogos = jogos


    def add_favoritos(self, jogo):
        self.jogos.append(jogo)


    def ficha(self):
        conteudo = f"Nome real: [on blue] {self.nome} [/]"
        conteudo += "\nJogos favoritos:"
        self.jogos.sort()
        for c in self.jogos:
            conteudo += f"\n:video_game: {c}"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)


j1 = Gamer("Fabricio da Silva", "detonador2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()