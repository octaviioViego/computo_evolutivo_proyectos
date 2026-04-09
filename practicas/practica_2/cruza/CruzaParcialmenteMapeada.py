from .Cruza import Cruza
import random

class CruzaParcialmenteMapeada(Cruza):
    """
    - (PMX)
    """

    def ejecutar(self, padre1:list[int], padre2:list[int])-> tuple[list[int],list[int]]:
        size:int = len(padre1)

        hijo_uno:list[int] = [None] * size
        hijo_dos:list[int] = [None] * size

        hijo_uno = self._algoritmo_PMX(padre1=padre1,padre2=padre2,size=size)
        hijo_dos = self._algoritmo_PMX(padre1=padre2,padre2=padre1,size=size)

        return hijo_uno, hijo_dos
    
    
    def _algoritmo_PMX(self, padre1:list[int], padre2:list[int], size:int) -> list[int]:
    
        hijo:list[int] = [None] * size
        
        # 1. Fijar Ciudad de México (Se puede fijar cualquiero otra ciudad solo acomonandolo en la posicion 0).
        hijo[0] = padre1[0]
        punto_uno, punto_dos = sorted(random.sample(range(1,size),2))
        hijo[punto_uno:punto_dos+1] = padre1[punto_uno:punto_dos+1]
        
        for posicion in range(punto_uno,punto_dos+1):
            ciudad_p2  = padre2[posicion]
            
            if ciudad_p2 not in hijo:
                recorrido = posicion
                while True:
                    valor_p1 = padre1[recorrido]
                    posicion_valor_p2 = padre2.index(valor_p1)

                    if hijo[posicion_valor_p2] is None:
                            hijo[posicion_valor_p2] = ciudad_p2
                            break
                    
                    recorrido = posicion_valor_p2
            
        
        for posicion in range(size):
            if hijo[posicion] is None:
                hijo[posicion] = padre2[posicion]

        return hijo