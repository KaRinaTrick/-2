def calculate_structure_sum(*data_structure):
    s = 0
    for i in data_structure:
        if isinstance(i, str):
            s += len(i)
        elif isinstance(i, int):
            s += i
        elif isinstance(i, float):
            s += i
        elif isinstance(i, bool):  # True = 1, False = 0
            s += i
        elif isinstance(i, dict):
            s += calculate_structure_sum(*list(i.items()))
        elif isinstance(i, list):
            s += calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            s += calculate_structure_sum(*i)
        elif isinstance(i, set):
            s += calculate_structure_sum(*i)
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
    True,
    2.5,
    [2.4, 2.90, 6.78]
]
result = calculate_structure_sum(data_structure)

print(result)
