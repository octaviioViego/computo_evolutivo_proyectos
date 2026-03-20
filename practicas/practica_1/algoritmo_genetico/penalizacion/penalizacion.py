from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt
from carga import Carga
class Penalizacion(ABC):

    def __init__(self, peso_maximo:int=50):
        self.peso_maximo = peso_maximo
        self.peso_total = 0

    def calcular_peso_total(self,carga: npt.NDArray[np.int8]) -> None:
        self.peso_total = 0

        for posicion, objeto in enumerate(carga):
            if objeto == 1:
                carga = Carga()
                nombre,valor,peso = carga.informacion_carga(posicion=posicion)
                self.peso_total +=  peso
      #  print(f"Peso total {self.peso_total}")

    @abstractmethod
    def calcular_aptitud(self)->int:
        pass