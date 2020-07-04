# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import csv
file_name = "raw_database.xlsx"

# %%
df3 = pd.read_excel(file_name, usecols=("A,C,E,G,H,J,K,L,M,N"), sheet_name=2)

# %%
print(df3.columns)

# %%
df3.columns = ["Protocolo", "Data Finalização", "Fornecedor", "UF do Consumidor", "Cidade do Consumidor", 
              "Relato do Consumidor", "Resposta do Fornecedor", "Texto da Avaliação", 
              "Indicador de solução", "Nota"]


# %%
print(df3.info())


# %%
df3["Fornecedor"]= df3["Fornecedor"].astype('category')
df3["UF do Consumidor"]= df3["UF do Consumidor"].astype('category')
df3["Cidade do Consumidor"]= df3["Cidade do Consumidor"].astype('category')
df3["Indicador de solução"] = df3["Indicador de solução"].astype('category')
df3["Data Finalização"] = pd.to_datetime(df3["Data Finalização"], format='%d/%m/%Y %H:%M:%S')


# %%
print(df3.dtypes)
print(df3["Data Finalização"]_

ano_2020 = (df3["Data Finalização"].between('2020-01-01 00:00:01', '2020-12-31 23:59:59'))
ano_2019 = (df3["Data Finalização"].between('2019-01-01 00:00:01', '2019-12-31 23:59:59'))


# %%
df3[ano_2020 & ano_2019]
#df3[~ano_2019]


# %%
df_2019=df3[ano_2019]
df_2020=df3[ano_2020]


# %%
len(df_2019)


# %%
len(df_2020)


# %%
len(df_2019) + len(df_2020)


# %%
df_2020


# %%
len(df3)


# %%
df_2019.to_excel("2019.xlsx", encoding = "utf-8", index=False)


# %%
df_2020.to_excel("2020.xlsx", encoding = "utf-8", index=False)


# %%


