from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time
from selenium.webdriver.firefox.options import Options

# Configurações do Firefox para otimização
options = Options()
options.set_preference("permissions.default.image", 2)  # Desabilita o carregamento de imagens
options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")  # Desabilita o Flash

# Inicializa o navegador Firefox com as opções de otimização
driver = webdriver.Firefox(options=options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda o usuário escanear o QR Code
input("Escaneie o QR Code e pressione Enter para continuar...")

# Lê os contatos do arquivo
with open("contatos.txt", "r", encoding="utf-8") as file:
    contatos = [linha.strip() for linha in file]

# Mensagem que será enviada
mensagem = "Olá! Esta é uma mensagem automática da nossa imobiliária 😊"

# Configura espera do WebDriver
wait = WebDriverWait(driver, 30)

# Função para enviar a mensagem
def enviar_mensagem(numero, mensagem):
    try:
        # Codifica a mensagem para a URL
        texto_codificado = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto_codificado}"

        # Vai para o link específico de cada número
        driver.get(link)

        # Espera o botão de enviar ficar visível
        botao_enviar = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[@aria-label="Enviar"]')
        ))

        # Espera extra para garantir que o botão esteja pronto para ser clicado
        time.sleep(2)

        # Clica no botão de enviar usando JavaScript (para evitar elementos sobrepostos)
        driver.execute_script("arguments[0].click();", botao_enviar)
        print(f"✅ Mensagem enviada para: {numero}")
        time.sleep(2)

    except Exception as e:
        print(f"❌ Erro ao enviar mensagem para {numero}: {e}")

# Envia mensagem para todos os contatos
for contato in contatos:
    if contato:
        enviar_mensagem(contato, mensagem)

# Fecha o navegador após o envio
driver.quit()
