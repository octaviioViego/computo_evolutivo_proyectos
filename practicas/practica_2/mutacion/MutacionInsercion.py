from .Mutacion import Mutacion
import random

"""
    - Mutación por inserción.
"""
class MutacionInsercion(Mutacion):
    
    def __init__(self,tasa_mutacion:float):
        self.tasa_mutacion = tasa_mutacion
    

    def mutar(self, individuo:list[int])-> list[int]:
        if random.random() > self.tasa_mutacion:
            # Nos aseguramos que el tamaño maximo -1 sea valido en nuestro for.
            tamano_individuo = len(individuo) - 1

            gen_uno, gen_dos = sorted(random.sample(range(1, tamano_individuo), 2))
                     
            for i in range(gen_dos,gen_uno+1,-1):
                individuo[i],individuo[i-1] = individuo[i-1],individuo[i] 

            return individuo