from mutacion import Mutacion
import numpy as np
import numpy.typing as npt

class Seleccion_aleatoria(Mutacion):
    def generar_mutacion(self,carga: npt.NDArray[np.int8])->npt.NDArray[np.int8]:
        tasa_mutacion:float = 0.10
        tamano_carga:int = len(carga)
        posicion_mutacion:int = np.random.randint(0,tamano_carga) 
        probabilidades:npt.NDArray[np.float16] = np.random.uniform(0,1)

        if  probabilidades <= tasa_mutacion:
            if carga[posicion_mutacion] == 0:
                carga[posicion_mutacion] = 1
                return carga
            
            carga[posicion_mutacion] = 1
            return carga
        return carga