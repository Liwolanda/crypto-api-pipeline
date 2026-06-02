#%%
import pandas as pd
from extract import extract_coins
from transform import transformar
from load import salvar_sql
from analytics import *
df = extract_coins()
df = transformar(df)
salvar_sql(
    df,
    tabela='moedas'
)

print(df)
# %%

top_10_moedas()

top_10_preco()

# %%
