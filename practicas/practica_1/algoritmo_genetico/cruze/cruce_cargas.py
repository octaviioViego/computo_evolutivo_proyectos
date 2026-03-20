from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt

class Cruce_cargas(ABC):
    
    @abstractmethod
    def cruce(carga_uno:npt.NDArray[np.int8],carga_dos:npt.NDArray[np.int8])-> tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]]:
        pass 