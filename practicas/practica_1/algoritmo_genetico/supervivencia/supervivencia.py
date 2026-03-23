from abc import ABC, abstractmethod
from contenedor  import Contenedor
import numpy as np
import numpy.typing as npt
from mutacion import Mutacion
from cruze import Cruce_cargas

class Supervivencia(ABC):
    @abstractmethod
    def seleccion_supervivencia(poblacion: list[Contenedor],
                                tamano_poblacion:int,
                                generacion:int,
                                max_generaciones:int,
                                recombinacion:Cruce_cargas,
                                mutacion:Mutacion) -> tuple[list[Contenedor],Contenedor|None]:
        pass