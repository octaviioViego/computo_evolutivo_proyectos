import numpy as np
import numpy.typing as npt
from contenedor import Contenedor

class Carga():

    """
        - Generamos carga de manera aleatoria de 100 cargas diferentes.
    """
    def generar_carga(self):

        carga: npt.NDArray[np.int8] = np.random.randint(0,2,(100,30))
        return carga

    """
        - Obtener información de las direfentes objetos de las cargas.
    """
    def informacion_carga(self,posicion:int)->tuple[str, int, int]:

        objetos:list[tuple[str, int, int]] = [
                    ('Botella de agua', 30, 6),
                    ('Comida deshidratada', 40, 8),
                    ('Botiquı́n de primeros auxilios', 50, 10),
                    ('Linterna LED', 28, 4),
                    ('Baterı́as recargables', 14, 2),
                    ('Cuchillo multiusos', 30, 5),
                    ('Mapa topográfico', 15, 3),
                    ('Brújula profesional', 16, 3),
                    ('Tienda de campaña ultraligera', 70, 14),
                    ('Saco de dormir térmico', 65, 13),
                    ('Colchoneta inflable', 30, 6),
                    ('Chamarra impermeable', 40, 9),
                    ('Guantes térmicos', 15, 3),
                    ('Filtro portátil de agua', 35, 5),
                    ('Cuerda de escalada', 50, 12),
                    ('Mosquetones de acero', 22, 5),
                    ('Estufa portátil', 36, 8),
                    ('Cartucho de gas', 20, 4),
                    ('Kit de reparación', 18, 4),
                    ('Radio de emergencia', 45, 9),
                    ('Panel solar portátil', 65, 12),
                    ('GPS de montaña', 42, 6),
                    ('Cámara compacta', 40, 6),
                    ('Cuaderno impermeable', 10, 2),
                    ('Teléfono satelital', 40, 5),
                    ('Laptop ultraligera', 110, 15),
                    ('Power bank alta capacidad', 28, 4),
                    ('Raciones energéticas', 28, 5),
                    ('Manta térmica', 12, 2),
                    ('Silbato de emergencia', 10, 2)
                ]
        return objetos[posicion]

    def calcular_valor_peso(self, contenedor:Contenedor) -> tuple[int,int,list[str]]:
        carga:list[int] = contenedor.carga
        datos_carga:tuple[str, int, int]
        valor_carga:int = 0
        peso_carga:int = 0
        lista_productos: list[str] = []

        for posicion, producto in enumerate(carga):
            
            if producto == 0:
                continue
            datos_carga = self.informacion_carga(posicion=posicion)
            lista_productos.append(datos_carga[0])
            valor_carga += datos_carga[1]
            peso_carga += datos_carga[2]

        return valor_carga, peso_carga, lista_productos 
