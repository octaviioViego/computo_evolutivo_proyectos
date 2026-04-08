from .Mutacion import Mutacion
import random
"""
    - Mutacón por inversión.
"""
class MutacionInversion(Mutacion):
    
    def __init__(self,tasa_mutacion:float):
        self.tasa_mutacion = tasa_mutacion
        
    def mutar(self, individuo:list[int])-> list[int]:
        if random.random() < self.tasa_mutacion:
            tamano_individuo = len(individuo) - 1
           
            inicio, fin = sorted(random.sample(range(1, tamano_individuo), 2))
            

            aux_individuo = individuo[inicio:fin]
            aux_individuo.reverse()
            individuo[inicio:fin] = aux_individuo

            return individuo