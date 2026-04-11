from .Cruza import Cruza

class CruzaCiclos(Cruza):
    
    def ejecutar(self, padre1: list[int], padre2: list[int]) -> tuple[list[int], list[int]]:

        hijo_uno = self._algoritmo_ciclos(padre_uno=padre1,padre_dos=padre2)
        hijo_dos = self._algoritmo_ciclos(padre_uno=padre2,padre_dos=padre1)
        
        return hijo_uno, hijo_dos

    def _algoritmo_ciclos(self,padre_uno:list[int], padre_dos:list[int]) -> list[int]:
       
        moviles_p1 = padre_uno[1:]
        moviles_p2 = padre_dos[1:]

        size:int = len(moviles_p1)
        posiciones_visitadas = [False] * size
        hijo = [-1] * size

        heredar_p1:bool = True
        

        for posicion_inicial in range(size):
        
            if posiciones_visitadas[posicion_inicial]:
                continue
            
            posicion = posicion_inicial
            
            while not posiciones_visitadas[posicion]:

                if heredar_p1:
                    # Heredamos del primer padre
                    hijo[posicion] = moviles_p1[posicion]
                else:
                    # Heredamos del segundo padre
                    hijo[posicion] = moviles_p2[posicion]

                #Las posiciones visitadas
                posiciones_visitadas[posicion] = True 
                valor = moviles_p2[posicion]
                posicion = moviles_p1.index(valor)
                
            heredar_p1 = not heredar_p1

        hijo = [0] + hijo

        return hijo
