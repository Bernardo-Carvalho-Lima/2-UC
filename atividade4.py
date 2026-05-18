<<<<<<< HEAD
import pandas as pd

# Carregando nossos dados (usando a base de produtos que já temos)
df = pd.read_csv("produtos.csv")

# Comando chave: .describe()
# Ele faz um "check-up" geral de todos os números da tabela
resumo = df.describe()

print("--- Resumo Estatístico da Tabela ---")
=======
import pandas as pd

# Carregando nossos dados (usando a base de produtos que já temos)
df = pd.read_csv("produtos.csv")

# Comando chave: .describe()
# Ele faz um "check-up" geral de todos os números da tabela
resumo = df.describe()

print("--- Resumo Estatístico da Tabela ---")
>>>>>>> 3511cbb10a23666f1dd1a4db34ffd00c65c74467
print(resumo)