from carga import Carga
class Contenedor():
    def __init__(self,carga):
        self.carga = carga
        self.fitness = None

    def calcular_valor_peso(self) -> tuple[int,int,list[str]]:
        informacion: Carga = Carga()
        datos_carga:tuple[str, int, int]
        valor_carga:int = 0
        peso_carga:int = 0
        lista_productos: list[str] = []

        for posicion, producto in enumerate(self.carga):
            
            if producto == 0:
                continue
            datos_carga = informacion.informacion_carga(posicion=posicion)
            lista_productos.append(datos_carga[0])
            valor_carga += datos_carga[1]
            peso_carga += datos_carga[2]

        return valor_carga, peso_carga, lista_productos, self.carga 