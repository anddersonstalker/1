# Area de Classes
class Aluno:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade


    # Metodos de instancia
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f'{self.nome} é aluno e tem {self.idade} anos de idade'


# Area de Objetos
a1 = Aluno('Diego', 29)
a1.aniversario()
print(a1.mensagem())
