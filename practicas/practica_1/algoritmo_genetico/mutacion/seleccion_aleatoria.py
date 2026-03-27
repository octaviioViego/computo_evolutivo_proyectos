from mutacion import Mutacion
import numpy as np
import numpy.typing as npt

class Seleccion_aleatoria(Mutacion):
    def generar_mutacion(self,carga: npt.NDArray[np.int8])->npt.NDArray[np.int8]:
        if np.random.random() <= 0.10:  
        
            pos = np.random.randint(0, len(carga))
            carga[pos] = 1 - carga[pos]  
    
        return carga