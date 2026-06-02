#%%
import sqlite3
from pathlib import Path
import logging
from config import *

def salvar(df,caminho):

    try:
        Path(caminho).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(caminho,
                  index=False)
        

    except Exception as e:

        logging.error(f"erro{e}")


def salvar_sql (df, tabela):

    try:

        Path('../database').mkdir(
            exist_ok=True
        )

        conexao =sqlite3.connect(DATABASE_PATH)

        df.to_sql(
            tabela,
            conexao,
            if_exists='replace',
            index=False
        )


    finally:
        
        conexao.close()

# %%
