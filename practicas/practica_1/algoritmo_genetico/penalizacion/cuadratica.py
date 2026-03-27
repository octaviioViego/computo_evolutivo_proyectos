from penalizacion import Penalizacion

class Cuadratica(Penalizacion):
    
    def calcular_aptitud(self) -> float:
        alfa: float = 0.2

        if self.peso_total <= self.peso_maximo:
            return 0

        exceso = self.peso_total - self.peso_maximo
        valor_penalizacion = alfa * (exceso ** 2)

        return valor_penalizacion