import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    np_array = np.array(list)
    np_array = np_array.reshape((3, 3))

    for i in range(2):
        calculations['mean'].append(np_array.mean(axis=i).tolist())
        calculations['variance'].append(np_array.var(axis=i).tolist())
        calculations['standard deviation'].append(np_array.std(axis=i).tolist())
        calculations['max'].append(np_array.max(axis=i).tolist())
        calculations['min'].append(np_array.min(axis=i).tolist())
        calculations['sum'].append(np_array.sum(axis=i).tolist())

    calculations['mean'].append(float(np_array.mean()))
    calculations['variance'].append(float(np_array.var()))
    calculations['standard deviation'].append(float(np_array.std()))
    calculations['max'].append(int(np_array.max()))
    calculations['min'].append(int(np_array.min()))
    calculations['sum'].append(int(np_array.sum()))

    return calculations
