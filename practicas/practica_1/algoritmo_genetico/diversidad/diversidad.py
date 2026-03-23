"""
    - Se calcula la diversidad de la población usando varianza. 
"""

from promedio import Promedio
from varianza import Varianza
from contenedor import Contenedor
import numpy as np

class Diversidad():
    
    def calcular_diversidad(poblacion:list[Contenedor])->float:
        tamano_genes: int = len(poblacion[0].carga)
        promedio_gen = Promedio()
        varianza_gen = Varianza()

        promedios: float = promedio_gen.calcular_promedio(poblacion=poblacion)
        varianzas: float = varianza_gen.calcular_varianza(poblacion=poblacion,promedio=promedios)

        return np.suma(varianzas)/tamano_genes
        