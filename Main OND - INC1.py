#!/usr/bin/env python
# coding: utf-8

# 
# 

# In[ ]:


# Tabelas disponíveis

    # BALANÇO DE ENERGIA ACUMULADA DIÁRIA
        df_BEA_D

    # PRODUÇÃO DE ENERGIA POR TIPO
        # Hidráulica
        df_prodh_rg - produção diária por região + itaipu
        df_poth_rg - potencia diária por região + itaipu
        df_prodh_usina - produção e potencia diária por usina + itaipu
        # Térmica
        df_prodt_rg - produção diária por região
        df_pott_rg - potencia diária por região
        df_prodt_usina -produção e potencia diária por unidade geradora
        # Eólica
        # Solar
    
    # Dados dos reservatórios (incompleto)
        df_RES_D
    


# Bibliotecas

# In[145]:



import os
import time
import fnmatch
import urllib.request
import telegram
import datetime
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


# Download de tabelas

# In[153]:



# Define o número de dias anteriores para buscar as URLs das regiões
num_days =3 

# Obtém as datas dos últimos 'num_days' dias e inverte a lista para buscar da menor para a maior data
dates = [datetime.today() - timedelta(days=x) for x in range(num_days)][::-1]

# Define os formatos das datas para uso na URL e no nome do arquivo
date_formats = [date.strftime('%Y_%m_%d') for date in dates]
date_formats2 = [date.strftime('%d-%m-%Y') for date in dates]

# Define as URLs de download com variação das datas definidas
url_regioes = {}
url_prod = {}
url_reservatorios= {}

for i in range(num_days):
    # BALANÇO DE ENERGIA ACUMULADA DIÁRIA - BEA
    url_regioes[date_formats[i]] = {
        'sul': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/03_DadosDiariosAcumulados_Regiao_{date_formats2[i]}.xlsx',
        'sudeste': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/04_DadosDiariosAcumulados_Regiao_{date_formats2[i]}.xlsx',
        'nordeste': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/05_DadosDiariosAcumulados_Regiao_{date_formats2[i]}.xlsx',
        'norte': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/06_DadosDiariosAcumulados_Regiao_{date_formats2[i]}.xlsx',
        'brasil': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/07_DadosDiariosAcumulados_Regiao_{date_formats2[i]}.xlsx'
    }
    # PRODUÇÃO DE ENERGIA POR TIPO (BDE_D)
    url_prod[date_formats[i]] = {
        '_H': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/08_ProducaoHidraulicaUsina_{date_formats2[i]}.xlsx',
        '_T': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/09_ProducaoTermicaUsina_{date_formats2[i]}.xlsx'
        #'PROD_S':PLATAFORMA QUEBRADA
        #'PROD_E': PLATAFORMA QUEBRADA
    }
    
    url_reservatorios[date_formats[i]] = {
        'sul': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/23_SituacaoPrincipaisReservatorios_Regiao_{date_formats2[i]}.xlsx',
        'sudeste': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/24_SituacaoPrincipaisReservatorios_Regiao_{date_formats2[i]}.xlsx',
        'nordeste': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/25_SituacaoPrincipaisReservatorios_Regiao_{date_formats2[i]}.xlsx',
        'norte': f'https://sdro.ons.org.br/SDRO/DIARIO/{date_formats[i]}/HTML/26_SituacaoPrincipaisReservatorios_Regiao_{date_formats2[i]}.xlsx'
    }
    
# Percorre URL_regioes para tentar baixar os arquivos
for data, urls in url_regioes.items():
    for regiao, url in urls.items():
        filename = f'BEA_D_{regiao.upper()}_{data}.xlsx'
        try:
            urllib.request.urlretrieve(url, filename)
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de {regiao} da data {data} baixado com sucesso')
        except urllib.error.HTTPError:
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de {regiao} da data {data} não encontrado')
            continue

# Percorre URL_prod para tentar baixar os arquivos
for data, urls in url_prod.items():
    for prod_type, url in urls.items():
        filename = f'BDE_D_PROD_{prod_type}_{data}.xlsx'
        try:      
            urllib.request.urlretrieve(url, filename)
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de produção {prod_type} da data {data} baixado com sucesso')
        except urllib.error.HTTPError:
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de produção {prod_type} da data {data} não encontrado')
            continue
    
# Percorre URL_regioes para tentar baixar os arquivos
for data, urls in url_reservatorios.items():
    for reservatorios, url in urls.items():
        filename = f'RES_{regiao.upper()}_{data}.xlsx'
        try:
            urllib.request.urlretrieve(url, filename)
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de {regiao} da data {data} baixado com sucesso')
        except urllib.error.HTTPError:
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de {regiao} da data {data} não encontrado')
            continue

