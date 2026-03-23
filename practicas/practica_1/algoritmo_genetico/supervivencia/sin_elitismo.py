from supervivencia import Supervivencia
from cruze import Cruce_cargas, Cruce_un_punto
from torneo import Torneo
from mutacion import Mutacion, Seleccion_aleatoria
from contenedor import Contenedor
import numpy as np
import numpy.typing as npt


class Sin_elitismo(Supervivencia):

    def seleccion_supervivencia(self,
                                poblacion: list[Contenedor],
                                tamano_poblacion:int,
                                generacion:int,
                                max_generaciones:int,
                                recombinacion:Cruce_cargas,
                                mutacion:Mutacion)->tuple[list[Contenedor],Contenedor|None]:
                
        
        # # TODO: Verificar si hay solución
        # # Si hay solución termina el algoritmo, y retornar la solución
        # # De lo contrario continua con el proceso de evolución
        # for indice in range(0, len(aptitudes)):
        #     if aptitudes[indice] == 0:
        #         print("Existe una solucion en el tablero")
        #         print(f"Se encontro la solución en la generación {generacion}")
        #         return poblacion[indice]
            
        # Nueva generación
        nueva_poblacion: list[Contenedor] = []
        
        padre1: npt.NDArray[np.int8]
        padre2: npt.NDArray[np.int8]
        hijo1: npt.NDArray[np.int8]
        hijo2: npt.NDArray[np.int8]

        seleccion_cargas: Torneo = Torneo()
        cruzar_cargas: Cruce_cargas = recombinacion()
        mutacion_cargas: Mutacion = mutacion()
            
        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = seleccion_cargas.seleccionar_padres(poblacion=poblacion)
            hijo1, hijo2 = cruzar_cargas.cruce(padre1, padre2)

            if not generacion >= max_generaciones:

                hijo1 = mutacion_cargas.generar_mutacion(hijo1)
                hijo2 = mutacion_cargas.generar_mutacion(hijo2)

            # Construye a la nueva población con los hijos
            carga_hijo_1:Contenedor = Contenedor(carga=hijo1)
            carga_hijo_2:Contenedor = Contenedor(carga=hijo2) 
            nueva_poblacion.append(carga_hijo_1)
            nueva_poblacion.append(carga_hijo_2)
        
        return nueva_poblacion , None