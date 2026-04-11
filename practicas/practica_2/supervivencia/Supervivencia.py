import numpy as np
import numpy.typing as npt
from abc import ABC, abstractmethod
from Individuo  import Individuo
from mutacion import Mutacion
from cruza import CruzaParcialmenteMapeada


class Supervivencia(ABC):
    """
    - Definimos los parametros de la supervivencia.
    - El regreso de -> tuple[list[Individuo],Individuo|None] es si usamos elitismo o no. 
        - Elitismo: Regresamos al mejor individuo de la población anterior  sustituyendo al peor de la población nueva.
        - Sin elitismo: Regresamos todos los individuos de la nueva poblacion. 
    """
    @abstractmethod
    def seleccion_supervivencia(poblacion: list[Individuo],
                                tamano_poblacion:int,
                                generacion:int,
                                max_generaciones:int,
                                recombinacion:CruzaParcialmenteMapeada,
                                tasa_mutacion:float,
                                mutacion:Mutacion) -> tuple[list[Individuo],Individuo|None]:
        