import pyautogui
import time
import pandas
#
pyautogui.PAUSE = 0.5
#
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# abre o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(site)
pyautogui.press("enter")

#esperar o carregamento

time.sleep(3)
#LOGIN
pyautogui.press("TAB")
time.sleep(3)
pyautogui.write("TESTE LOGIN")
pyautogui.press("TAB")
time.sleep(3)
pyautogui.write("TESTE SENHA")
pyautogui.press("TAB")
time.sleep(3)
pyautogui.press("ENTER")

#PAGINA SEGUINTE ( https://dlp.hashtagtreinamentos.com/python/intensivao/tabela )

#TABELA
tabela = pandas.read_csv('produtos.csv')
print(tabela.size)

for i in tabela.index:
   pyautogui.click(x=38,y=600)
   time.sleep(3)
   pyautogui.press("TAB")
   codigo = tabela.loc[i, "codigo"]
   pyautogui.write(str(codigo))
   pyautogui.press("TAB")
   marca = tabela.loc[i, "marca"]
   pyautogui.write(str(marca))
   pyautogui.press("TAB")
   tipo = tabela.loc[i, "tipo"]
   pyautogui.write(str(tipo))
   pyautogui.press("TAB")
   categoria = tabela.loc[i, "categoria"]
   pyautogui.write(str(categoria))
   pyautogui.press("TAB")
   precoun = tabela.loc[i, "preco_unitario"]
   pyautogui.write(str(precoun))
   pyautogui.press("TAB")
   custo = tabela.loc[i, "custo"]
   pyautogui.write(str(custo))
   pyautogui.press("TAB")

   obs = tabela.loc[i, "obs"]
   if not pandas.isna(obs):
       pyautogui.write(str(obs))

   #FIM DO LOOP
   pyautogui.press("TAB")
   pyautogui.press("ENTER")
   pyautogui.scroll(5000)
# COMANDOS DIVERSOS
# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey




#STEP 1
#Abrir o link "  https://dlp.hashtagtreinamentos.com/python/intensivao/login  "

#STEP 2
# Introduizr Login
# Introduizr Senha
# Clicar em Logar

#STEP 3
# Preencher os campos CODIGO DO PRODUTO | MARCA DO PRODUTO | TIPO DO PRODUTO | CATEGORIA DO PRODUTO | PREÇO UNITARIO DO PRODUTO | CUSTO DO PRODUTO | OBS
# CLICAR EM ENVIAR


#PYAUTOGUI : ANY -   biblioteca que serve para guiar o mouse
#Usa o pip install pyautogui

