from grafica import Grafica
import matplotlib.pyplot as plt

class Grafica_lineas_dobles(Grafica):

    def generar_grafica(self, datos: list[list[float]], etiqueta: str = 'Sin etiqueta') -> None:
        
        tamano = len(datos[0])
        x = list(range(tamano)) 
        
        dato_uno = datos[0]  # fitness
        dato_dos = datos[1]  # diversidad

        fig, ax1 = plt.subplots()

        # --- FITNESS ---
        ax1.set_xlabel('Generación')
        ax1.set_ylabel('Fitness')

        ax1.plot(
            x,
            dato_uno,
            label='Fitness',
            linestyle=':',
            linewidth=1
        )

        # --- DIVERSIDAD ---
        ax2 = ax1.twinx()
        ax2.set_ylabel('Diversidad')

        ax2.plot(
            x,
            dato_dos,
            label='Diversidad',
            linestyle='--',
            linewidth=1
        )

        # Leyendas separadas
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        plt.title(f'Evolución del Fitness vs Diversidad')
        plt.grid(True)
        plt.show()