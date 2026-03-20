from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt

class Mutacion(ABC):
    @abstractmethod
    def generar_mutacion(carga: npt.NDArray[np.int8])->npt.NDArray[np.int8]:
        pass