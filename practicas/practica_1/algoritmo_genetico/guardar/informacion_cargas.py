from .guardar import Guardar,pd

class InformacionCargas(Guardar):
    def __init__(self,
                 lista_informacion_cargas: list[list[tuple[int,int,list[str],list[int]]]],
                 nombre_archivo="datos_cargas"):
            self.lista_informacion_cargas = lista_informacion_cargas
            self.nombre_archivo = nombre_archivo
            self.nombre_archivo = nombre_archivo

    def guardar_CSV(self)->None:
        filas = []

        for configuracion in self.lista_informacion_cargas:
            for valor, peso, productos, carga in configuracion:
                filas.append((valor, peso, ", ".join(productos), carga))  # convertir lista a string

        df = pd.DataFrame(filas, columns=[
            'Valor carga',
            'Peso carga',
            'Lista de productos',
            'Carga'
        ])

        df.to_csv(self.ruta_acceso + self.nombre_archivo + ".csv", index=False)    

    