# Percorre URL_reservatorios para tentar baixar os arquivos
for data, urls in url_reservatorios.items():
    for regiao, url in urls.items():
        filename = f'RES_D_{regiao.upper()}_{data}.xlsx'
        try:
            urllib.request.urlretrieve(url, filename)
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de {regiao} da data {data} baixado com sucesso')
        except urllib.error.HTTPError:
            bot = telegram.Bot(token='SEU_TOKEN_AQUI')
            bot.send_message(chat_id='SEU_CHAT_ID_AQUI', text=f'Arquivo de {regiao} da data {data} não encontrado')
            continue


# ETLs

# In[150]:


# ETL BALANÇO DE ENERGIA ACUMULADA DIÁRIA

dfs = []
for date in date_formats:
    df_date = pd.DataFrame()
    for regiao in ['sul','sudeste', 'nordeste', 'norte','brasil']:
        prod_regiao = f'BEA_D_{regiao.upper()}_{date}.xlsx'
        if os.path.exists(prod_regiao):
            df = pd.read_excel(prod_regiao, sheet_name='Plan1')
            df['data_captura'] = date
            df['regiao'] = regiao
            df_date = pd.concat([df_date, df], axis=0)
        dfs.append(df_date)
        

# Concatena e remove col completamente vazias
    df_BEA_D = pd.concat(dfs, axis=0).dropna()

# Renomeia colunas
    df_BEA_D = df_BEA_D.rename(columns={'Unnamed: 0': 'data',
                             'Unnamed: 1': 'total',
                             'Unnamed: 2': 'hidraulica',
                             'Unnamed: 3': 'termica',
                             'Unnamed: 4': 'eolica',
                             'Unnamed: 5': 'solar',
                             'Unnamed: 6': 'intercambio',
                             'Unnamed: 7': 'carga'})

# Limpando o dataframe
    to_remove = ['Dados Diários acumulados', 'Valores - MWmed', 'Subsistema Norte', 'Total', np.nan,'Data', 'Subsistema Sul', 'Subsistema Nordeste', 'Subsistema Sudeste']
    df_BEA_D = df_BEA_D[~df_BEA_D['data'].isin(to_remove)]

# Remove valores que se repetem em 'data' e 'regiao', incluindo valores vazios
    df_BEA_D.drop_duplicates(subset=['data', 'regiao'], inplace=True)

#atualizando formato dos dados
    df_BEA_D['total'] = pd.to_numeric(df_BEA_D['total'], errors='coerce')
    df_BEA_D['hidraulica'] = pd.to_numeric(df_BEA_D['hidraulica'], errors='coerce')
    df_BEA_D['termica'] = pd.to_numeric(df_BEA_D['termica'], errors='coerce')
    df_BEA_D['eolica'] = pd.to_numeric(df_BEA_D['eolica'], errors='coerce')
    df_BEA_D['solar'] = pd.to_numeric(df_BEA_D['solar'], errors='coerce')
    df_BEA_D['intercambio'] = pd.to_numeric(df_BEA_D['intercambio'], errors='coerce')
    df_BEA_D['carga'] = pd.to_numeric(df_BEA_D['carga'], errors='coerce')
    df_BEA_D['data'] = pd.to_datetime(df_BEA_D['data'], format='%d/%m/%Y')
    df_BEA_D['data_captura'] = pd.to_datetime(df_BEA_D['data_captura'], format='%Y_%m_%d') 


# In[164]:


import datetime

# Obtém o caminho atual do diretório do script
dir_path = os.getcwd()

# Define o padrão de nome de arquivo para correspondência
filename_pattern_h = 'BDE_D_PROD__H*.xlsx'
filename_pattern_t = 'BDE_D_PROD__T*.xlsx'

# Cria listas vazias para armazenar os DataFrames de cada tipo de arquivo
dfs_h1 = []
dfs_h2 = []
dfs_h3 = []
dfs_t1 = []
dfs_t2 = []
dfs_t3 = []

