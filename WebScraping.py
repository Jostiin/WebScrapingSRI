import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#6Lc6rokUAAAAAJBG2M1ZM1LIgJ85DwbSNNjYoLDk
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time
import os
import datetime
import base64
import requests
import json
import mysql.connector
import random
import traceback



def start_webdriver():
    
    options = uc.ChromeOptions()
    options.add_argument("--password-store=basic")
    options.add_argument(f'--load-extension=C:/Users/Usuario/Documents/WebScrapingBOT/WebScrapingSRI2/2.0.1_0')
    #options.add_argument('--headless=new')
    #options.add_argument('--disable-gpu')
  
    #solver-button
    #solver-button

    #options.add_experimental_option(
    #    "prefs",{
    #        "credentials_enable_service":False,
    #        "profile.password_manager_enabled":False
    #    }
    #)
 
    '''
    options = Options()
    
    options.add_argument(f'--load-extension=C:/Users/Usuario/Documents/WebScrapingBOT/WebScrapingSRI2/2.0.1_0')
    
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--safebrowsing-disable-download-protection")  # Deshabilitar protección de descarga
    options.add_argument("--disable-infobars") 
    options.add_argument("--window-size=1600,1200")  
    prefs = {
    "profile.default_content_setting_values": {
        "cookies": 2,
        "images": 2,
        "plugins": 2,
        "popups": 2,
        "geolocation": 2,
        "notifications": 2,
        "auto_select_certificate": 2,
        "fullscreen": 2,
        "mouselock": 2,
        "mixed_script": 2,
        "media_stream": 2,
        "media_stream_mic": 2,
        "media_stream_camera": 2,
        "protocol_handlers": 2,
        "ppapi_broker": 2,
        "automatic_downloads": 2,
        "midi_sysex": 2,
        "push_messaging": 2,
        "ssl_cert_decisions": 2,
        "metro_switch_to_desktop": 2,
        "protected_media_identifier": 2,
        "app_banner": 2,
        "site_engagement": 2,
        "durable_storage": 2
    }
    
}

    # Agregar preferencias al objeto de opciones de Chrome
    options.add_experimental_option("prefs", prefs)
    
    #options.add_argument("--safebrowsing.enabled=false")
    
    options.add_argument("--safebrowsing-disable-download-protection")  # Deshabilitar protección de descarga
    #options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=options)
    '''
    driver = uc.Chrome(headless=False,options=options)
    return driver

def Ingresar_element_login_sri(driver):
    time.sleep(2)
    pausa = random.uniform(2,3)
    time.sleep(pausa)
    element_Iniciar_Sesion = WebDriverWait(driver,60).until(ec.element_to_be_clickable((By.XPATH,"//a[@href='/sri-en-linea/contribuyente/perfil']")))
    pausa = random.uniform(2,3)
    time.sleep(pausa)
    action = ActionChains(driver).move_to_element(element_Iniciar_Sesion)
    pausa = random.uniform(2,3)
    time.sleep(pausa)
    action.click().perform() 

def Ingresar_keys_login_sri(driver,ruc,password,ci=""):
  
        # TODO: Ingreso de RUC
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        e_ruc = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='usuario']")))
        
        #action_ruc = ActionChains(driver).move_to_element(e_ruc)
        
        #action_ruc.click().perform()
        #pausa = random.uniform(2,3)
        #time.sleep(pausa)
        e_ruc.send_keys(ruc)
        
        # TODO: Ingreso de CEDULA OPCIONAL
        if(ci != "0"):
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            e_cedula = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='ciAdicional']")))
            #action_cedula = ActionChains(driver).move_to_element(e_cedula)
            #action_cedula.click().perform() 
            #pausa = random.uniform(2,3)
            #time.sleep(pausa)
            e_cedula.send_keys(ci)
        else: 
            pass
    
        # TODO: Ingreso de PASSWORD
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        e_password = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='password']")))
        #action_password = ActionChains(driver).move_to_element(e_password)
       
        #action_password.click().perform() 
        #pausa = random.uniform(2,3)
        time.sleep(pausa)
        e_password.send_keys(password)
        # TODO: INGRESAR
        pausa = random.uniform(1,2)
        time.sleep(pausa)
        e_btnSubmit = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@value='Ingresar']")))
        pausa = random.uniform(1,2)
        time.sleep(pausa)
        action_btnSubmit = ActionChains(driver).move_to_element(e_btnSubmit)
        pausa = random.uniform(1,2)
        time.sleep(pausa)
        action_btnSubmit.click().perform() 
       
