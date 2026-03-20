from penalizacion import Penalizacion  

class Fitness_Cero(Penalizacion):

    def calcular_aptitud(self) -> int:
        if self.peso_total > self.peso_maximo: 
            return 0
        
        return self.peso_total 