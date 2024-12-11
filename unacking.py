def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'HARD', False]
values_dict = {'a': 4, 'b': 'Ivan', 'c': 175.5}
print_params(*values_list)
print_params(**values_dict)

# values_list_2 = ['what', 1234.1234]
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)

# Важно!
#
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
#
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
#
# def a(my_list = [])) – это приводит к ошибкам!