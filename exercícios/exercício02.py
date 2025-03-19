#Faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
#Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt 

# Definição dos grupos e valores
aluno = ['Amanda','Caio','Carla',  'Diego', 'Fernanda']
nota = [85 , 60 , 90, 75, 55]

# Configura um gráfico de barras, onde recebemos os grupos, valores
# E opcionalmente as cores 
plt.bar(aluno, nota, color=['yellow', 'green', 'pink', 'black', 'orange'])

# Define o título do gráfico
plt.title('Gráfico de barras Notas')

# Define o título do eixo x
plt.xlabel('aluno')

# Define o título do eixo y
plt.ylabel('nota')

#Cria o gráfico
plt.show()

#Salva dentro do arquivo de imagem
plt.savefig('chart.png')

