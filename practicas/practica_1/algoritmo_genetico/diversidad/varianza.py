"""
    - Se calcula la varianza en cada gen usando el promedio.
"""
from contenedor import Contenedor

class Varianza():

    def calcular_varianza(self,lista_promedio: list[float], poblacion:list[Contenedor])->list[float]:
        suma_promedio_gen: float
        tamano_poblacion: int = len(poblacion)
        tamano_genes: int = len(poblacion[0].carga)
        lista_varianza: list[float] = []

        for posicion in range(tamano_genes):
            suma_promedio_gen = 0

            for contenedor in poblacion:
                suma_promedio_gen += (contenedor.carga[posicion]-lista_promedio[posicion]) ** 2   
            
            lista_varianza.append(suma_promedio_gen/tamano_poblacion)
            
        return lista_varianza
    