########################### CODIGO DA AULA 1 + 2 DA JORNADA RPA ############################
'''
Nota: Esse código foi gerado apartir da ferramenta Python RPA DEV Studio 2 conforme visto em https://youtu.be/rLdXNCvGnuE

O Python RPA Dev Studio é uma ferramenta low-code que auxilia na criação de automações;

Para esta atividade, o bot teve de:
# Pegar uma planilha que contenha dados incompletos de um cadastro de pessoas (Planilha disponivel em :        /aux/lista_clientes.xlsx )
# Utilizar o Bot para consumir uma API PUBLICA  ( https://cepsapi.com.br/public/index.html ) que vai buscar a complementação desses dados
# E trazendo a complementação, vai submeter isso numa Aplicação Web ( https://jornadarpa.com.br/alunos/desafios/cep )
#

'''
#####################################CADASTRO DE USUARIOS##############################################################
import json
from botcity.web.browsers.chrome import default_options
from webdriver_manager.chrome import ChromeDriverManager
import os
from botcity.web import *
from datetime import datetime
from botcity.plugins.excel import *
import requests

class Bot:
    def bot(self):

        # Flowchart Activity
        # Displayname: CADASTRO DE USUARIOS
        flowStep = "__ReferenceID0"

        while True:

            if flowStep == "__ReferenceID0":

                # Read Excel Activity
                # Displayname: Read_Excel
                excelBot = BotExcelPlugin()
                file_or_path = "F:\\RPA\\Python RPA\\Projeto Cadastro Clientes\\input\\lista_clientes.xlsx"

                listaClientes = excelBot.read(file_or_path=file_or_path).as_list(sheet="Sheet1")[1:]
                flowStep = "__ReferenceID1"
                continue

            if flowStep == "__ReferenceID1":

                # Open Browser Activity
                # Displayname: OpenBrowser
                webDriverPath = ChromeDriverManager().install()
                webBot = WebBot()
                webBot.driver_path = webDriverPath
                webBot.browser = Browser.CHROME
                webBot.headless = False
                webBotDef_options = default_options()
                webBotDef_options.add_argument("--incognito")
                webBotDef_options.add_argument("--page-load-strategy=Normal")
                webBot.options = webBotDef_options
                webBot.browse('https://jornadarpa.com.br/alunos/desafios/cep')

                flowStep = "__ReferenceID2"
                continue

            if flowStep == "__ReferenceID2":

                # Wait Activity
                # Displayname: Wait
                webBot.wait(5000)

                flowStep = "__ReferenceID3"
                continue

            if flowStep == "__ReferenceID3":

                # DisplayName: Element_Library

                # Sequence: Element list

                # Find Element Activity
                # Displayname: Find_Element
                botaoSalvar = webBot.find_element(selector="Salvar", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Find_Element
                campoNome = webBot.find_element(selector="nome", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Find_Element
                campoCep = webBot.find_element(selector="cep", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Find_Element
                campoEstado = webBot.find_element(selector="estado", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Find_Element
                campoRua = webBot.find_element(selector="rua", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                # Find Element Activity
                # Displayname: Find_Element
                campoBairro = webBot.find_element(selector="bairro", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

                flowStep = "__ReferenceID4"
                continue

            if flowStep == "__ReferenceID4":

                # ForEach Activity
                # Displayname: ForEach
                for line in listaClientes:
                    # Sequence: Body

                    # Http request Activity
                    # Displayname: 'Http_Request_Swegger'
                    api_key = ''
                    headers = {'Accept': 'application/json'}
                    query_params = {}
                    url = 'https://cepsapi.com.br/getLogradourosByCep/{cep}'
                    path_params = {'cep': line[1]}
                    if 'cep' in path_params:
                        url = url.replace('{cep}', str(path_params['cep']))
                    timeout_sec = 30
                    resultAPI = requests.get(url=url, headers=headers, params=query_params, timeout=timeout_sec)

                    # Displayname: Get_Field_API_Result
                    resultadoUF = (resultAPI.json() if hasattr(resultAPI, 'json') else resultAPI)['data'][0]['uf_sigla']
                    # Displayname: Get_Field_API_Result
                    resultadoRua = (resultAPI.json() if hasattr(resultAPI, 'json') else resultAPI)['data'][0]['logradouro_completo']
                    # Displayname: Get_Field_API_Result
                    resultadoBairro = (resultAPI.json() if hasattr(resultAPI, 'json') else resultAPI)['data'][0]['bairro_nome']
                    # DisplayName: Form_Element_Action_Web

                    # Sequence: Action list

                    # Type Into Activity
                    # Displayname: Type Into campoNome field
                    campoNome.send_keys(line[0])

                    # Type Into Activity
                    # Displayname: Type Into campoCep field
                    campoCep.send_keys(line[1])

                    # Type Into Activity
                    # Displayname: Type Into campoEstado field
                    campoEstado.send_keys(resultadoUF)

                    # Type Into Activity
                    # Displayname: Type Into campoRua field
                    campoRua.send_keys(resultadoRua)

                    # Type Into Activity
                    # Displayname: Type Into campoBairro field
                    campoBairro.send_keys(resultadoBairro)

                    # Click Activity
                    # Displayname: Click in botaoSalvar element
                    botaoSalvar.click()


            break


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()
