import pandas as pd

dados = {
    'Fruta': ['Maçã', 'Banana', 'Laranja', 'Morango', 'Uva'],
    'Quantidade': [10, 15, 8, 20, 12],
    'Preco': [2.50, 1.20, 3.00, 5.50, 4.00]}

df = pd.DataFrame(dados)

print("--- Meu Primeiro DataFrame ---")
print(df)