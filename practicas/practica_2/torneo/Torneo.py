import numpy as np
import numpy.typing as npt
import random
from Individuo import Individuo


class Torneo():
    def seleccionar_padres(self,poblacion:list[Individuo])-> tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]]:
        
        seleccionados = random.sample(list(poblacion),5)
        candidatos_array_ordenados:npt.NDArray = sorted(seleccionados, key=lambda ind:ind.fitness) 
    
        torneo: npt.NDArray = candidatos_array_ordenados[-2:] 
    
        # Ordenar a los individuos seleccionados de acuerdo a la aptitud y seleccionar a los 2 mejores
        ruta_uno: tuple[np.array,int] = torneo[0]
        ruta_dos: tuple[np.array,int] = torneo[1]
        
        
        return ruta_uno, ruta_dos