# Percorre todos os arquivos na pasta atual que correspondem ao padrão de nome de arquivo
for filename in os.listdir(dir_path):
    if fnmatch.fnmatch(filename, filename_pattern_h):
        try:
            # Extrai a data do nome do arquivo
            date_str = '_'.join(filename.split('_')[5:9]).split('.')[0]
            
            # Tenta converter a string em um objeto datetime
            try:
                date_obj = datetime.datetime.strptime(date_str, '%Y_%m_%d')
                
                # Lê as tabelas prodh_rg, poth_rg e prodh_usina em seus respectivos dataframes e adiciona uma coluna com a data
                prodh_rg = pd.read_excel(os.path.join(dir_path, filename), sheet_name='Plan1', header=3, usecols='A:D', nrows=7)
                prodh_rg['data'] = date_obj
                dfs_h1.append(prodh_rg)
                
                poth_rg = pd.read_excel(os.path.join(dir_path, filename), sheet_name='Plan1', header=11, usecols='A:D', nrows=7)
                poth_rg['data'] = date_obj
                dfs_h2.append(poth_rg)
                
                prodh_usina = pd.read_excel(os.path.join(dir_path, filename), sheet_name='Plan1', header=22, usecols='A:D', nrows=1000)
                prodh_usina['data'] = date_obj
                dfs_h3.append(prodh_usina)
            except ValueError:
                # A string não pode ser convertida em uma data
                print(f"Valor inválido na coluna date do arquivo {filename}: {date_str}")
                continue
        except Exception as e:
            print(f"Erro ao ler o arquivo {filename}: {e}")
    
    elif fnmatch.fnmatch(filename, filename_pattern_t):
        try:
            # Extrai a data do nome do arquivo
            date_str = '_'.join(filename.split('_')[5:9]).split('.')[0]
            
            # Tenta converter a string em um objeto datetime
            try:
                date_obj = datetime.datetime.strptime(date_str, '%Y_%m_%d')
                
                # Lê as tabelas prodt_rg, pott_rg e prodt_usina em seus respectivos dataframes e adiciona uma coluna com a data
                prodt_rg = pd.read_excel(os.path.join(dir_path, filename), sheet_name='Plan1', header=3, usecols='A:D', nrows=7)
                prodt_rg['data'] = date_obj
                dfs_t1.append(prodt_rg)
                
                pott_rg = pd.read_excel(os.path.join(dir_path, filename), sheet_name='Plan1', header=10, usecols='A:D', nrows=7)
                pott_rg['data'] = date_obj
                dfs_t2.append(pott_rg)
                
                prodt_usina = pd.read_excel(os.path.join(dir_path, filename), sheet_name='Plan1', header=20, usecols='A:D', nrows=1000)
                prodt_usina['data'] = date_obj
                dfs_t3.append(prodh_usina)
            except ValueError:
                # A string não pode ser convertida em uma data
                print(f"Valor inválido na coluna date do arquivo {filename}: {date_str}")
                continue
        except Exception as e:
            print(f"Erro ao ler o arquivo {filename}: {e}")
        
# OBS: a tabela BDE_D_PROD__H Itaipu é classificada como uma região, criando +1 linha de diferença por tabela à BDE_D_PROD__T 

# Concatenando os dataframes Hidráulico Térmico
df_prodh_rg = pd.concat(dfs_h1)
df_poth_rg = pd.concat(dfs_h2)
df_prodh_usina = pd.concat(dfs_h3)
df_prodt_rg = pd.concat(dfs_t1)
df_pott_rg = pd.concat(dfs_t2)
df_prodt_usina = pd.concat(dfs_t3)


# A tabela df_prodt_rg apresentou valores em object mesmo a leitura correta
df_prodt_rg['GWh no Dia'] = pd.to_numeric(df_prodt_rg['GWh no Dia'], errors='coerce')
df_prodt_rg['GWh acum. no Mês até o Dia'] = pd.to_numeric(df_prodt_rg['GWh acum. no Mês até o Dia'], errors='coerce')
df_prodt_rg['GWh acum. no Ano até o Dia'] = pd.to_numeric(df_prodt_rg['GWh acum. no Ano até o Dia'], errors='coerce')


# Removendo linhas duplicadas
dfs = [df_prodh_rg, df_poth_rg, df_prodh_usina, df_prodt_rg, df_pott_rg, df_prodt_usina]
dfs = list(map(lambda df: df.drop_duplicates(), dfs))


# In[159]:


pd.read_excel("BDE_D_PROD__T_2023_03_06.xlsx")
print(dir_path)


# In[141]:





# In[167]:


# ELT reservatorios
import pandas as pd

dfs = []
for date in date_formats:
    df_date = pd.DataFrame()
    for regiao in ['sul','sudeste', 'nordeste', 'norte']:
        cap_reservatorio = f'RES_D_{regiao.upper()}_{date}.xlsx'
        if os.path.exists(cap_reservatorio):
            df = pd.read_excel(cap_reservatorio, sheet_name='Plan1')
            filename = os.path.basename(cap_reservatorio)
            date_str = '_'.join(filename.split('_')[3:6]).split('.')[0]
            df['data_captura'] = date_str
            df['regiao'] = regiao
            df_date = pd.concat([df_date, df], axis=0)
    dfs.append(df_date)

