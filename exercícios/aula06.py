import pandas as pd
import numpy as np

#Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({
    "Orcamento campanha": np.random.randint(1000, 5000, size=100)
})