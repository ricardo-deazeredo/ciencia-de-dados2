import numpy as np
from scipy import stats

# Nota de matemática
notas = [78, 85, 91, 73, 88, 92, 79, 85, 90, 87]

# Calcular a média

media = np.mean(notas)
print(f'media: {media}')

# Calcular a mediana

mediana = np.median(notas)
print(f'mediana: {mediana}')

# Calcular a moda

moda = stats.mode(notas, keepdims=True)
print(f'moda: {moda.mode[0]}, frequência: {moda.count[0]}')