# Concatena e remove col completamente vazias
df_RES_D = pd.concat(dfs, axis=0)

df_RES_D.drop('Unnamed: 2', axis=1, inplace=True)


# Renomeia colunas
df_RES_D = df_RES_D.rename(columns={'Unnamed: 0': 'bacia',
                             'Unnamed: 1': 'reservatorio',
                             'Unnamed: 2': 'nivel_m',
                             'Unnamed: 3': 'vol_util_%',
                             'Unnamed: 4': 'afluencia',
                             'Unnamed: 5': 'defluencia',
                             'Unnamed: 6': 'vertida',
                             'Unnamed: 7': 'transferida'})

# Limpando o dataframe
to_remove = ['Dados Hidráulicos dos Reservatórios', 'Subsistema Sul	', 'Subsistema Norte', 'Bacia', np.nan, 'Subsistema Sul', 'Subsistema Nordeste', 'Subsistema Sudeste']
df_BEA_D = df_BEA_D[~df_BEA_D['data'].isin(to_remove)]


#atualizando formato dos dados
df_BEA_D['total'] = pd.to_numeric(df_BEA_D['total'], errors='coerce')
    
df_RES_D.dtypes


# In[ ]:





# In[ ]:





# In[ ]:





# Balanço de Energia Acumulado no Mês Até o Dia -https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/02_BalancoEnergeticoAcumuloDia_05-03-2023.xlsx
# 
# Balanço de Energia Diário- https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/01_RelBalancoEnergeticoDiario_05-03-2023.xlsx
# 
#     
# DADOS ACUMULADO POR REGIÃO 
#             sul - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/03_DadosDiariosAcumulados_Regiao_05-03-2023.xlsx
# 
#             sudeste - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/04_DadosDiariosAcumulados_Regiao_05-03-2023.xlsx
# 
#             nordeste - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/05_DadosDiariosAcumulados_Regiao_05-03-2023.xlsx
# 
#             norte - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/06_DadosDiariosAcumulados_Regiao_05-03-2023.xlsx
# 
#             sist. interligado nasc - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/07_DadosDiariosAcumulados_Regiao_05-03-2023.xlsx
#     
#     
# PRODUÇÃO
# 
#             Produção hidraulica por usina - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/08_ProducaoHidraulicaUsina_05-03-2023.xlsx
# 
#             produção eletrica por usina - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/09_ProducaoTermicaUsina_05-03-2023.xlsx
# 
#             produção eolica (ta bichado, não libera o pdf no download)
# 
#             produção solar  (ta bichado, não libera o pdf no download)
# 
#             motivo do despacho termico - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/12_MotivoDespachoTermico_05-03-2023.xlsx
# 
#             reserva girante da demanda máxima - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/13_ReservaGiranteDemandaMaxima_05-03-2023.xlsx
#     
# 
# 
# 
# CARDA HORARIA
# 
# carga horaria por subsistema - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/14_CargaHorariaSub_05-03-2023.xlsx
# 
# carga diaria por subsistema - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/15_CargaDiariaSubmercado_05-03-2023.xlsx
# 
# demanda máxima - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/16_DemandaMaxima_05-03-2023.xlsx
#     
# 
# 
# 
# Integração de Novos Equipamentos e Linhas de Transmissão no SIN (??)
# 
# 
# Variação de Energia Armazenada - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/20_VariacaoCargaEnergiaArmazenada_05-03-2023.xlsx
# 
# Energia natural afluente - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/21_EnergiaNaturalAfluente_05-03-2023.xlsx
# 
# 
# 
# 
# DADOS HIDRAULICOS DOS RESERVATORIOS
# 
# SUL - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/23_SituacaoPrincipaisReservatorios_Regiao_05-03-2023.xlsx
# 
# SUDESTE - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/24_SituacaoPrincipaisReservatorios_Regiao_05-03-2023.xlsx
# 
# NORDESTE - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/25_SituacaoPrincipaisReservatorios_Regiao_05-03-2023.xlsx
# 
# NORTE - https://sdro.ons.org.br/SDRO/DIARIO/2023_03_05/HTML/26_SituacaoPrincipaisReservatorios_Regiao_05-03-2023.xlsx
# 
# 
# 

# In[ ]:




