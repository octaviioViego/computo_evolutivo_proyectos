from .Mutacion import Mutacion
import random
"""
    - Mutación desordenada.
"""
class MutacionDesordenada(Mutacion):
    
    def __init__(self,tasa_mutacion:float):
        self.tasa_mutacion = tasa_mutacion
    

    def mutar(self, individuo:list[int])-> list[int]:
        if random.random() < self.tasa_mutacion:
            tamano_individuo = len(individuo) - 1
            
            inicio, fin = sorted(random.sample(range(1, tamano_individuo), 2))
            
            individuo_aux = individuo[inicio:fin] 
            
            sub_conjunto = random.sample(individuo_aux, (len(individuo_aux)))
            individuo[inicio:fin] = sub_conjunto
            
            return individuo
