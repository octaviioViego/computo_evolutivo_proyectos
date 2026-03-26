from .guardar import Guardar, pd
from cruze import Cruce_cargas
from mutacion import Mutacion
from supervivencia import Supervivencia

class AnalisisEstadistico(Guardar):
    def __init__(self,
                lista_configuraciones_totales: list[list[tuple[int,float,float,float,Cruce_cargas,Mutacion,str,Supervivencia]]],
                nombre_archivo="analisis_estadistico"):
            self.lista_configuraciones_totales = lista_configuraciones_totales
            self.nombre_archivo = nombre_archivo
    
    def guardar_CSV(self)->None:
        filas = []
    
        for configuracion in self.lista_configuraciones_totales:

            fitness_mej, valor_prom, valor_var, valor_des_std, conf_cruce, conf_mutacion, conf_penalizacion, conf_supervivencia = configuracion
                
            filas.append((fitness_mej, valor_prom, valor_var, 
                        valor_des_std, conf_cruce, conf_mutacion, 
                        conf_penalizacion, conf_supervivencia))  # convertir lista a string

        df = pd.DataFrame(filas, columns=[
            'Mayor fitness ',
            'Promedio',
            'Varianza',
            'Desviación estándar',
            'Cruce',
            'Mutación',
            'Penalización',
            'Supervivencia'
        ])

        df.to_csv(self.ruta_acceso + self.nombre_archivo + ".csv", index=False)    