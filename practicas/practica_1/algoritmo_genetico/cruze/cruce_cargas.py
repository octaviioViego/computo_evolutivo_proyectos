from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt
from contenedor import Contenedor
class Cruce_cargas(ABC):
    
    @abstractmethod
    def cruce(carga_uno:Contenedor,carga_dos:Contenedor)-> tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]]:
        pass 