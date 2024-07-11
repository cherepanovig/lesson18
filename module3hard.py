#Универсальное решение для подсчёта суммы всех чисел и длин всех строк


def calculate_structure_sum(data_structure):
    sum_data = 0
    if isinstance(data_structure, (list, tuple, set)): # Если это список, кортеж, множество
        for item in data_structure:
            sum_data += calculate_structure_sum(item) # Рекурсивный вызов функции, для суммирования разных типов элементов
    elif  isinstance(data_structure, str): # Если это строка - сумма по длине строки
        sum_data += len(data_structure)
    elif isinstance(data_structure, (int, float)): # Если это число - сумма по значениям
        sum_data += data_structure
    elif isinstance(data_structure, dict): # Если это словарь
        for key, value in data_structure.items():
            sum_data += calculate_structure_sum(key) # Рекурсивный вызов функции, для суммирования разных типов элементов
            sum_data += calculate_structure_sum(value)
    return sum_data


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)