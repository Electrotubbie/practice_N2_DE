import pandas as pd
import msgpack
import os

VARIANT = 37
PATH = 'task3/'
INPUT_JSON_FILE = f'products_{VARIANT}.json'
OUTPUT_JSON_FILE = f'products_result_{VARIANT}.json'
OUTPUT_MSGPACK_FILE = f'products_result_{VARIANT}.msgpack'

df = pd.read_json(f'{PATH}{INPUT_JSON_FILE}')
grouped = df.groupby(['name']) # группировка столбца 'name'
stats = grouped.describe()['price'][['mean', 'min', 'max']].reset_index() # извлечение необходимых значений из описания сгруппированного датасета
stats = stats.rename(columns={'mean': 'avr'}).reindex(columns=['name', 'max', 'min', 'avr']) # приведение структуры к требуемой
stats.to_json(f'{PATH}{OUTPUT_JSON_FILE}', orient='records') # сохранение датасета в json файл
# подготовка датасета для сохранения в msgpack
product_stats = [
    {
        'name': row['name'],
        'max': row['max'],
        'min': row['min'],
        'avr': row['avr']
    }
    for i, row in stats.iterrows()
]
# сохранение в msgpack
with open(f'{PATH}{OUTPUT_MSGPACK_FILE}', 'wb') as f:
    msgpack.dump(product_stats, f)
# сверка объёмов
print(f'json    = {os.path.getsize(f"{PATH}{OUTPUT_JSON_FILE}")}')
print(f'msgpack = {os.path.getsize(f"{PATH}{OUTPUT_MSGPACK_FILE}")}')