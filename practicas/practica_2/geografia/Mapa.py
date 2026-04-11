from geopy.distance import geodesic
from practicas.practica_2.geografia.Ciudad import Ciudad

class Mapa:
    """
    Gestiona la topología del problema. 
    Calcula y almacena la matriz de distancias para optimizar el rendimiento.
    """

    def __init__(self, lista_ciudades: list[Ciudad]):
        self.ciudades = lista_ciudades
        self.numero_ciudades = len(lista_ciudades)
    
        # Diccionario para mapear nombre de ciudad a su índice en la matriz
        self.indices = {ciudad.nombre: posicion for posicion, ciudad in enumerate(lista_ciudades)}
    
        # La matriz se calcula al instanciar el mapa
        self._matriz_distancias = self._precalcular_matriz()

    def _precalcular_matriz(self):
        """Genera una matriz de adyacencia con las distancias geodésicas."""
        matriz = [[0.0] * self.numero_ciudades for _ in range(self.numero_ciudades)]
        for i in range(self.numero_ciudades):
            for j in range(i + 1, self.numero_ciudades):
                distancia = geodesic(
                    (self.ciudades[i].coordenadas), 
                    (self.ciudades[j].coordenadas)
                ).kilometers
                
                # La matriz es simétrica (A->B es igual a B->A)
                matriz[i][j] = matriz[j][i] = distancia
        return matriz

    def obtener_distancia(self, idx_orig, idx_dest):
        """Acceso ultra-rápido a la matriz."""
        return self._matriz_distancias[idx_orig][idx_dest]

    def __len__(self):
        return self.numero_ciudades
    