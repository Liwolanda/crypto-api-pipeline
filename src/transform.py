import pandas as pd
import logging
import json

def transformar(df):
    
    try: 
        
        logging.info('Iniciando transformacao')
        logging.info(f'Linhas antes: {len(df)}')

        # ----- validacao

        print(df.isnull().sum())

        linhas_antes = len(df)
        
        df = df.dropna()

        linhas_removidas = linhas_antes - len(df)

        logging.info(f"linhas removidas: {linhas_removidas}")
        
        print(df.shape)
        
        colunas = ['ath_date', 'atl_date', 'last_updated']

        df[colunas] = df[colunas].apply(
            pd.to_datetime,
            errors='coerce'
        )

        df['roi'] = df['roi'].apply(
        lambda x: json.dumps(x) if isinstance(x, dict) else None
        )

        logging.info(f'Linhas depois: {len(df)}')

    except Exception as e:

        logging.error(f"Erro {e}")

    return df
        