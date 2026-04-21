# Area de Classes
class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0


# Metodos de instancia
def aniversario(self):
    self.idade += 1


def mensagem(self):
    print(f'O {self.nome} é aluno e tem {self.idade} anos de idade e seu signo é {self.signo}')


# Area de Objetos
a1 = Aluno()
a1.nome = 'Diego'
a1.idade = 29

aniversario(a1)

mensagem(a1)