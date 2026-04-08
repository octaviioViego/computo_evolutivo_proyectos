from .Mutacion import Mutacion
import random

"""
    - Mutación por intercambio.
"""

class MutacionIntercambio(Mutacion):
    
    def __init__(self,tasa_mutacion:float):
        self.tasa_mutacion = tasa_mutacion
    
    def mutar(self, individuo:list[int])-> list[int]:
        if random.random() < self.tasa_mutacion:
            tamano_individuo = len(individuo) - 1
            
            gen_uno, gen_dos = sorted(random.sample(range(1, tamano_individuo), 2))
            
            individuo[gen_uno], individuo[gen_dos] = individuo[gen_dos], individuo[gen_uno]
            
            return individuo