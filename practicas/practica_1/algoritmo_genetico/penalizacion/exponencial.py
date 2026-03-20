from penalizacion import Penalizacion
import math

class Exponencial(Penalizacion):
    
    def calcular_aptitud(self) -> int:
        alfa:int = 1
        valor_penalizacion: int = 0
        exceso: int = 0

        if self.peso_total <= self.peso_total:
            return 0

        exceso = self.peso_total-self.peso_maximo

        valor_penalizacion = (alfa * (self.math.exp(exceso)))
        
        return  valor_penalizacion