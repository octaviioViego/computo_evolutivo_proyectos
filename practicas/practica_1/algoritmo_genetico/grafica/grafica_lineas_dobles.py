from grafica import Grafica
import matplotlib.pyplot as plt

class Grafica_lineas_dobles(Grafica):

    def generar_grafica(self, datos: tuple[list[float],list[float]], 
                        etiqueta_general: str = 'Sin etiqueta',
                        etiqueta_uno:str = 'Sin etiqueta',
                        etiqueta_dos:str = 'Sin etiqueta') -> None:
        
        
        tamano = len(datos[0])
        x = list(range(tamano)) 
        datos_uno: list[float] = datos[0]
        datos_dos: list[float] = datos[1]

        plt.figure() # Controla la figura y no deja que se ensucie.

        # Crear las dos líneas en el mismo gráfico
        plt.plot(x, datos_uno, label=etiqueta_uno, color='blue', linestyle='-', marker='.')
        plt.plot(x, datos_dos, label=etiqueta_dos, color='red', linestyle='--', marker='.')



        plt.title(f'Valor {etiqueta_general} en las generaciones')
        plt.xlabel('Generación')
        plt.ylabel('Valor')

        plt.legend()
        plt.grid(True)
        plt.show()
