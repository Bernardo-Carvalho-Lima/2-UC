import pandas as pd

# Comando chave: pd.read_csv
# Ele "lê" o arquivo externo e transforma em uma tabela do Pandas (DataFrame)
df_produtos = pd.read_csv("produtos.csv")

# Exibindo os dados que foram carregados
print("--- Dados Carregados do Arquivo CSV ---")
print(df_produtos)

# Dica extra: Ver apenas as primeiras linhas (útil para arquivos gigantes)
print("\n--- Resumo das primeiras linhas ---")
print(df_produtos.head(2))