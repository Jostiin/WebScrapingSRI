from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ua = UserAgent(browsers=['chrome'])
randomAgent = ua.random
options = Options()
options.page_load_strategy = 'eager'
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument(f'user-agent={randomAgent}')

test_driver = webdriver.Chrome(options=options)

test_driver.get('https://www.google.com/recaptcha/api2/demo')

print(randomAgent)
