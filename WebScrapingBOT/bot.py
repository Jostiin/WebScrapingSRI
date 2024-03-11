#BIBLIOTECA
from bs4 import BeautifulSoup
import requests



class WebScraping:
    def __init__(self):
        self.url = "https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT"
        self.ConectionPage(self.url)
    def ConectionPage(self,url):
        try:
            self.req = requests.get(url)
            self.bs4HTML = BeautifulSoup(self.req.text,"html.parser")
            print("Conexion exitosa")
            
        except requests.exceptions.ConnectionError:
            print("Error de conexion")
    def AunthenticationCaptChat(self):
        print(self.bs4HTML.prettify())
        #CAPTHA_img = self.bs4HTML.find("img", alt = "Red dot")
        CAPTHA_img = self.bs4HTML.find_all("img")
        print(CAPTHA_img)


#data = bs4HTML.find_all(class_ = "ui-tabview-title")

#data = bs4HTML.title

#print(bs4HTML.prettify())
            
WebScraping()