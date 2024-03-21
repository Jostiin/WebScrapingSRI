from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from email.message import EmailMessage
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException

import os
import requests
import json
import time
import mysql.connector
import smtplib

import base64
from datetime import datetime

def SendEmailProcessSecond(Company,subject,message):
    date = datetime.now()
    remitente = "orbejostin513@gmail.com"
    destinatario = "orbejostin513@gmail.com"
    mensaje = f"{Company.upper()}\n\n{message}\n\nArchivo: TXT\nFecha: {date.strftime('%d/%m/%Y')}\nHora: {date.strftime('%H:%M %p')}" 
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = subject
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login(remitente, "qqfn mnzt tpei jybj")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

def SendEmailProcess(Company,subject,message):
    date = datetime.now()
    
    remitente = "orbejostin513@gmail.com"
    destinatario = "wespinosa86@gmail.com"
    mensaje = f"{Company.upper()}\n\n{message}\n\nArchivo: TXT\nFecha: {date.strftime('%d/%m/%Y')}\nHora: {date.strftime('%H:%M %p')}" 
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = subject
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login(remitente, "qqfn mnzt tpei jybj")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()
    

class WebScrapingSRI:
    def __init__(self,ID_company,RUC,CI_,password,url,type,companyName):
        
        self.RUC = RUC
        self.password = password
        self.CI_ = CI_
        self.url_webhook = url
        self.type_ = type.lower()
        self.dataXML = []
        self.attempts = 1
        self.id_company = ID_company
        self.company_Name = companyName

        #"https://app.sivo.ec/v5/webhooktxt"
        self.LoginPageConnection = False
        while(self.LoginPageConnection  == False):
            try:
                self.DriverSelected()
                self.ConnectionPage()
                self.LoginPage()
                
            except NoSuchElementException:
                print("Error de conexion en la sección 'Comprobantes electrónicos recibidos', volviendo a intentar en 5 minutos...")
                print("--------------------ERROR WAIT 5--------------------")
                self.browser.quit()
                time.sleep(300)
                pass
            except ElementClickInterceptedException:
                print("Error en la descarga del archivo por posible recaptcha, volviendo a intentar en 5 minutos...")
                print("--------------------ERROR WAIT 5--------------------")
                self.browser.quit()
                time.sleep(300)
                pass
                
            except Exception as e:
                self.attempts = self.attempts + 1
                print(e)
                SendEmailProcessSecond(self.company_Name,"BOT SELENIUM ERROR",f"Error desconocido \nDetails: {e}")
                print("--------------------ERROR WAIT 5--------------------")
                self.browser.quit()
                time.sleep(300)
                pass
        self.browser.quit()   
    def DriverSelected(self):
        print("DriverSelect")
        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
       
        #options.add_argument(f'user-agent={randomAgent}')
        self.browser = webdriver.Chrome(options=options)
        self.actions = ActionChains(self.browser)
    def ConnectionPage(self):
        print("ConnectionPage")
        try: 
            self.browser.get('https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT') 
        except:
            print("No se pudo conectar a la pagina, volviendo a intentar en 5 minutos...")      
    def LoginPage(self):
        print("Iniciando session")
        self.browser.implicitly_wait(30)
       
        FacturasElectronicasElement = self.browser.find_elements(By.CLASS_NAME,"ui-panelmenu-header-link")
      
        FacturasElectronicasElement[4].click()

        print("FacturasElectronicasElement")
        time.sleep(2)

        ComprobantesElectronicosElement = self.browser.find_element(By.XPATH,"//a[@href='https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=57&idGrupo=55']")
        
        ComprobantesElectronicosElement.click()
        print(" ComprobantesElectronicosElement")
        time.sleep(2)

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
        print("keys send")
        self.browser.implicitly_wait(2)
        btnSubmit = self.browser.find_element(By.ID,"kc-login")
        btnSubmit.submit()
        time.sleep(2)
        try: 
            AlertError = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"alert-error")))
            if(AlertError):
               
                SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en el registro: credenciales incorrectas.")
                print("Error en el registro: credenciales incorrectas.")
                SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en el registro: credenciales incorrectas.")
                self.browser.quit()
            else:
                pass
        except:
            print("Except on Download file")
            self.DownloaFile()    
    def DownloaFile(self):
        print("DownloadFile")
        if self.type_ == "txt":
            date = datetime.now()
            
            Issue_period_day = self.browser.find_element(By.ID, 'frmPrincipal:dia')
            select_day = Select(Issue_period_day)
            select_day.select_by_value("0") #TODOS
            #Consultar facturas
            btnConsult = self.browser.find_element(By.ID,"btnRecaptcha")
            btnConsult.click()
          
            #Descargar facturas TXT
            self.browser.implicitly_wait(20)
            wait = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID,"frmPrincipal:lnkTxtlistado")))
            self.actions.move_to_element(wait).perform()
            wait.click()
            time.sleep(5)
            self.MoveFile(0)
        elif self.type_ == "xml":
            Issue_period_day = self.browser.find_element(By.ID, 'frmPrincipal:dia')
            select_day = Select(Issue_period_day)
            select_day.select_by_value(str(datetime.now().day-1))
            #Consultar facturass
            btnConsult = self.browser.find_element(By.ID,"btnRecaptcha")
            btnConsult.click()
            #Descargar facturas XML
            try:
                self.browser.implicitly_wait(20)
                TablaRecibidos = self.browser.find_element(By.ID,"frmPrincipal:tablaCompRecibidos_data")
                rows = TablaRecibidos.find_elements(By.TAG_NAME, "tr")
                rows_count = len(rows)
                try:
                    for i in range(0,rows_count):
                        self.browser.implicitly_wait(5)
                        fileXML =  WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID,f"frmPrincipal:tablaCompRecibidos:{i}:lnkXml")))
                        fileXML.click()
                        time.sleep(2)
                        self.MoveFile(i)
                    try:
                        data = {
                            "archivos": self.dataXML,
                            "tipo":self.type_.upper(),
                            "cantidad":len(self.dataXML),
                            "company_id":self.id_company
                        }
                        response = requests.post(self.url_webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
                        #print(json.dumps(data))
                        if response.status_code == 200:
                            self.LoginPageConnection = True
                            SendEmailProcess(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito")
                            SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito")
                        else:
                            SendEmailProcess(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")
                            SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")
                    except requests.exceptions.ConnectionError:
                        SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en la conexion del webhook. Programa finalizado")
                        SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en la conexion del webhook. Programa finalizado")
                        self.LoginPageConnection = True
                except:
                    print("Error en la descarga de los archivos {self.type_}, volviendo intentar en 5 minutos...")
                    self.attempts = self.attempts+1
                    self.LoginPageConnection = True
            except:
                SendEmailProcess(self.company_Name,"Descarga SRI",f"No existen archivos descargables para el dia {date.day()-1}")
                SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"No existen archivos descargables para el dia {date.day()-1}")
                self.LoginPageConnection = True

            self.LoginPageConnection = True 
        else:
            SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en el archivo: Verifique el tipo de arhivo (TXT,XML)")
            SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en el archivo: Verifique el tipo de arhivo (TXT,XML)")
            self.LoginPageConnection = True      
    def MoveFile(self,i):
        print("MoveFile")
        if self.type_ == "txt":
            date = datetime.now()
            nombre_anterior = os.path.expanduser("~")+"/Downloads/"+self.RUC+"_Recibidos.txt"  #1791972066001_Recibidos.txt
            self.nombre_actual = os.path.expanduser("~")+"/Downloads/"+self.RUC+f"_{date.strftime('%d-%m-%Y')}_"+"Recibidos.txt"  #1791972066001_13/3/2024_Recibidos.txt
            try:
                os.rename(nombre_anterior,self.nombre_actual)
                self.ConvertBased64_Send(self.nombre_actual,i)
            except Exception as ee:
                SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en la descarga del archivo. Volviendo a intentar dentro de 5 minutos...")
                SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en la descarga del archivo.  Volviendo a intentar dentro de 5 minutos... \nDetails: {ee}")
                
                pass
        elif self.type_ == "xml":
            self.nombre_actual = os.path.expanduser("~")+"/Downloads/Factura.xml"
            try:
                self.ConvertBased64_Send(self.nombre_actual,i)
            except Exception as ee:
                SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en la descarga del archivo \nDetails: {ee}")
                SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en la descarga del archivo \nDetails: {ee}")
    def ConvertBased64_Send(self,PathFile,i):
        print("ConvertBased64")
        #print(f"Archivo {self.type_} descargado")
        if self.type_ == "txt":
            with open(PathFile,'rb') as archivo:
                texto = archivo.read()
            text_based = base64.b64encode(texto)
            data = {
                "archivos": [text_based.decode()],
                "tipo":self.type_.upper(),
                "cantidad":1,
                "company_id":self.id_company
            }
            response = requests.post(self.url_webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            #print(json.dumps(data))
            if response.status_code == 200:
                self.LoginPageConnection = True
                SendEmailProcess(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito")
                SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Archivo {self.type_} finalizado con exito")
            else:
                SendEmailProcess(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")
                SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error al enviar el archivo {self.type_} : codigo {str(response.status_code)}")
                self.LoginPageConnection = True
            os.remove(self.nombre_actual) 
        elif self.type_ == "xml":
            try:#FACTURAS
                with open(PathFile,'rb') as archivo:
                    texto = archivo.read()
                text_based = base64.b64encode(texto)
                self.dataXML.append(text_based.decode())
                os.remove(PathFile)
            except:#COMPROBANTES
                PathComprobante = os.path.expanduser("~")+"/Downloads/Comprobante de Retención.xml"
                with open(PathComprobante,'rb') as archivo:
                    texto = archivo.read()
                text_based = base64.b64encode(texto)
                self.dataXML.append(text_based.decode())
                os.remove(PathComprobante)
            time.sleep(3)
        else:
            SendEmailProcess(self.company_Name,"Descarga SRI",f"Error en el archivo: Verifique el tipo de arhivo (TXT,XML)")
            SendEmailProcessSecond(self.company_Name,"Descarga SRI",f"Error en el archivo: Verifique el tipo de arhivo (TXT,XML)")
class DBMysql():
    def __init__(self):
        try: 
            self.mydb = mysql.connector.connect(
            host="172.105.153.61",
            user="forge",
            password="CCfRNQT9fbx6lnJ5DYoI",
            database="Sivo_Security"
            )
            if self.mydb.is_connected():
                self.SelectDB()   
        except:
            print("Error en el conexion con la base de datos")
            pass
    def SelectDB(self):

        CountNumberBD = 1
        
        mycursorCount = self.mydb.cursor()
        mycursorCount.execute("SELECT COUNT(*) FROM conexion_sri")
        myresultCount = mycursorCount.fetchone()[0]

        
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM conexion_sri")
        myresult = mycursor.fetchall()

        for x in myresult:
            if x[8] == "A":
                
                SendEmailProcess(x[3],"Descarga SRI",f"Se ha iniciado la descarga de archivos [{CountNumberBD}/{myresultCount}]")
                SendEmailProcessSecond(x[3],"Descarga SRI",f"Se ha iniciado la descarga de archivos [{CountNumberBD}/{myresultCount}]")
                print(f"{CountNumberBD}/{myresultCount}")
                WebScrapingSRI(x[1],x[2],x[4],x[5],x[7],x[6],x[3])
            
                CountNumberBD = CountNumberBD+1
            else:
                continue

        self.mydb.close()

DBMysql()
            