class Ciudad:
    """
    Representa una entidad geográfica en el problema del viajero (TSP).
    Esta clase actúa como un contenedor de datos inmutable.
    """

    def __init__(self,nombre:str,longitud:float,latitud:float):
        self.__nombre = nombre
        self.__longitud = longitud
        self.__latitud = latitud

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def coordenadas(self) -> tuple:
        return (self.__latitud,self.__longitud)

    def __repr__(self):
        return f"Nombre ciudad = {self.__nombre}, altitud = {self.__latitud}, longitud = {self.__longitud}."