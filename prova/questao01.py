#Faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
#Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt 

# Definição dos grupos e valores
grupos = ['Norte','Nordeste','Centro-Oeste',  'Sudeste', 'Sul']
valores = [150000, 200000, 8000, 300000, 120000]

# Configura um gráfico de barras, onde recebemos os grupos, valores
# E opcionalmente as cores 
plt.bar(grupos, valores, color=['green', 'orange', 'blue', 'red', 'purple'])

# Define o título do gráfico
plt.title('Gráfico de casos de covid por região')

# Define o título do eixo x
plt.xlabel('Grupos')

# Define o título do eixo y
plt.ylabel('Valores')

#Cria o gráfico
plt.show()

#Salva dentro do arquivo de imagem
plt.savefig('chart.png')

