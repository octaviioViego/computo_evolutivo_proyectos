from abc import ABC, abstractmethod

class Mutacion(ABC):

    @abstractmethod
    def mutacion(self, individuo:list[int], tasa_mutacion:int)-> list[int]:
        """
        Si se aplica la mutación a un individuo será de:
        - Tasa de mutación:
            - 5%
            - 10%
            - 20%
        - Retornamos al individio con alguna mutación.
        """
        pass