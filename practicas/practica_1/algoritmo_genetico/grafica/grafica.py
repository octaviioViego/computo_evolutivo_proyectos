from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt

class Grafica(ABC):
    @abstractmethod
    def generar_grafica(self, datos: list[float], etiqueta: str = 'Sin etiqueta')-> None:
        pass