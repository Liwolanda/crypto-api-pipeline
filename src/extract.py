#%%
import pandas as pd
import logging as log
import requests
from config import *


# ----- funcoes


def extract_coins():

    listas_df = []
    
    try:

        for pagina in range (1, TOTAL_PAGES + 1):

            url = API_URL


            parametros = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": PER_PAGE,
            "page": pagina
}

            resposta = requests.get(
            url,
            params=parametros
    )

            dados = resposta.json()

            df_moedas = pd.DataFrame(dados)

            listas_df.append(df_moedas)

            print(f"{len(df_moedas)}")

    except Exception as e:
        log.error('Erro')
    
    
    df_final = pd.concat(
        listas_df,
        ignore_index=True
    )
    
    return df_final
# %%
