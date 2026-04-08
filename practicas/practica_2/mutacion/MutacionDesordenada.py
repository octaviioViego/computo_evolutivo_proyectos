from .Mutacion import Mutacion

"""
    - Mutación desordenada.
"""
class MutacionDesordenada(Mutacion):
    
    def __init__(self,tasa_mutacion:float):
        self.tasa_mutacion = tasa_mutacion
    

    def mutacion(self, individuo:list[int])-> list[int]:
        pass