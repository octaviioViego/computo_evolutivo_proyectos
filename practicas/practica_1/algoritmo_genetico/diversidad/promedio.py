"""
    - Clase que calcula el promedio de cada gen. Donde:
        - xij es el valor del gen i del individuo j
        - P es el tamaño de la población
        - n es el número de genes del individuo
"""
from contenedor import Contenedor

class Promedio():
    
    def calcular_promedio(poblacion:list[Contenedor]) -> list[float]:
        
        suma_genes: int
        tamano_poblacion:int = len(poblacion)
        lista_promedio: list[float] = []
        tamano_genes: int = len(poblacion[0].carga)

        for posicion in range(tamano_genes):
            suma_genes = 0

            for contenedor, _ in poblacion:
                suma_genes += contenedor[posicion]

            lista_promedio.append(suma_genes/tamano_poblacion)

        return lista_promedio
        