from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicia o GeckoDriver (Firefox)
driver = webdriver.Firefox()

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Espera você escanear o QR code
input("Escaneie o QR Code e pressione Enter para continuar...")

# Lê contatos do arquivo
with open("contatos.txt", "r", encoding="utf-8") as file:
    contatos = [linha.strip() for linha in file]

# Mensagem a ser enviada
mensagem = "Olá! Esta é uma mensagem automática da nossa imobiliária 😊"

# Função para enviar mensagem
def enviar_mensagem(contato, mensagem):
    try:
        # Campo de pesquisa
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.send_keys(contato)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        
        # Campo de mensagem
        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        msg_box.send_keys(mensagem)
        msg_box.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para: {contato}")
        time.sleep(2)
        
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato}: {e}")

# Envia a mensagem para todos os contatos
for contato in contatos:
    enviar_mensagem(contato, mensagem)

# Fecha o navegador ao final
driver.quit()
