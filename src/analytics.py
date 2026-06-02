#%%

import sqlite3
import pandas as pd
import logging



def top_10_moedas():

    try:

        # ----- funcao sqlite3
    
        conexao = sqlite3.connect('../database/banco.db')

        top = pd.read_sql(
            """SELECT
                    name,
                    symbol,
                    market_cap
                FROM moedas
                ORDER BY market_cap DESC
                LIMIT 10
                """,
                conexao
        )

    finally:

        conexao.close()

    return top


def top_10_preco():

    try:

        conexao2 = sqlite3.connect('../database/banco.db')

        logging.info('banco conectado')
        
        top_preco = pd.read_sql(
            """SELECT
                    name,
                    symbol,
                    current_price
                FROM moedas
                ORDER BY current_price DESC
                LIMIT 10;
            """,
            conexao2
        )


    finally:

        conexao2.close()

    return top_preco
# %%
