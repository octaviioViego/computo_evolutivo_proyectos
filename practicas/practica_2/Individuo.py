class Individuo():

    """
    Representa una solución potencial en la población.
    """

    def __init__(self,ruta:list[int],fitness: float = 0.0):
        self.cromosoma = ruta
        self.fitness = fitness
        