def Ingresar_menu_FacturacionElctronica_sri(driver):
  
    # TODO: Seleccionar seccion Facturación Electrónica
   
        pausa = random.uniform(2,2)
        time.sleep(pausa)
        e_btnFacturacion = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//button[@title='Facturación Electrónica']")))
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        action_btnFacturacion = ActionChains(driver).move_to_element(e_btnFacturacion)
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        action_btnFacturacion.click().perform() 
        # TODO: Ingreso a Comprobantes de pagos
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        e_comprobantesPago = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//a[@href='https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=57&idGrupo=55']")))
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        action_comprobantesPago = ActionChains(driver).move_to_element(e_comprobantesPago)
        pausa = random.uniform(2,3)
        time.sleep(pausa)
        action_comprobantesPago.click().perform()
    
def Rellenar_formulario_ComprobantesElectronicos_sri(driver,tipo):
            fecha_actual = datetime.datetime.now()
            dia_actual = fecha_actual.day
        # TODO: Seleccionar el radio Ruc/Cédula/Pasaporte
            #///pausa = random.uniform(2,3)
            #///time.sleep(pausa)
            #///e_RadioRuc = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:opciones:0']")))
            #///pausa = random.uniform(2,3)
            #///time.sleep(pausa)
            #///action_RadioRuc = ActionChains(driver).move_to_element(e_RadioRuc)
            #///pausa = random.uniform(2,3)
            #///time.sleep(pausa)
            #///action_RadioRuc.click().perform() 
            # TODO: Seleccionar la fecha
            #///time.sleep(5)
            #///e_SelectYear = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//select[@id='frmPrincipal:ano']")))
            #///action_SelectYear = ActionChains(driver).move_to_element(e_SelectYear)
            #///action_SelectYear.click().perform()
            # TODO: Seleccionar la mes
            #///time.sleep(5)
            #///e_SelectMonth = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//select[@id='frmPrincipal:mes']")))
            #///action_SelectMonth = ActionChains(driver).move_to_element(e_SelectMonth)
            #///action_SelectMonth.click().perform()
            # TODO: Seleccionar dia
            pausa = random.uniform(4,5)
            time.sleep(pausa)
            e_SelectDay = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//select[@id='frmPrincipal:dia']")))
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_SelectDay = ActionChains(driver).move_to_element(e_SelectDay)
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_SelectDay.click().perform() 
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            select_SelectDay = Select(e_SelectDay)
            if(tipo=="TXT"):
                select_SelectDay.select_by_visible_text("Todos")
            elif(tipo=="XML"):
                select_SelectDay.select_by_visible_text(f"{dia_actual-1}")
            # TODO: Seleccionar Tipo de comprobante
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            e_TipoComprobante = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//select[@id='frmPrincipal:cmbTipoComprobante']")))
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_TipoComprobante = ActionChains(driver).move_to_element(e_TipoComprobante)
            pausa = random.uniform(1,2)
            time.sleep(pausa)
            action_TipoComprobante.click().perform() 
            pausa = random.uniform(1,2)
            time.sleep(pausa)
            select_TipoComprobante = Select(e_TipoComprobante)
            select_TipoComprobante.select_by_visible_text("Factura")
            e_TipoComprobante2 = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//select[@id='frmPrincipal:cmbTipoComprobante']")))
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_TipoComprobante2 = ActionChains(driver).move_to_element(e_TipoComprobante2)
            pausa = random.uniform(1,2)
            time.sleep(pausa)
            action_TipoComprobante2.click().perform()
            time.sleep(2)
            #RecaptchaSolver(driver)
            time.sleep(10)
            
            # TODO: boton Consultar
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            e_btnConsult = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//button[@id='btnRecaptcha']")))
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_btnConsult = ActionChains(driver).move_to_element(e_btnConsult)
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_btnConsult.click().perform()         
        
