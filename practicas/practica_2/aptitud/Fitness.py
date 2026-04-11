from practicas.practica_2.geografia.Mapa import Mapa

class Fitnes():
    
    def calcular(ruta:list[int]) -> float:
        mapa:Mapa = Mapa() 
        size:int = len(ruta)
        distancia_total:float

        for pocision in range(size-1):
            distancia_total += mapa.obtener_distancia(idx_orig=pocision,idx_dest=pocision+1)
            
        # De la ciudad final a la CDMX (Ciudad inicial).
        distancia_total += mapa.obtener_distancia(idx_orig=ruta[size-1],idx_dest=0)
        
        # Minimizamos la distancia.
        distancia_total = 1/distancia_total
        
        return distancia_total 
