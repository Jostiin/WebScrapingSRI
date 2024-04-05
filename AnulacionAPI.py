from fastapi import FastAPI
import time
import random
from pydantic import BaseModel
import json

import undetected_chromedriver as uc
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



class scrapingAnulacion:
    def __init__(self,ruc,password,ci,tipo,fecha,clave,no,receptor,correo):
        self.driver = self.Driver()

        self.ruc = ruc
        self.password = password
        self.ci = ci

        self.fecha = fecha
        self.clave = clave
        self.no = no
        self.receptor = receptor
        self.correo = correo

        self.Ingresar_element_login_sri()
        self.Ingresar_keys_login_sri()
        self.Ingresar_menu_FacturacionElctronica_sri()
        self.Ingresar_anulacion_solicitudanulacion(self.fecha, self.clave, self.no, self.receptor, self.correo)
        self.Ingresar_anulacion_SolicitudAnulacioncomprobantes()
        input()
        pass
    def Driver(self):
        options = uc.ChromeOptions()
        options.add_argument("--password-store=basic")
        #options.add_argument('--headless=new')
        #options.add_argument('--disable-gpu')
    
        options.add_experimental_option(
            "prefs",{
                "credentials_enable_service":False,
                "profile.password_manager_enabled":False
            }
        )
    
        '''
        options = Options()
        options.page_load_strategy = 'eager'
        #options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
        driver = webdriver.Chrome(options=options)
        '''
        driver = uc.Chrome(headless=False,use_subprocess=False,options=options)
        driver.get("https://srienlinea.sri.gob.ec/")
        return driver
    def Ingresar_element_login_sri(self):
        pausa = random.uniform(4,8)
        time.sleep(pausa)
        element_Iniciar_Sesion = WebDriverWait(self.driver,60).until(ec.element_to_be_clickable((By.XPATH,"//a[@href='/sri-en-linea/contribuyente/perfil']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action = ActionChains(self.driver).move_to_element(element_Iniciar_Sesion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action.click().perform() 
    def Ingresar_keys_login_sri(self):
        # TODO: Ingreso de RUC
        pausa = random.uniform(4,8)
        time.sleep(pausa)
        e_ruc = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='usuario']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_ruc = ActionChains(self.driver).move_to_element(e_ruc)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_ruc.click().perform() 
        e_ruc.send_keys(self.ruc)
        
        # TODO: Ingreso de CEDULA OPCIONAL
        pausa = random.uniform(3,5)
        time.sleep(pausa)
        e_cedula = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='ciAdicional']")))
        pausa = random.uniform(3,5)
        time.sleep(pausa)
        action_cedula = ActionChains(self.driver).move_to_element(e_cedula)
        pausa = random.uniform(3,5)
        time.sleep(pausa)
        action_cedula.click().perform() 
        e_cedula.send_keys(self.ci)
    
        # TODO: Ingreso de PASSWORD
        pausa = random.uniform(3,5)
        time.sleep(pausa)
        e_password = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='password']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_password = ActionChains(self.driver).move_to_element(e_password)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_password.click().perform() 
        e_password.send_keys(self.password)
        # TODO: INGRESAR
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_btnSubmit = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@value='Ingresar']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_btnSubmit = ActionChains(self.driver).move_to_element(e_btnSubmit)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_btnSubmit.click().perform() 
    def Ingresar_menu_FacturacionElctronica_sri(self):
  
        # TODO: Seleccionar seccion Facturación Electrónica
        pausa = random.uniform(4,8)
        time.sleep(pausa)
        e_btnFacturacion = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//button[@title='Facturación Electrónica']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_btnFacturacion = ActionChains(self.driver).move_to_element(e_btnFacturacion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_btnFacturacion.click().perform() 
        # TODO: Ingreso a produccion
        '''
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_produccion = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//a[@class='ui-menuitem-link ui-corner-all ng-tns-c13-35 ng-star-inserted']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_produccion = ActionChains(self.driver).move_to_element(e_produccion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_produccion.click().perform()
        '''
        # TODO: Ingreso a anulacion
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_anulacion = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//a[@href='https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=61&idGrupo=58']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_anulacion = ActionChains(self.driver).move_to_element(e_anulacion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_anulacion.click().perform()
    def Ingresar_anulacion_solicitudanulacion(self,fecha,clave,no,receptor,correo):
        # TODO: Ingreso a solicitud de anulacion comprobantes
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        urlpath = "mojarra.jsfcljs(document.getElementById(\'consultaDocumentoForm\'),{\'consultaDocumentoForm:j_idt19\':\'consultaDocumentoForm:j_idt19\'},\'\');return false04/04/2024"
        e_solicitudAnulacion = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,f"//a[text()='Solicitud de anulación comprobantes']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_solicitudAnulacion = ActionChains(self.driver).move_to_element(e_solicitudAnulacion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_solicitudAnulacion.click().perform()
        # TODO: Seleccionar Tipo de comprobante
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_tipocomprobante = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//select[@id='frmPrincipal:cmbTipoComprobante']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_tipocomprobante = ActionChains(self.driver).move_to_element(e_tipocomprobante)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_tipocomprobante.click().perform() 
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        select_tipocomprobante = Select(e_tipocomprobante)
        select_tipocomprobante.select_by_visible_text("Factura")
        # TODO: Ingresar de fecha de autorizacion
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_fechaautorizacion = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:calendarFechaAutorizacion_input']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_fechaautorizacion = ActionChains(self.driver).move_to_element(e_fechaautorizacion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_fechaautorizacion.click().perform() 
        e_fechaautorizacion.send_keys(fecha)
        # TODO: Ingresar de clave acceso
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_claveAcceso = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:itxtClaveAcceso']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_claveAcceso = ActionChains(self.driver).move_to_element(e_claveAcceso)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_claveAcceso.click().perform() 
        e_claveAcceso.send_keys(clave)
        # TODO: Ingresar de no autorizacion
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_NoAutorizacion = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:itxtNoAutorizacion']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_NoAutorizacion = ActionChains(self.driver).move_to_element(e_NoAutorizacion)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_NoAutorizacion.click().perform() 
        e_NoAutorizacion.send_keys(no)
        # TODO: Ingresar de Identificacion receptor
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        e_IdentificacionReceptor = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:itxtIdentificacion']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_IdentificacionReceptor = ActionChains(self.driver).move_to_element(e_IdentificacionReceptor)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_IdentificacionReceptor.click().perform() 
        e_IdentificacionReceptor.send_keys(receptor)
        # TODO: Ingresar de correo electronico
        pausa = random.uniform(4,8)
        time.sleep(pausa)
        e_correoReceptor = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:itxtCorreoElectronico']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_correoReceptor = ActionChains(self.driver).move_to_element(e_correoReceptor)
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_correoReceptor.click().perform() 
        e_correoReceptor.send_keys(correo)
        # TODO: SOLICITAR
        pausa = random.uniform(5,7)
        time.sleep(pausa)
        e_btnSolicitar = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:btnAceptar']")))
        pausa = random.uniform(3,7)
        time.sleep(pausa)
        action_btnSolicitar = ActionChains(self.driver).move_to_element(e_btnSolicitar)
        pausa = random.uniform(2,5)
        time.sleep(pausa)
        action_btnSolicitar.click().perform()
    def Ingresar_anulacion_SolicitudAnulacioncomprobantes(self):
        try:
            pausa = random.uniform(3,7)
            time.sleep(pausa)
            e_btnEnviar = WebDriverWait(self.driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='frmPrincipal:btnEnviar']")))
            pausa = random.uniform(3,7)
            time.sleep(pausa)
            action_btnEnviar = ActionChains(self.driver).move_to_element(e_btnEnviar)
            pausa = random.uniform(3,7)
            time.sleep(pausa)
            action_btnEnviar.click().perform()
        except:
            datos = {
                'message': 'Pagina no encontrada',
            }
            return datos
        # TODO: Aceptar alerta
        pausa = random.uniform(4,8)
        time.sleep(pausa)
        alert = WebDriverWait(self.driver,30).until(ec.alert_is_present())
        alert.accept()
        return True


# Crear la aplicación FastAPI
app = FastAPI()
class Values(BaseModel):
    Ruc: str
    Password: str
    Ci: str
    Tipo: str
    Fecha: str
    Clave: str
    No: str
    Receptor: str
    Correo: str
# Definir una ruta con un método POST
@app.post("/anulacion")
def obtener_datos_ejemplo(values: Values):
    #///print(values.Tipo)
    datos = scrapingAnulacion(values.Ruc,values.Password,values.Ci,values.Tipo,values.Fecha,values.Clave,values.No,values.Receptor,values.Correo)
    
    return datos

# Ejecutar la aplicación con el servidor uvicorn
if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)