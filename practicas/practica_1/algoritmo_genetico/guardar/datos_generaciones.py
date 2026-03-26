from .guardar import Guardar,pd


class DatosGeneraciones(Guardar):
    def __init__(self,
                 valor_maximo_generacion: list[int],
                 valor_minimo_generacion: list[int],
                 valor_promedio_generacion: list[float],
                 valor_desviacion_std_generacion: list[float],
                 valor_varianza_generacion: list[float],
                 valor_diversidad_generacion: list[float],
                 nombre_archivo="datos_generaciones"):
            
            self.valor_maximo_generacion = valor_maximo_generacion
            self.valor_minimo_generacion = valor_minimo_generacion
            self.valor_promedio_generacion = valor_promedio_generacion
            self.valor_desviacion_std_generacion = valor_desviacion_std_generacion
            self.valor_varianza_generacion = valor_varianza_generacion
            self.valor_diversidad_generacion = valor_diversidad_generacion
            self.nombre_archivo = nombre_archivo

    def guardar_CSV(self)->None:
        datos_generaciones = list(zip(
            self.valor_maximo_generacion,
            self.valor_minimo_generacion,
            self.valor_promedio_generacion,
            self.valor_desviacion_std_generacion,
            self.valor_varianza_generacion,
            self.valor_diversidad_generacion
        ))

        df = pd.DataFrame(datos_generaciones, columns=[
            'Fitness maximo',
            'Fitness minimo',
            'Promedio',
            'Desviación std',
            'Varianza',
            'Diversidad'
        ])

        df.to_csv(self.ruta_acceso + self.nombre_archivo + ".csv", index=True)

    