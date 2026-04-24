from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados:int = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado, qtd_lados = 1):
        super().__init__(qtd_lados)
        self.lado:float = lado

    def perimetro(self):
        perimetro:float = self.lado * 4
        return perimetro

    def area(self):
        area:float = self.lado ** 2
        return area

class Circulo(Poligono):
    def __init__(self, raio, qtd_lados = 1):
        super().__init__(qtd_lados)
        self.raio:float = raio

    def perimetro(self):
        perimetro:float = 3.14 * (2 * self.raio)
        return perimetro

    def area(self):
        area:float = 3.14 * (self.raio ** 2)
        return area