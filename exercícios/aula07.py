import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({
    "Orcamento campanha": np.random.randint(1000, 5000, size=100),
    "Visualizações_Anuncio": np.random.randint(2000, 20000, size= 100),
    "Vendas": np.random.randint(10, 1000, size=100),
    "Cliques": np.random.randint(100, 2000, size=100)
})

# Pairplot: Visualizar todas as relações 
sns.pairplot(dados)
plt.show()
plt.savefig('pairplot7.png')

#Joinplot: Explorar a relação entre duas variáveis específicas
sns.jointplot(x='Visualizações_Anuncio', y='Vendas', data=dados, kind="reg")
plt.show()
plt.savefig('joinplot7.png')

#Lmplot: Visualizar a linha de regressão
sns.lmplot(x='Visualizações_Anuncio', y='Vendas', data=dados)
plt.show()
plt.savefig('lmplot7.png')