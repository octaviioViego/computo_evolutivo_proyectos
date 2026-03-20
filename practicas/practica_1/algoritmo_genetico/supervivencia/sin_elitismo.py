from supervivencia import Supervivencia
from fitness import Fitness
from cruze import Cruce_cargas, Cruce_un_punto
from torneo import Torneo
from mutacion import Mutacion, Seleccion_aleatoria
import numpy as np
import numpy.typing as npt


class Sin_elitismo(Supervivencia):

    def seleccion_supervivencia(self,
                                poblacion: npt.NDArray[np.int8],
                                tamano_poblacion,
                                generacion,
                                max_generaciones):
                
        # TODO: Calcular aptitudes de toda la población para verificar si ya hay una solución
        aptitudes: list[np.int_] = []
        fitness: Fitness 
        
        for individuo in poblacion:
            fitness = Fitness(individuo)
            aptitudes.append(fitness.calcular_fitness())

        valor_maximo: int = (np.max(aptitudes))
        valor_minimo: int = (np.min(aptitudes))
        valor_promedio: float = (np.mean(aptitudes))
        
        # # TODO: Verificar si hay solución
        # # Si hay solución termina el algoritmo, y retornar la solución
        # # De lo contrario continua con el proceso de evolución
        # for indice in range(0, len(aptitudes)):
        #     if aptitudes[indice] == 0:
        #         print("Existe una solucion en el tablero")
        #         print(f"Se encontro la solución en la generación {generacion}")
        #         return poblacion[indice]
            
        # Nueva generación
        
        nueva_poblacion: list[npt.NDArray[np.int8]] = []
        poblacion_fitness: list[tuple[list[int], float]] = []

        padre1: npt.NDArray[np.int8]
        padre2: npt.NDArray[np.int8]
        hijo1: npt.NDArray[np.int8]
        hijo2: npt.NDArray[np.int8]

        seleccion_cargas: Torneo = Torneo()
        cruzar_cargas: Cruce_cargas = Cruce_un_punto()
        mutacion_cargas: Mutacion = Seleccion_aleatoria()
            
        for posicion in range(0,len(poblacion)):
            poblacion_fitness.append((poblacion[posicion],aptitudes[posicion]))

        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = seleccion_cargas.seleccionar_padres(poblacion=poblacion_fitness)
            hijo1, hijo2 = cruzar_cargas.cruce(padre1, padre2)

            if not generacion >= max_generaciones:

                hijo1 = mutacion_cargas.generar_mutacion(hijo1)
                hijo2 = mutacion_cargas.generar_mutacion(hijo2)

            # Construye a la nueva población con los hijos
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)

            # Sustituye a la población completa de padres por los hijos
            poblacion = np.array(nueva_poblacion, dtype=np.int8)
        
        return poblacion, valor_maximo, valor_minimo, valor_promedio