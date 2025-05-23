import matplotlib.pyplot as plt
import pandas as pd

def exibirGrafico():
    df = pd.DataFrame({
        "area": [125, 150, 142, 138, 160, 500, 485, 520, 478, 492, 1500, 90, 105, 112, 2000],
        "preço": [110, 130, 125, 120, 140, 400, 380, 420, 390, 405, 1000, 95, 105, 115, 1200]
    })
    plt.scatter(df['area'], df['preço'])
    plt.title('Área (m²) x preço (R$ mil)')

    plt.xlabel('Área (m²)')
    plt.ylabel('preço (R$ mil)')

    plt.grid(True)
    plt.show()

    plt.savefig('chart5.png')

    # Removendo os outliers usando IQR
    Q1 = df[['area', 'preço']].quantile(0.25) # Primeiro quartil
    Q3 = df[['area', 'preço']].quantile(0.75) # Terceiro quartil
    IQR = Q3 - Q1

    # Filtra somente os dados mais próximos a mediana, excluíndo os outliers
    mask = ~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
    df_limpo = df[mask]

    plt.scatter(df_limpo['area'], df_limpo['preço'])
    plt.title('Área (m²) x preço (R$ mil)')

    plt.xlabel('Área (m²)')
    plt.ylabel('preço (R$ mil)')

    plt.grid(True)
    plt.show()

    plt.savefig('chart6.png')