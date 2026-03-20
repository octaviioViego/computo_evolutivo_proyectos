from mutacion import Mutacion
import numpy as np
import numpy.typing as npt

class Tasa_mutacion(Mutacion):
    def generar_mutacion(self,carga: npt.NDArray[np.int8])->npt.NDArray[np.int8]:
        tasa_mutacion:float = 0.10
        tamano_carga: int = len(carga)
        probabilidades:npt.NDArray[np.float16] = np.random.uniform(0,1,size=tamano_carga)
        
        for posicion,probabilidad in enumerate(probabilidades):
            if probabilidad <= tasa_mutacion:
                if carga[posicion] == 0:
                    carga[posicion] = 1
                    continue
                
                carga[posicion] = 0
        
        return carga