import json
from scraper import get_price
import csv
from datetime import datetime

# Carrega os produtos a partir do JSON
with open("products.json") as f:
    products = json.load(f)

# Função para salvar o histórico no CSV
def salvar_historico(nome_produto, preco):
    with open("precos.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), nome_produto, preco])

# Loop principal: coleta e salva os preços
for product in products:
    current_price = get_price(product['url'])
    if current_price is not None:
        print(f"{product['name']} - R${current_price:.2f}")
        salvar_historico(product['name'], current_price)

