from grafica import Grafica
import matplotlib.pyplot as plt

class Grafica_lineas(Grafica):

    def generar_grafica(self, datos: list[float], etiqueta: str = 'Sin etiqueta') -> None:
    
        tamano = len(datos)
        x = list(range(tamano)) 

        plt.figure() # Controla la figura y no deja que se ensucie.
        plt.plot(
            x,
            datos,
            label=etiqueta,
            color='black',
            linestyle=':',
            linewidth=1
        )

        plt.title(f'Valor {etiqueta} en las generaciones')
        plt.xlabel('Generación')
        plt.ylabel('Valor')

        plt.legend()
        plt.grid(True)
        plt.show()
