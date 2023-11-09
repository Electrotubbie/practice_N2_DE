import numpy as np
import os

VARIANT = 37
PATH = 'task2/'
INPUT_MATRIX_FILE = f'matrix_{VARIANT}_2.npy'
POINTS_FILE = f'points_{VARIANT}'
POINTS_ZIP_FILE = f'points_zip_{VARIANT}'

min_value = 500 + VARIANT
matrix = np.load(f'{PATH}{INPUT_MATRIX_FILE}')

x = np.empty(0)
y = np.empty(0)
z = np.empty(0)

for i, row in enumerate(matrix):
    for j, digit in enumerate(row):
        if digit > min_value:
            x = np.append(x, i)
            y = np.append(y, j)
            z = np.append(z, digit)

np.savez(f'{PATH}{POINTS_FILE}', x=x, y=y, z=z)
np.savez_compressed(f'{PATH}{POINTS_ZIP_FILE}', x=x, y=y, z=z)

print(f'points     = {os.path.getsize(f"{PATH}{POINTS_FILE}.npz")}')
print(f'points_zip = {os.path.getsize(f"{PATH}{POINTS_ZIP_FILE}.npz")}')