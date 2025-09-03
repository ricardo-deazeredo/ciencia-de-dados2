import pandas as pd
import numpy as np

#Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({
    "Orcamento campanha": np.random.randint(1000, 5000, size=100),
    "Visualizacoes anuncio": np.random.randint(2000, 20000, size= 100),
    "Vendas": np.random.randint(10, 1000, size=100),
    "Cliques": np.random.randint(100, 2000, size=100)
})

print(dados.corr().round(4))