import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
y = np.cos(4*x)

plt.plot(x, y)
plt.title('Grágico do Cosseno')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.show()