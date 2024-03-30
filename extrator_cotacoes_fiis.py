#Obs: não somos responsáveis pela violação de qualquer direito autoral com o uso desse programa, use por sua
#responsabilidade, e lembre-se de dar crédito ao fundsexplorer.com.br

import argparse
from tqdm import tqdm
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
from datetime import datetime

# Versão do programa
VERSION = ['1.0.1']

# Options
parser = argparse.ArgumentParser(description='Extrator de dados de Cotaçoes de FIIS a partir do fundsexplorer.com.br.')
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {VERSION}')
parser.add_argument('-o', '--output', help='Especifique o nome de saíde do seu arquivo. O Default é fundsexplorer_ranking_output.csv.', default='fundsexplorer_ranking.csv')
args = parser.parse_args()

print(f'Started in:   {datetime.now().strftime("%B %d, %Y %H:%M:%S")}\n')
start_time = datetime.now()

def setUpdate():
    try:
        Service(ChromeDriverManager().install()) #instala o webdrive com a mesma versao
    except Exception as e:
        print(f'Error Install: {e}')

# status_bar
progress_bar = tqdm(total=6, bar_format='{l_bar}{bar}| {percentage:3.0f}% ')

# Inicialize o driver do Selenium
setUpdate()

progress_bar.update(1)  # Update

serv = Service(ChromeDriverManager().install()) #instala o webdrive com a mesma versao
options = Options()
options.add_argument("--lang=en")
options.add_argument('--headless')
options.add_argument("--incognito")
driver = webdriver.Chrome(service=serv, options=options)

url = "https://www.fundsexplorer.com.br/ranking"

# Navegue até a página
driver.get(url)

progress_bar.update(1)  # Update

# Espere até que a tabela esteja carregada (pode ser necessário aumentar esse tempo)
driver.implicitly_wait(10)

# Add JavaScript para Clicar no Elemento para pegar todas as colunas
select_all_checkbox = driver.find_element(By.ID, 'colunas-ranking__todos')
driver.execute_script("arguments[0].click();", select_all_checkbox)

# Extraia a tabela
table = driver.find_element(By.CSS_SELECTOR, '.default-fiis-table__container.ranking-table')

progress_bar.update(1)  # Update

# Crie um DataFrame do Pandas a partir dos dados da tabela
fiis = pd.read_html(table.get_attribute('outerHTML'), encoding='utf-8', decimal=".", thousands='.')[0]

# Feche o driver
driver.quit()

progress_bar.update(1)  # Update

# atualize a listas dos seus fundos para filtrar apenas os de interesse:
funds = ['VISC11', 
         'HGBS11', 
         'XPML11', 
         'HTMX11', 
         'HGLG11', 
         'VILG11', 
         'XPLG11', 
         'KNRI11', 
         'VINO11', 
         'BRCR11', 
         'IRDM11', 
         'TGAR11', 
         'MXRF11']

fiis = fiis[fiis['Fundos'].isin(funds)] #filtra os fundos seus fundos

fiis = fiis.dropna(axis=1, how='all') #remove colunas vazias

progress_bar.update(1)  # Update

# Salve o DataFrame em um arquivo CSV
fiis.to_csv(args.output, index=False, decimal='.')

progress_bar.update(1)  # Update

progress_bar.close()  # close

print(f'\nTotal time:    {str(datetime.now() - start_time).split(".")[0]}')
print(f'Finished at:   {datetime.now().strftime("%B %d, %Y %H:%M:%S")}\n')


