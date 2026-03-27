from penalizacion import Penalizacion
import math

class Exponencial(Penalizacion):
    
    def calcular_aptitud(self) -> float:
        alfa: float = 0.01

        if self.peso_total <= self.peso_maximo:
            return 0

        exceso = self.peso_total - self.peso_maximo
        valor_penalizacion = alfa * math.exp(exceso)

        return valor_penalizacion