import numpy as np


def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    np_array = np.array(input_list).reshape((3, 3))

    calculations = {key: [] for key in ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']}

    for axis in [0, 1, None]:
        calculations['mean'].append(np_array.mean(axis=axis).tolist())
        calculations['variance'].append(np_array.var(axis=axis).tolist())
        calculations['standard deviation'].append(np_array.std(axis=axis).tolist())
        calculations['max'].append(np_array.max(axis=axis).tolist())
        calculations['min'].append(np_array.min(axis=axis).tolist())
        calculations['sum'].append(np_array.sum(axis=axis).tolist())

    return calculations
