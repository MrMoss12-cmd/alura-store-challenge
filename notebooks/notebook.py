# Verificar las versiones de las bibliotecas instaladas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {plt.__version__}")

# Crear un gráfico de prueba
plt.figure(figsize=(8, 4))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Gráfico de prueba')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()