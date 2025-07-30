import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# conjunto de dados exemplo
dados = [10, 20, 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]

# Calcular quartis
quartis = np.percentile(dados, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

# Calcular decis
decis = np.percentile(dados, [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f'Decis: {decis}')

# Calcular percentis
percentis = np.percentile(dados, [10, 25, 50, 75, 90])
print(f'Percentis: {percentis}')

# Visualização por BoxPlot
plt.boxplot(dados, vert=False)
plt.title('Boxplot das notas')
plt.xlabel('Notas')
plt.show()
plt.savefig('chart7.png')
