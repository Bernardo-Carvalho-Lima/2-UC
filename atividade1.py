<<<<<<< HEAD
import pandas as pd

dados = {
    'Fruta': ['Maçã', 'Banana', 'Laranja', 'Morango', 'Uva'],
    'Quantidade': [10, 15, 8, 20, 12],
    'Preco': [2.50, 1.20, 3.00, 5.50, 4.00]}

df = pd.DataFrame(dados)

print("--- Meu Primeiro DataFrame ---")
print(df)

#atividade 2
import pandas as pd

df_produtos = pd.read_csv("produtos.csv")

print("--- Dados Carregados do Arquivo CSV ---")
print(df_produtos)

print("\n--- Resumo das primeiras linhas ---")
print(df_produtos.head(2))
=======
import pandas as pd

dados = {
    'Fruta': ['Maçã', 'Banana', 'Laranja', 'Morango', 'Uva'],
    'Quantidade': [10, 15, 8, 20, 12],
    'Preco': [2.50, 1.20, 3.00, 5.50, 4.00]}

df = pd.DataFrame(dados)

print("--- Meu Primeiro DataFrame ---")
print(df)
>>>>>>> 3511cbb10a23666f1dd1a4db34ffd00c65c74467
