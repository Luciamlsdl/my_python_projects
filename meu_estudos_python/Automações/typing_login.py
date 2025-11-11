# typing_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from dotenv import load_dotenv
import os

# Carrega variáveis do .env para os.environ
load_dotenv()

# Pega as credenciais do .env
USER = os.getenv("TYPING_USER")
PASS = os.getenv("TYPING_PASS")

if USER is None or PASS is None:
    raise SystemExit("Variáveis TYPING_USER ou TYPING_PASS não encontradas no .env")

# Inicializa o ChromeDriver automático (webdriver-manager baixa/atualiza o driver)
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # descomente se quiser rodar sem abrir janela (sem interface)
nav = webdriver.Chrome(service=service, options=options)

try:
    nav.get("https://www.typingstudy.com/")
    nav.maximize_window()
    sleep(2)
    nav.find_element(By.ID, "username").send_keys(USER)
    nav.find_element(By.ID, "password").send_keys(PASS)
    nav.find_element(By.CLASS_NAME, "shadow_btn").click()

    input("Digite Enter para fechar")  # pausa para ver o resultado
finally:
    nav.quit()
