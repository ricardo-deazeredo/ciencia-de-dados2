#Faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
#Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt 

# Definição dos grupos e valores
mês = ['Janeiro','Fevereiro','Março',  'Abril', 'Maio']
faturamento = [25000 ,  28000, 22000,31000 , 27000]

# Configura um gráfico de barras, onde recebemos os grupos, valores
# E opcionalmente as cores 
plt.bar(mês, faturamento, color=['yellow', 'green', 'pink', 'black', 'orange'])

# Define o título do gráfico
plt.title('Gráfico de barras Faturamento')

# Define o título do eixo x
plt.xlabel('mês')

# Define o título do eixo y
plt.ylabel('faturamento')

#Cria o gráfico
plt.show()

#Salva dentro do arquivo de imagem
plt.savefig('chart.png')

