import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
valores = [120, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

quartis = np.percentile(valores, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

plt.boxplot(valores, vert=False)
plt.title('valores e meses')
plt.xlabel('mes')
plt.show()
plt.savefig('chart8.png')