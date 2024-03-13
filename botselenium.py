from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import argparse

parser = argparse.ArgumentParser(description="Scraping SRI")

parser.add_argument('RUC', help='RUC')
parser.add_argument('CI', help='RUC')
parser.add_argument('CLAVE', help='RUC')

args = parser.parse_args()

class WebScrapingSRI:
    def __init__(self,RUC,CI_,password):
        #Configuracion de chrome
        self.RUC = RUC
        self.password = password
        self.CI_ = CI_

        self.LoginPageConnection = False
        self.DriverSelected()
        #Conexion de SRI
        #Login
        while(self.LoginPageConnection  == False):
            try:
                self.ConnectionPage()
                self.LoginPage()
            except:
                print("Error en la pagina: Esperar 3 minutos")
                self.browser.close()
                time.sleep(180)
                pass
        self.browser.close()
        exit()
    def DriverSelected(self):
    
        #try:
        #chrome_options = Options()
        #chrome_options.headless = True 
        #chrome_options.port = 4444  
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("--headless=new")
        #chrome_options.add_argument("--disable-dev-shm-usage")

      
        #1
        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        #options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(options=options)



        #self.browser = webdriver.Firefox()
        #self.browser = webdriver.Firefox(options = chrome_options,executable_path='/usr/local/bin/geckodriver')
        #except:

        #    firefox_options = Options()
        #    firefox_options.add_argument("--headless")
        #    self.browser = webdriver.Firefox(options=firefox_options)
    def ConnectionPage(self):
       
        #Condicional de conexion a pagina
        try: 
            self.browser.get('https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT') 

        except:
            print("Error en la conexion")
            self.browser.close()
            exit()
    def LoginPage(self):
        #LOG
        print("Iniciando sesion")
        #Cargando variables de entorno
        self.browser.implicitly_wait(30)
        #Ingresar al LOGIN
        
        FacturasElectronicasElement = self.browser.find_elements(By.CLASS_NAME,"ui-panelmenu-header-link")
        FacturasElectronicasElement[4].click()

        ComprobantesElectronicosElement = self.browser.find_element(By.XPATH,"//a[@href='https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=57&idGrupo=55']")
        ComprobantesElectronicosElement.click()

        USER = self.browser.find_element(By.ID,'usuario')
        CI = self.browser.find_element(By.ID,'ciAdicional')
        PASSWORD = self.browser.find_element(By.ID,'password')


        #Rellenar formulario

        USER.send_keys(self.RUC)
        if self.CI_ != "0":
            CI.send_keys(self.CI_)
        else:
            pass
        PASSWORD.send_keys(self.password)

        #Enviar formulario
        btnSubmit = self.browser.find_element(By.ID,"kc-login")
        btnSubmit.submit()

        #Condicional de credenciales correctas
        try: 
            AlertError = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"alert-error")))
            if(AlertError):
                print("log/dev: Error de sesion: Datos incorrectos")
                self.browser.close()
                exit()
            else:
                pass
        except:
            pass

        self.DownloaFile()
    def DownloaFile(self):
        print("Descargando..")
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
        self.browser.implicitly_wait(30)
        wait = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID,"frmPrincipal:lnkTxtlistado")))
        wait.click()
        self.LoginPageConnection = True


WebScrapingSRI( args.RUC,args.CI,args.CLAVE)

#WebScrapingSRI("1791972066001","Walejandro86*","1720802394")
  



#WebScrapingSRI("1720802394001","Walejandro86*")





#1720802394001 # 1791972066001
#1720802394
#Walejandro86*