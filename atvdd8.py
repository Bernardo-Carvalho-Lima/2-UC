import pandas as pd

# Carregando os dados
df = pd.read_csv("produtos.csv")

# Comando chave adaptado: df["Nova_Coluna"] = Cálculo
# No seu caso da academia: df["IMC"] = df["Peso"] / (df["Altura"] ** 2)
df["Valor_Total_Estoque"] = df["Preco"] * df["Estoque"]

print("--- Tabela com a Nova Coluna ---")
print(df)

