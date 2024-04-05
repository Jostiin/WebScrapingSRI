import undetected_chromedriver as uc
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import json
import time
print("empieza")

options = uc.ChromeOptions()
options.add_argument("--password-store=basic")
options.add_experimental_option(
        "prefs",{
            "credentials_enable_service":False,
            "profile.password_manager_enabled":False
        }
    )
driver = uc.Chrome(headless=False,options=options)


driver.get("https://www.google.com/recaptcha/api2/demo?invisible=true")

url = "https://www.google.com/recaptcha/api2/demo?invisible=true"

api = "83a82cc9461e57e8b1883ec0a6b8aaff"

sitekey = "6LfP0CITAAAAAHq9FOgCo7v_fb0-pmmH9VW3ziFs"


url1 = f"https://2captcha.com/in.php?key={api}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}"
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
time.sleep(5)
driver.execute_script('document.getElementById("frmPrincipal").submit();')
time.sleep(10)
input()