from abc import ABC, abstractmethod
import pandas as pd
class Guardar(ABC):
    ruta_acceso:str = "/home/oarroyo/computo_evolutivo_proyectos/datos_experimentos/archivos_configuraciones/"
    @abstractmethod
    def guardar_CSV(self)-> None:
        pass 