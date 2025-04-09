import matplotlib.pyplot as plt
import pandas as pd

#Organiza os dados
df = pd.DataFrame({
    "times": ['Grêmio', 'Inter', 'Juventude'],
    "pontos": [30, 1, 10]
})
plt.bar(df['times'], df['pontos'], color=['orange', 'red', 'yellow'])

plt.title('Pontos de times')
plt.xlabel('Times')
plt.ylabel('Pontos')

plt.show()
plt.savefig('chart4.png')