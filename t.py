from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("https://sapiens.dti.ufv.br/sapiens_crp/CheckLogin.asp") 
time.sleep(2)
username = browser.find_element_by_id("Usuario")
password = browser.find_element_by_id("Senha")
username.send_keys("user")
password.send_keys("password")
browser.find_element_by_id("Login").click()
for i in range(3):
    time.sleep(2)
    if browser.title == "Sistema de Controle de Acesso":
        username = browser.find_element_by_id("Usuario")
        password = browser.find_element_by_id("Senha")
        username.send_keys("user")
        password.send_keys("password")
        browser.find_element_by_id("Login").click()
        #print('Inseri os dados {}'.format(i+1) + ' vez.')
pageAvaliacoes = browser.get("https://sapiens.dti.ufv.br/sapiens_crp/aluno/avaliacoes.asp?n=601040066")
nota = browser.find_element_by_xpath('/html/body/center/p[1]/table/tbody/tr[5]/td[13]/font/b').text
newNota = 35
if(nota != newNota):
    time.sleep(2)
    browser.execute_script("alert('Nota atualizada');")
time.sleep(4)
browser.quit()

