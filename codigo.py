# Passo a passo do projeto

# instalar o pyautogui
# pip install pyautogui
import pyautogui
import time
import pandas


pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=770, y=395)
pyautogui.write("rodrigopresida@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
time.sleep(3)
    

tabela = pandas.read_csv("produtos.csv")
print(tabela)
pyautogui.click(780, y=281)
for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
   
# codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
# marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
# tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
# categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
#preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
# custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
# observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(500)
    pyautogui.click(780, y=281)
    time.sleep(1)
    

#pyautogui.PAUSE = 1
# Clicar --> pyautogui.click
# Escrever --> pyautogui.write
# Apertar uma tecla --> pyautogui.press
# 1- Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# 2- Fazer login
# 3- Importar base de dados
# 4- Cadastrar produtos
# 5- Repetir o processo até acabar os dados





