from penalizacion import *
from carga import * 
import numpy as np
import numpy.typing as npt

class Fitness():
    
    metodos_penalizacion: dict[str,Penalizacion] = {
            "fitnes_cero": Fitness_Cero,
            "lineal": Lineal,
            "cuadratica":Cuadratica,
            "exponencial":Exponencial,
        }

    def __init__(self,carga:npt.NDArray[np.int8]):
        self.carga:npt.NDArray[np.int8] = carga
        self.valor_total: int = 0
    
    def _calcular_valor_total(self)-> None:
         self.valor_total = 0
         carga = Carga()
         for posicion, objeto in enumerate(self.carga):
            if objeto == 1:
                nombre, valor , peso = carga.informacion_carga(posicion=posicion)
                self.valor_total += valor
    
    def calcular_fitness(self,penalizacion_selecionada:str = "fitnes_cero")-> int:
        self._calcular_valor_total()
        penalizacion: Penalizacion = self.metodos_penalizacion[penalizacion_selecionada]()
        penalizacion.calcular_peso_total(carga=self.carga)
        valor_penalizacion: int = penalizacion.calcular_aptitud()
        
        if penalizacion_selecionada == "fitnes_cero":
            if valor_penalizacion == 0:
                return 0

        return self.valor_total - valor_penalizacion
