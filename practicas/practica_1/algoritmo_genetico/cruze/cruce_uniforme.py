from .cruce_cargas import Cruce_cargas
import numpy as np
import numpy.typing as npt

class Cruce_uniforme(Cruce_cargas):


    def cruce(self,carga_uno:npt.NDArray[np.int8],carga_dos:npt.NDArray[np.int8])-> tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]]:
        tamano_carga: int = len(carga_uno)
        carga_uno:npt.NDArray[np.int8] = carga_uno[0]
        carga_dos:npt.NDArray[np.int8] = carga_dos[0]

        carga_hijo_uno:npt.NDArray[np.int8] = np.random.randint(0,1,tamano_carga)
        carga_hijo_dos:npt.NDArray[np.int8] = np.random.randint(0,1,tamano_carga)
        numero_aleatorio:int = 0
        
        for posicion in range(tamano_carga):
            numero_aleatorio = np.random.randint(0,2)

            if numero_aleatorio == 1:
                carga_hijo_uno[posicion] = carga_uno[posicion] 
                carga_hijo_dos[posicion] = carga_dos[posicion]
                
            else:            
                carga_hijo_uno[posicion] = carga_dos[posicion] 
                carga_hijo_dos[posicion] = carga_uno[posicion]

        return carga_hijo_uno,carga_hijo_dos