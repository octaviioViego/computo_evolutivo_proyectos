import numpy as np
import numpy.typing as npt
from .cruce_cargas import Cruce_cargas

class Cruce_dos_punto(Cruce_cargas):
    def cruce(self,carga_uno:npt.NDArray[np.int8],carga_dos:npt.NDArray[np.int8])-> tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]]:
        tamano_carga: int = len(carga_uno) 
        punto_cruce: int = tamano_carga//3
        carga_uno:npt.NDArray[np.int8] = carga_uno[0]
        carga_dos:npt.NDArray[np.int8] = carga_dos[0]


        carga_hijo_uno:npt.NDArray[np.int8] = np.concatenate((carga_uno[:punto_cruce],carga_dos[punto_cruce:-punto_cruce],carga_uno[-punto_cruce:]))
        carga_hijo_dos:npt.NDArray[np.int8] = np.concatenate((carga_dos[:punto_cruce],carga_uno[punto_cruce:-punto_cruce],carga_dos[-punto_cruce:]))

        return carga_hijo_uno,carga_hijo_dos