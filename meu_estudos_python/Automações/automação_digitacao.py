from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

nav = webdriver.Chrome()
nav.get("https://www.typingstudy.com/")
nav.maximize_window()
sleep(2)
nav.find_element(By.ID, "username").send_keys('*******')
nav.find_element(By.ID, "password").send_keys('********')
nav.find_element(By.CLASS_NAME, "shadow_btn").click()

input("Digite Enter para fechar")