def Proceso_archivo_TXT(RUC,url_webhook,id_company):

    ispassing = False
    # TODO: Descargar txt
    while(ispassing==False):
        try:
            time.sleep(6)
            e_btnDownload = WebDriverWait(driver,60).until(ec.element_to_be_clickable((By.XPATH,"//a[@id='frmPrincipal:lnkTxtlistado']")))
            pausa = random.uniform(3,7)
            time.sleep(pausa)
            e_btnDownload.click()
            time.sleep(2)
            break
            #action_btnDownload = ActionChains(driver).move_to_element(e_btnDownload)
            #pausa = random.uniform(3,7)
            #time.sleep(pausa)
            #action_btnDownload.click()
                    
        except ElementClickInterceptedException:
            e_btnSolver = WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//button[@id='solver-button']")))
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_btnSolver = ActionChains(driver).move_to_element(e_btnSolver)
            pausa = random.uniform(2,3)
            time.sleep(pausa)
            action_btnSolver.click().perform()

    print("Proceso archivo TXT")
    date = datetime.datetime.now()
    nombre_anterior = os.path.expanduser("~")+"/Downloads/"+RUC+"_Recibidos.txt"  #1791972066001_Recibidos.txt
    nombre_actual = os.path.expanduser("~")+"/Downloads/"+RUC+f"_{date.strftime('%d-%m-%Y')}_"+"Recibidos.txt"  #1791972066001_13/3/2024_Recibidos.txt
    try:
        os.rename(nombre_anterior,nombre_actual)
        #///self.ConvertBased64_Send(self.nombre_actual,i)
        with open(nombre_actual,'rb') as archivo:
            texto = archivo.read()
            text_based = base64.b64encode(texto)
            data = {
                "archivos": [text_based.decode()],
                "tipo":"TXT",
                "cantidad":1,
                
                "company_id":id_company
            }
            response = requests.post(url_webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            
            if response.status_code == 200:
                print(response.text)
                #///SendEmailProcess(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito")
                #SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito")
            else:
                pass
                #///SendEmailProcess(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")
                #SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")   
        os.remove(nombre_actual) 
    except:
        pass
        #///SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en la descarga del archivo. Volviendo a intentar dentro de 5 minutos...")
        #SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en la descarga del archivo.  Volviendo a intentar dentro de 5 minutos... \nDetails: {ee}")

def Proceso_archivo_XML(driver,id_company):
    dataXML = []
    rows_count = 0
    ispassing = False
    while(ispassing==False):
        try:
            time.sleep(10)
            e_tablaXML = WebDriverWait(driver,30).until(ec.presence_of_element_located((By.XPATH,"//tbody[@id='frmPrincipal:tablaCompRecibidos_data']")))
            rows = e_tablaXML.find_elements(By.TAG_NAME, "tr")
            rows_count = len(rows)
            break
        except:
            time.sleep(5)
            def get_shadow_root(element):
                return driver.execute_script('return arguments[0].shadowRoot', element)
            #iframe = WebDriverWait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it(()))
            iframe = driver.find_elements(By.TAG_NAME, "iframe")
            driver.switch_to.frame(iframe[2])
            divIframe = driver.find_elements(By.XPATH, "//div[@title='button-holder help-button-holder']").click()
            input("espera")
            
            #driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='recaptcha challenge expires in two minutes']"))
            #driver.switch_to.default_content()
            #WebDriverWait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"//iframe[@title='recaptcha challenge expires in two minutes']")))
            #WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@id='solver-button']"))).click()
            #shadow_host = driver.find_element(By.CLASS_NAME, 'button-holder help-button-holder')
            #button = get_shadow_root(shadow_host).find_element(By.XPATH, "//button[@id='solver-button']").click()
            
            
            #e_btnSolver = driver.find_element(By.XPATH,"//button[@id='solver-button']")
            #e_btnSolver = WebDriverWait(driver,30).until(ec.element_to_be_clickable(()))
            #pausa = random.uniform(2,3)
            #time.sleep(pausa)
            #action_btnSolver = ActionChains(driver).move_to_element(e_btnSolver)
            #pausa = random.uniform(2,3)
            #time.sleep(pausa)
            #e_btnSolver.click()
    input("enter xml")
    
    for i in range(0,rows_count):
        driver.implicitly_wait(5)
        fileXML =  WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID,f"frmPrincipal:tablaCompRecibidos:{i}:lnkXml")))
        fileXML.click()
        time.sleep(5)
        try:#FACTURAS
            nombre_actual = os.path.expanduser("~")+"/Downloads/Factura.xml"
            with open(nombre_actual,'rb') as archivo:
                texto = archivo.read()
            text_based = base64.b64encode(texto)
            dataXML.append(text_based.decode())
            os.remove(nombre_actual)
        except:#COMPROBANTES
            PathComprobante = os.path.expanduser("~")+"/Downloads/Comprobante de Retención.xml"
            with open(PathComprobante,'rb') as archivo:
                texto = archivo.read()
            text_based = base64.b64encode(texto)
            dataXML.append(text_based.decode())
            os.remove(PathComprobante)
    '''
    def convertir_a_base64(archivo):
        with open(archivo, 'rb') as archivo_xml:
            xml_bytes = archivo_xml.read()
            base64_bytes = base64.b64encode(xml_bytes)
            return base64_bytes.decode('utf-8')

    def listar_archivos_xml(ruta_carpeta):
        archivos_xml = []
        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith('.xml'):
                archivos_xml.append(archivo)
        return archivos_xml

    carpeta = 'C:/Users/Usuario/Downloads'  # Reemplaza con la ruta de la carpeta
    archivos_xml = listar_archivos_xml(carpeta)

    for archivo in archivos_xml:
        ruta_completa = os.path.join(carpeta, archivo)
        contenido_base64 = convertir_a_base64(ruta_completa)
        print(f"Archivo: {archivo}, Base64: {contenido_base64}")
    '''
    data = {
        "archivos": dataXML,
        "tipo":"XML",
        "cantidad":len(dataXML),
        "company_id":id_company
    }
    #response = requests.post(url_webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(json.dumps(data))
    #if response.status_code == 200:
    ##    pass
    #    SendEmailProcess(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito ")
       
    #else:
    #pass
    #    SendEmailProcess(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")
                            
    #//nombre_actual = os.path.expanduser("~")+"/Downloads/Factura.xml"
    
    
