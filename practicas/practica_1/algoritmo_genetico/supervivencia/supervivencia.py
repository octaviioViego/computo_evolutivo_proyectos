from abc import ABC, abstractmethod
from contenedor  import Contenedor
import numpy as np
import numpy.typing as npt

class Supervivencia(ABC):
    @abstractmethod
    def seleccion_supervivencia(poblacion: list[Contenedor],
                                tamano_poblacion,
                                generacion,
                                max_generaciones):
        pass