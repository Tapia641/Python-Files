import matplotlib.pyplot as plt
import numpy as np

#DEFINI
x = np.linspace(0, 1 * np.pi, 10)
markerline, stemlines, baseline = plt.stem(x, np.sin((np.pi/2)*x), '-')

#DEFINIMOS LA BASE DE LA RECTA CON EL COLOR Y SU GROSOR
plt.setp(baseline, color='r', linewidth=1)

#MOSTRAMOS LA GRAFICA
plt.show()