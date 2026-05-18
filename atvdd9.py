import pandas as pd

# Carregando os dados
df = pd.read_csv("produtos.csv")

# Comando chave: .value_counts()
# Ele conta quantas vezes cada item aparece na coluna selecionada
contagem_produtos = df["Produto"].value_counts()

print("--- Contagem por Produto ---")
print(contagem_produtos)