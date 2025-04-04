#Faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
#Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt 

# Definição dos grupos e valores
grupos = ['São Paulo','Rio de janeiro','Belo Horizonte',  'Porto Alegre', 'Curitiba']
valores = [12300 , 6700 , 2800, 1500, 1940]

# Configura um gráfico de barras, onde recebemos os grupos, valores
# E opcionalmente as cores 
plt.bar(grupos, valores, color=['yellow', 'green', 'pink', 'black', 'orange'])

# Define o título do gráfico
plt.title('Gráfico de barras simples')

# Define o título do eixo x
plt.xlabel('Grupos')

# Define o título do eixo y
plt.ylabel('Valores')

#Cria o gráfico
plt.show()

#Salva dentro do arquivo de imagem
plt.savefig('chart.png')

