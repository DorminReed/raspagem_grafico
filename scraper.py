from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_price(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') #opcional
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        time.sleep(3) # tempo para carregar

        price_element = driver.find_element(By.CLASS_NAME, "finalPrice")
        price_text = price_element.text.strip().replace("R$", "").replace(".", "").replace(",", ".")
        return float(price_text)
    except Exception as e:
        print(f"Erro ao buscar preço: {e}")
        return None
    finally:
        driver.quit()
    