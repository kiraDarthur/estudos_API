from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurando o navegador
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e configurado corretamente

# URL da página do Google Images
url = 'https://www.google.com/search?sca_esv=85af15397c77c0f6&sxsrf=ACQVn09SnjsMF1ERxZ78gpgZwvz1STUwDQ:1709041107923&q=one+piece&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjYqpOh0suEAxUrhv0HHY8ACeIQ0pQJegQIGRAB&biw=1164&bih=827&dpr=1.1#imgrc=_OOmh9l_-4p5kM'

# Abrindo a página
driver.get(url)

# Aguardando um curto período de tempo para as imagens carregarem (você pode ajustar esse tempo conforme necessário)
time.sleep(5)

# Encontrando a primeira imagem na página
first_image = driver.find_element(By.XPATH, '//div[@id="islrg"]//img')

# Obtendo a URL da imagem
image_url = first_image.get_attribute('src')

# Baixando a imagem
response = requests.get(image_url)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    with open('imagem_downloaded.png', 'wb') as f:
        f.write(response.content)
    print("Imagem baixada com sucesso!")
else:
    print("Erro ao baixar a imagem:", response.status_code)

# Fechando o navegador
driver.quit()
