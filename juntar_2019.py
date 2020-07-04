import pandas as pd
import numpy as np

file1 = "../2019_p1.xlsx"
file2 = "../2019_p2.xlsx"

df1 = pd.read_excel(file1)
print(df1)
print("tamanho de df1", len(df1))

df2 = pd.read_excel(file2)
print(df2)
print("tamanho de df2", len(df2))

df = pd.concat([df1,df2])
print(df)
print("df1 + df2): ", len(df1)+len(df2))

df.to_excel("../2019.xlsx", encoding = "utf-8", index=False)


