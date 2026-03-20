from penalizacion import Penalizacion

class Lineal(Penalizacion):

    def calcular_aptitud(self)-> int:
        
        alfa:int = 1
        valor_penalizacion: int = 0
        exceso: int = 0
        
        if self.peso_total <= self.peso_maximo:
            return 0

        exceso = (self.peso_total - self.peso_maximo)
        valor_penalizacion = (alfa * exceso)
        
        return  valor_penalizacion