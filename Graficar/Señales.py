import matplotlib.pyplot as plt
import numpy as np

def Dibuja():
    #DEFINIMOS LOS PARAMETROS A DIBUJAR
    N = 50
    inicio = -8
    fin = 8
    Eje_X = np.linspace(inicio, fin, N, endpoint=True)
    Eje_Y = np.zeros(N)

    #USAMOS STEM PARA DIBUJAR DELTAS
    markerline, stemlines, baseline = plt.stem(Eje_X, np.cos((5*np.pi/4)*Eje_X), '-')

    #DEFINIMOS LA BASE DE LA RECTA CON EL COLOR Y SU GROSOR
    plt.setp(baseline, color='r', linewidth=1)

    #MOSTRAMOS LA GRAFICA
    plt.show()

if __name__ == "__main__":
    Dibuja()