import pandas as pd

df_produtos = pd.read_csv("produtos.csv")

print("--- Dados Carregados do Arquivo CSV ---")
print(df_produtos)

print("\n--- Resumo das primeiras linhas ---")
print(df_produtos.head(2))