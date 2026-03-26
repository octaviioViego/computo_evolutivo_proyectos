from .guardar import Guardar, pd
from cruze import Cruce_cargas
from mutacion import Mutacion
from supervivencia import Supervivencia


class Configuracion(Guardar):
    
    def __init__(self,
                 configuraciones_posibles:list[list[Cruce_cargas,Mutacion,str,Supervivencia]],
                 nombre_archivo="datos_configuraciones"):
                self.configuraciones_posibles = configuraciones_posibles
                self,nombre_archivo = nombre_archivo

    def guardar_CSV(self)-> None:
        pf:pd.DataFrame = pd.DataFrame(self.configuraciones_posibles,columns=['Cruce','Mutacion',
                                                                     'Penalizacion','Supervivencia'])
        pf.to_csv(self.ruta_acceso+self.nombre_archivo+".csv",index=True)