def RecaptchaSolver(driver):

    url = driver.current_url

    api = "83a82cc9461e57e8b1883ec0a6b8aaff"

    sitekey = "6Lc6rokUAAAAAJBG2M1ZM1LIgJ85DwbSNNjYoLDk"

    url1 = f"https://2captcha.com/in.php?key={api}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&invisible=1"
    r1 = requests.get(url1)
    textt1 = r1.text
    rid = textt1.split("|")[1]
    print(rid)
    url2 = f"https://2captcha.com/res.php?key={api}&action=get&id={rid}"
    time.sleep(5)
    while True:
        try:
            r2 = requests.get(url2)
            r2Text = r2.text
            form_token = r2Text.split("|")[1]
            print(form_token)
            break
        except:
            continue

    driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{form_token}";')
    time.sleep(10)
    #driver.execute_script(f'grecaptcha.execute()')
    #print("Captcha good")

    

if __name__ == '__main__':
    
    mydb = mysql.connector.connect(
        host="172.105.153.61",
        user="forge",
        password="CCfRNQT9fbx6lnJ5DYoI",
        database="Sivo_Security"
        )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM conexion_sri")
        myresult = mycursor.fetchall()
    for x in myresult:
        if x[8] == "A":
            ErrorPage = False
            while(ErrorPage==False):
                try:
                    driver = start_webdriver()
    
                    driver.get("https://srienlinea.sri.gob.ec/")
                    
                    # * LOGIN
                    Ingresar_element_login_sri(driver)
                    Ingresar_keys_login_sri(driver,x[2],x[5],x[4])
                    # * FACTURA ELECTRONICA
                    Ingresar_menu_FacturacionElctronica_sri(driver)
                    # * RELLENAR FORMULARIO
                    Rellenar_formulario_ComprobantesElectronicos_sri(driver,x[6])
                    
                    if(x[6] == "TXT"):

                        Proceso_archivo_TXT(x[2],x[7],x[1])
                        ErrorPage = True
                        break
                    elif(x[6] == "XML"):
                        Proceso_archivo_XML(driver,x[1])
                        ErrorPage = True
                        break
                    
                        
                except Exception as e:
                    print(e)
                    traceback.print_exc()
                    input("intentar de nuevo")
                    driver.quit()
                    
                    time.sleep(2)
            driver.quit()
                # * PAUSA
        else:
            continue
    
    