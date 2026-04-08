from abc import ABC, abstractmethod

class Cruza(ABC):
    """
    Clase base abstracta para los operadores de recombinación.
    """
    @abstractmethod
    def ejecutar(self, padre1:list[int], padre2:list[int])-> tuple[list[int],list[int]]:
        """
        - Retornamos dos hijos de ambos padres en forma de tupla.
        """
        pass