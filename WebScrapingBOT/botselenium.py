from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

import os
from dotenv import load_dotenv
from colorama import Fore


class WebScrapingSRI:
    def __init__(self):
        
        #Configuracion de chrome
        
        #self.chrome_options = Options()
        #self.chrome_options.add_argument("--headless")

        #Conexion de SRI
        self.ConnectionPage()
        #Inicio de sesion a SRI 
        self.LoginPage()
    def DriverSelected(self):
        try:
            self.browser = webdriver.Firefox()
            
        except:
            self.browser = webdriver.Chrome()
    def ConnectionPage(self):
        #self.browser = webdriver.Chrome(options=self.chrome_options)
        self.DriverSelected()
       
        #Condicional de conexion a pagina
        try: 
            self.browser.get('https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT') 
            print(Fore.BLUE + f"[{self.browser.title}]")
        except:
            print(Fore.RED+"Error en la conexion"+Fore.RESET)
    def LoginPage(self):
        #LOG
        print(Fore.YELLOW+"log/dev: Iniciando sesion"+Fore.RESET)

        #Cargando variables de entorno
        load_dotenv()

        #Ingresar al LOGIN
        FacturasElectronicasElement = self.browser.find_elements(By.CLASS_NAME,"ui-panelmenu-header-link")
        FacturasElectronicasElement [4].click()

        ComprobantesElectronicosElement = self.browser.find_element(By.XPATH,"//a[@href='https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=57&idGrupo=55']")
        ComprobantesElectronicosElement.click()

        USER = self.browser.find_element(By.ID,'usuario')
        CI = self.browser.find_element(By.ID,'ciAdicional')
        PASSWORD = self.browser.find_element(By.ID,'password')

        #Rellenar formulario
        USER.send_keys(os.getenv("USER"))
        CI.send_keys(os.getenv("CI"))
        PASSWORD.send_keys(os.getenv("PASSWORD"))

        #Enviar formulario
        btnSubmit = self.browser.find_element(By.ID,"kc-login")
        btnSubmit.submit()

        #Condicional de credenciales correctas
        AlertError = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"alert-error")))
        if(AlertError):
            print(Fore.RED+"log/dev: Error de sesion: Datos incorrectos"+Fore.RESET)
            self.browser.quit()
            exit()
        else:
            pass

        import time
        time.sleep(20)
    def DownloaFile(self):
        #Checkbox
        Rb_ruc = self.browser.find_element()
        Rb_ruc.click()
        #Periodo de emision
        self.browser.find_element()
        #Tipo de comprobante
        TypeOfReceipt = self.browser.find_element()
        select = Select(TypeOfReceipt)
        select.deselect_by_value()
        #Descargar
        btnDownload = self.browser.find_element()
        btnDownload.click()
        
WebScrapingSRI()
        