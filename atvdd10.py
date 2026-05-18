import pandas as pd

# 1. Carregamos a base original
df = pd.read_csv("produtos.csv")

# 2. Aplicamos o filtro (Atividade 7)
# Vamos pegar produtos com estoque < 60
df_reposicao = df[df["Estoque"] < 60]

# 3. Comando chave: .to_csv
# Isso cria um arquivo novo no seu computador com o resultado do filtro
df_reposicao.to_csv("reposicao_estoque.csv", index=False)

print("Arquivo 'reposicao_estoque.csv' gerado com sucesso!")