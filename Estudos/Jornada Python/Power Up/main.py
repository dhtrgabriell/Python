import pyautogui as auto
import time
import pandas

# VAR
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'    
tabela = pandas.read_csv('produtos.csv')

# CONFG
auto.PAUSE = 0.5

# ABRINDO O NAVEGADOR
auto.hotkey('win', 's')
auto.write('edge')   

auto.press('enter')

# ACESSANDO O SITE
time.sleep(3)
auto.write(link)
auto.press('enter')
time.sleep(3)

# FAZENDO LOGIN
auto.click(x=535, y=287)
auto.write('pythonimpressionador@gmail.com')
auto.press('tab')
auto.write('sua senha')
auto.press('tab')
auto.press('enter')

# CADASTRAR DADOS
for linha in tabela.index:
    auto.click(x=502, y=198)
    auto.write(tabela.loc[linha, 'codigo'])
    auto.press('tab')
    auto.write(tabela.loc[linha, 'marca'])
    auto.press('tab')
    auto.write(tabela.loc[linha, 'tipo'])
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'categoria']))
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'preco_unitario']))
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'custo']))
    auto.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        auto.write(tabela.loc[linha, 'obs'])
    auto.press('tab')
    auto.press('enter')
    auto.scroll(5000)