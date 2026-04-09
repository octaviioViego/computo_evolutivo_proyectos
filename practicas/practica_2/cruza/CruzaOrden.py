from .Cruza import Cruza 
import random

class CruzaOrden(Cruza):
    """Implementación del Order Crossover (OX1)."""
    
    def ejecutar(self, padre1:list[int], padre2:list[int])-> tuple[list[int],list[int]]:
        size:int = len(padre1)
        hijo_uno:list[int] = [None] * size
        hijo_dos:list[int] = [None] * size
        
        hijo_uno:list[int] = self._generar_hijo_ox(padre1=padre1,padre2=padre2,size=size)
        hijo_dos:list[int] = self._generar_hijo_ox(padre1=padre2,padre2=padre1,size=size) 

        return hijo_uno,hijo_dos

    def _generar_hijo_ox(self, padre1: list[int], padre2: list[int], size: int) -> list[int]:
        hijo = [None] * size
        
        # 1. Fijar Ciudad de México (Se puede fijar cualquiero otra ciudad solo acomonandolo en la posicion 0).
        hijo[0] = padre1[0]
        
        # 2. Definir segmento aleatorio (sin tocar el indice 0)
        punto_uno, punto_dos = sorted(random.sample(range(1, size), 2))
        hijo[punto_uno:punto_dos+1] = padre1[punto_uno:punto_dos+1]
        
        # 3. Recolectar ciudades de padre2 que no estan en el segmento
        # Empezamos a buscar desde punto_dos+1 para mantener el orden circular
        contenido_hijo = set(hijo)
        p2_circular = padre2[punto_dos+1:] + padre2[:punto_dos+1]
        faltantes = [ciudad_p2 for ciudad_p2 in p2_circular if ciudad_p2 not in contenido_hijo]
        
        # 4. Rellenar los huecos 
        faltantes.reverse() 
        
        # Rellenamos de punto_dos+1 hasta el final
        for posicion in range(punto_dos + 1, size):
            if hijo[posicion] is None:
                hijo[posicion] = faltantes.pop()
        
        # Rellenamos desde el inicio (después del 0) hasta punto_dos
        for posicion in range(1, punto_dos + 1):
            if hijo[posicion] is None:
                hijo[posicion] = faltantes.pop()
                
        return hijo