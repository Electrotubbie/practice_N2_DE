import json
import pickle

VARIANT = 37
PATH = 'task4/'
INPUT_PKL_FILE = f'products_{VARIANT}.pkl'
INPUT_JSON_FILE = f'price_info_{VARIANT}.json'
MOD_PKL_FILE = f'mod_products_{VARIANT}.pkl'

def refresh_price(product: dict, price_info: dict) -> dict:
    method = price_info['method']
    # if method == 'add': рудимент вордовского задания
    if method == 'sum':
        product['price'] += price_info['param']
    elif method == 'sub':
        product['price'] -= price_info['param']
    elif method == 'percent+':
        product['price'] *= 1 + price_info['param']
    elif method == 'percent-':
        product['price'] *= 1 - price_info['param']
    else:
        raise ValueError(f'{method} метода нет!')
    product['price'] = round(product['price'], 2)
    return product

with open(f'{PATH}{INPUT_JSON_FILE}', 'r') as f_json:
    price_info_list = json.load(f_json)
with open(f'{PATH}{INPUT_PKL_FILE}', 'rb') as f_pkl:
    products = pickle.load(f_pkl)
# преобразование информации об изменении цен в удобный вид
prices_info = dict()
for info in price_info_list:
    prices_info[info['name']] = info
# обновление цен
refreshed_products = list()
for product in products:
    new_product = refresh_price(product, prices_info[product['name']])
    refreshed_products.append(new_product)

with open(f'{PATH}{MOD_PKL_FILE}', 'wb') as f_pkl:
    pickle.dump(refreshed_products, f_pkl)