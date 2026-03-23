"""
    - Se calcula la diversidad de la población usando varianza. 
"""

from .promedio import Promedio
from .varianza import Varianza
from contenedor import Contenedor
import numpy as np

class Diversidad():
    
    def calcular_diversidad(self,poblacion:list[Contenedor])->float:
        tamano_genes: int = len(poblacion[0].carga)
        promedio_gen = Promedio()
        varianza_gen = Varianza()

        promedios: float = promedio_gen.calcular_promedio(poblacion=poblacion)
        varianzas: float = varianza_gen.calcular_varianza(poblacion=poblacion,lista_promedio=promedios)

        return np.sum(varianzas)/tamano_genes
        