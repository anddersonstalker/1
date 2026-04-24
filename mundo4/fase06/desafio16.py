from rich import print


class Funcionario:
    """
Cria um funcionario com atributos, NOME, SETOR E CARGO.
    """
    empresa = 'Curso em Video'


    def __init__(self, nome = 'Desconhecido', setor = '', cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    
    def apresentacao(self):
        return f":Handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}."


f1 = Funcionario('Pedro', 'Financeiro', 'Contador')
print(f1.apresentacao())