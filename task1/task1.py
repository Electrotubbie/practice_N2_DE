import numpy as np
import json

VARIANT = 37
PATH = 'task1/'
INPUT_MATRIX_FILE = f'matrix_{VARIANT}.npy'
MATRIX_DATA_FILE = f'matrix_data_{VARIANT}.json'
NORM_MATRIX_FILE = f'normilized_matrix_{VARIANT}.npy'

matrix = np.load(f'{PATH}{INPUT_MATRIX_FILE}')
m_data = dict()
m_data['sum'] = np.sum(matrix) # сумма всех элементов матрицы
m_data['avr'] = np.mean(matrix) # среднее значение всех элементов матрицы
m_data['sumMD'] = np.trace(matrix) # сумма элементов на главной диагонали
m_data['avrMD'] = m_data['sumMD'] / len(matrix.diagonal()) # среднее элементов на главной диагонали
m_upside_down = matrix[::-1] # отражённая по вертикали матрица
m_data['sumSD'] = np.trace(m_upside_down) # сумма элементов на побочной диагонали
m_data['avrSD'] = m_data['sumSD'] / len(m_upside_down.diagonal()) # среднее элементов на побочной диагонали
m_flatten = matrix.flatten() # вектор из всех значений матрицы
m_data['max'] = max(m_flatten) # максимальное значение
m_data['min'] = min(m_flatten) # минимальное значение

# преобразование типов данных для сериализации и сохранения в json
m_data_json = {key: float(m_data[key]) for key in m_data.keys()}
with open(f'{PATH}{MATRIX_DATA_FILE}', 'w') as f:
    json.dump(m_data_json, f)

# нормализация матрицы
norm_matrix = np.zeros(np.shape(matrix))
for i, row in enumerate(matrix):
    for j, digit in enumerate(row):
        norm_matrix[i][j] = digit / m_data['sum']

# на самом деле если взять сумму всех элементов нормализованной матрицы,
# то у меня получилось следующее:

# >>> sum(norm_matrix.flatten())
# 1.0000000000000007

# полагаю, данная погрешность не является критичной

np.save(f'{PATH}{NORM_MATRIX_FILE}', norm_matrix)