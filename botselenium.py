from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.common.exceptions import ElementClickInterceptedException,ElementNotInteractableException

import os
import requests
import json
import time
import argparse
import base64
from datetime import datetime

parser = argparse.ArgumentParser(description="Scraping SRI")

parser.add_argument('RUC', help='RUC')
parser.add_argument('CI', help='RUC')
parser.add_argument('CLAVE', help='RUC')

args = parser.parse_args()

class WebScrapingSRI:
    def __init__(self,RUC,CI_,password):
        
        self.RUC = RUC
        self.password = password
        self.CI_ = CI_
        self.url_webhook = "https://app.sivo.ec/v5/webhooktxt"

        self.LoginPageConnection = False
        while(self.LoginPageConnection  == False):
            try:
                self.DriverSelected()
                self.ConnectionPage()
                self.LoginPage()
            except:
                print("Error: Esperar 5 minutos")
                self.browser.quit()
                time.sleep(300)
                pass
        self.browser.quit()
        exit()  
    def DriverSelected(self):
        ua = UserAgent(browsers=['chrome'])
        randomAgent = ua.random
        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        #options.add_argument('user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
        options.add_argument(f'user-agent={randomAgent}')
        self.browser = webdriver.Chrome(options=options)
        self.actions = ActionChains(self.browser)
    def ConnectionPage(self):
        try: 
            self.browser.get('https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT') 
        except:
            pass   
    def LoginPage(self):
        print("Registrandose")
        self.browser.implicitly_wait(30)
        #FacturasElectronicasElement = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"ui-panelmenu-header-link")))
        FacturasElectronicasElement = self.browser.find_elements(By.CLASS_NAME,"ui-panelmenu-header-link")
        #self.actions.move_to_element(FacturasElectronicasElement[4]).perform()
        FacturasElectronicasElement[4].click()

        ComprobantesElectronicosElement = self.browser.find_element(By.XPATH,"//a[@href='https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=57&idGrupo=55']")
        #self.actions.move_to_element(ComprobantesElectronicosElement).perform()
        ComprobantesElectronicosElement.click()

        USER = self.browser.find_element(By.ID,'usuario')
        CI = self.browser.find_element(By.ID,'ciAdicional')
        PASSWORD = self.browser.find_element(By.ID,'password')

        USER.send_keys(self.RUC)
        self.browser.implicitly_wait(5)
        if self.CI_ != "0":
            CI.send_keys(self.CI_)
        else:
            pass
        PASSWORD.send_keys(self.password)
        self.browser.implicitly_wait(2)
        btnSubmit = self.browser.find_element(By.ID,"kc-login")
        btnSubmit.submit()
        try: 
            AlertError = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"alert-error")))
            if(AlertError):
                print("Datos incorrectos")
                self.browser.quit()
                exit()
            else:
                pass
        except:
            self.DownloaFile()    
    def DownloaFile(self):
        print("Esperando descarga...")
        Issue_period_day = self.browser.find_element(By.ID, 'frmPrincipal:dia')
        select_day = Select(Issue_period_day)
        select_day.select_by_value("0")
        #Consultar facturas
        btnConsult = self.browser.find_element(By.ID,"btnRecaptcha")
        btnConsult.click()
        #CAPTCHA
        try:
            boxImg1 = self.browser.find_element(By.XPATH,"//td[@tabindex=9]")
            boxImg2 = self.browser.find_element(By.XPATH,"//td[@tabindex=10]")
            boxImg3 = self.browser.find_element(By.XPATH,"//td[@tabindex=13]")
            boxImg1.click()
            boxImg2.click()
            boxImg3.click()
        except:
            pass
        #Descargar facturas
        #self.browser.implicitly_wait(10)
        wait = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID,"frmPrincipal:lnkTxtlistado")))
        self.actions.move_to_element(wait).perform()
        wait.click()
        print("Archivo descargado")
        self.LoginPageConnection = True
        self.MoveFile()
    def MoveFile(self):
        date = datetime.now()
        nombre_anterior = os.path.expanduser("~")+"/Downloads/"+self.RUC+"_Recibidos.txt"  #1791972066001_Recibidos.txt
        nombre_actual = os.path.expanduser("~")+"/Downloads/"+self.RUC+f"_{date.strftime('%d-%m-%Y')}_"+"Recibidos.txt"  #1791972066001_13/3/2024_Recibidos.txt
        
        try:
            os.rename(nombre_anterior,nombre_actual)
        except:
            pass
        self.ConvertBased64_Send(nombre_actual)
        os.remove(nombre_actual) 
    def ConvertBased64_Send(self,PathFile):
        with open(PathFile,'rb') as archivo:
            texto = archivo.read()
        text_based = base64.b64encode(texto)
        data = {
            "archivo": text_based.decode()
        }
        response = requests.post(self.url_webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
          print("Archivo enviado correctamente")
          print(response.text)
        else:
           print("Error al enviar el archivo")
           pass

WebScrapingSRI(args.RUC,args.CI,args.CLAVE)
