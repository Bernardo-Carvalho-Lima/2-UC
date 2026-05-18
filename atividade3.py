<<<<<<< HEAD
import pandas as pd

# 1. Este bloco garante que o arquivo tenha conteúdo
conteudo = """Produto,Preco,Estoque
Mouse,50.00,100
Teclado,120.00,50
Monitor,850.00,20"""

with open("produtos.csv", "w") as arquivo:
    arquivo.write(conteudo)

# 2. Agora sim, lemos o arquivo que acabamos de preencher
df = pd.read_csv("produtos.csv")

# 3. Atividade 3: Inspeção de Dados
print("--- As 3 primeiras linhas ---")
print(df.head(3))

print("\n--- Nome das colunas ---")
=======
import pandas as pd

# 1. Este bloco garante que o arquivo tenha conteúdo
conteudo = """Produto,Preco,Estoque
Mouse,50.00,100
Teclado,120.00,50
Monitor,850.00,20"""

with open("produtos.csv", "w") as arquivo:
    arquivo.write(conteudo)

# 2. Agora sim, lemos o arquivo que acabamos de preencher
df = pd.read_csv("produtos.csv")

# 3. Atividade 3: Inspeção de Dados
print("--- As 3 primeiras linhas ---")
print(df.head(3))

print("\n--- Nome das colunas ---")
>>>>>>> 3511cbb10a23666f1dd1a4db34ffd00c65c74467
print(df.columns)