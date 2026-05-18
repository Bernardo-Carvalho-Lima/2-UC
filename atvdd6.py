import pandas as pd

# Carregando os dados
df = pd.read_csv("produtos.csv")

# 1. Comando chave: .max() 
# Encontra o maior valor da coluna selecionada
preco_maximo = df["Preco"].max()

# 2. Comando chave: .min()
# Encontra o menor valor da coluna selecionada
preco_minimo = df["Preco"].min()

print(f"O produto mais caro custa: R$ {preco_maximo}")
print(f"O produto mais barato custa: R$ {preco_minimo}")