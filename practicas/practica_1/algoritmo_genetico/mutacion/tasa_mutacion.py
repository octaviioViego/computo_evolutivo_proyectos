from mutacion import Mutacion
import numpy as np
import numpy.typing as npt

class Tasa_mutacion(Mutacion):
    def generar_mutacion(self,carga: npt.NDArray[np.int8])->npt.NDArray[np.int8]:
        for i in range(len(carga)):
            if np.random.random() <= 0.10:
                carga[i] = 1 - carga[i]
        return carga