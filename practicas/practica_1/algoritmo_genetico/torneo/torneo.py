import numpy as np
import numpy.typing as npt
import random

class Torneo():
    def seleccionar_padres(self,poblacion: npt.NDArray[np.int8])-> tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]]:
        
        seleccionados = random.sample(list(poblacion),5)
        candidatos_array_ordenados:npt.NDArray = sorted(seleccionados, key=lambda x:x[1]) 
        # print("Candidatos")
        # print(candidatos_array_ordenados)
        torneo: npt.NDArray = candidatos_array_ordenados[-2:] 
        # print("Seleccionados")
        # print(torneo)
        # Ordenar a los individuos seleccionados de acuerdo a la aptitud y seleccionar a los 2 mejores
        carga1: tuple[np.array,int] = torneo[0] 
        carga2: tuple[np.array,int] = torneo[1]
        

        
        return carga1, carga2