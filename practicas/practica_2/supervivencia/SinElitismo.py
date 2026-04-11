from Supervivencia import Supervivencia,np,npt
from Individuo  import Individuo
from mutacion import Mutacion
from cruza import CruzaParcialmenteMapeada,Cruza
from torneo import Torneo


class Sin_Elitismo(Supervivencia):
    def seleccion_supervivencia(poblacion: list[Individuo],
                                tamano_poblacion:int,
                                generacion:int,
                                max_generaciones:int,
                                recombinacion:CruzaParcialmenteMapeada,
                                tasa_mutacion:float,
                                mutacion:Mutacion) -> tuple[list[Individuo],Individuo|None]:

        _poblacion_nueva: list[int] = poblacion
        
        # Creamos los objetos necesarios
        _cruza:Cruza = recombinacion()
        _mutacion:Mutacion = mutacion()
        _seleccion:Torneo = Torneo()

        _padre1: npt.NDArray[np.int8]
        _padre2: npt.NDArray[np.int8]
        _hijo1: npt.NDArray[np.int8]
        _hijo2: npt.NDArray[np.int8]

        for _ in range(tamano_poblacion // 2):
            _padre1, _padre2 =_seleccion.seleccionar_padres(poblacion=poblacion)
            
            _hijo1, _hijo2 = _cruza.ejecutar(_padre1, _padre2)

            if not generacion >= max_generaciones:

                _hijo1 = _mutacion.mutar(individuo=_hijo1,tasa_mutacion=tasa_mutacion)
                _hijo2 = _mutacion.mutar(individuo=_hijo2,tasa_mutacion=tasa_mutacion)
                
            # Construye a la nueva población con los hijos
            carga_hijo_1:Individuo = Individuo(ruta=_hijo1)
            carga_hijo_2:Individuo = Individuo(ruta=_hijo2)

            _poblacion_nueva.append(carga_hijo_1)
            _poblacion_nueva.append(carga_hijo_2)
        
        return _poblacion_nueva , None
