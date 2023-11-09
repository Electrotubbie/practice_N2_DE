import pandas as pd
import msgpack
import json
import pickle
import os
# ссылка на скачивание файла для анализа
# https://catalog.data.gov/dataset/real-estate-sales-2001-2018
PATH = 'task5/'
FILE_NAME = 'Real_Estate_Sales_2001-2020_GL.csv'
ANALYSE_NUMS_PATH = f'{PATH}analyse_nums/'
ANALYSE_LABELS_PATH = f'{PATH}analyse_labels/'
# чтение исходного файла и подготовка к анализу
df = pd.read_csv(f'{PATH}{FILE_NAME}').set_index('Serial Number').sort_index()
df = df.drop(columns=['Address', 'Non Use Code','Assessor Remarks', 'OPM remarks', 'Location'])
df['List Year'] = df['List Year'].astype(str)
# получение информации по столбцам с числами
stats_numbers = df.describe().loc[['mean', 'min', 'max', 'std']]
for col in stats_numbers.columns:
    stats_numbers.loc['sum', col] = sum(df[col])
# сохранение файлов
stats_numbers.to_csv(f'{ANALYSE_NUMS_PATH}stats_numbers.csv')
stats_numbers.to_json(f'{ANALYSE_NUMS_PATH}stats_numbers.json')
stats_numbers.to_pickle(f'{ANALYSE_NUMS_PATH}stats_numbers.pkl')
with open(f'{ANALYSE_NUMS_PATH}stats_numbers.msgpack', 'wb') as f:
    msgpack.dump(stats_numbers.to_dict(), f)
# получение информации по текстовым столбцам с метками
stats_labels_cols = ['List Year', 'Property Type', 'Residential Type']
stats_labels = dict()
for col in stats_labels_cols:
    stats_labels[col] = df[col].value_counts().to_dict()
# сохранение файлов
stats_labels_df = pd.DataFrame().from_dict(stats_labels)
stats_labels_df.to_csv(f'{ANALYSE_LABELS_PATH}stats_labels.csv')
with open(f'{ANALYSE_LABELS_PATH}stats_labels.json', 'w') as f:
    json.dump(stats_labels, f)
with open(f'{ANALYSE_LABELS_PATH}stats_labels.pkl', 'wb') as f:
    pickle.dump(stats_labels, f)
with open(f'{ANALYSE_LABELS_PATH}stats_labels.msgpack', 'wb') as f:
    msgpack.dump(stats_labels, f)
# сравнение размеров файлов
for file in os.scandir(ANALYSE_NUMS_PATH):
    print(file.name, os.path.getsize(file))
print()
for file in os.scandir(ANALYSE_LABELS_PATH):
    print(file.name, os.path.getsize(file))   