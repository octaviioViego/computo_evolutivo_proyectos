import random

class Poblacion:
    """
    Maneja la generación de rutas asegurando que el punto de partida 
    (Ciudad de México) permanezca fijo en la posición 0.
    """
    def __init__(self, tamano_poblacion: int = 50, 
                       num_ciudades: int = 20):
        
        # Guardamos la referencia de las ciudades restantes (sin la 0)
        self.__ciudades_restantes = list(range(1, num_ciudades))
        self.individuos = self._generar_poblacion(tamano_poblacion)

    def _generar_poblacion(self, tamano_poblacion: int):
        poblacion = []
        
        for _ in range(tamano_poblacion):
            # 1. Tomamos las ciudades del 1 al 19 y las desordenamos
            ruta_variable = random.sample(self.__ciudades_restantes, len(self.__ciudades_restantes))
            
            # 2. Insertamos siempre el índice 0 al inicio
            ruta_completa = [0] + ruta_variable
            
            poblacion.append(ruta_completa)
        
        return poblacion

    def __repr__(self):
        return f"Poblacion(total={len(self.individuos)}, cd_inicio=0)"