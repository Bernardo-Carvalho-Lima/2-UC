import pandas as pd

# Carregando os dados
df = pd.read_csv("produtos.csv")

# Comando chave: df["Coluna"].mean()
# Selecionamos a coluna entre aspas e colchetes e pedimos a média (.mean)
media_preco = df["Preco"].mean()

print(f"A média de preço dos produtos é: R$ {media_preco:.2f}")