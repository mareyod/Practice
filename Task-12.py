# Имеется ряд словарей с пересекающимися ключами (значения — положительные числа).
# Напишите 2 функции, которые делают с массивом словарей следующие операции:
# Первая функция max_dct(*dicts) формирует новый словарь по правилу:
# Если в исходных словарях есть повторяющиеся ключи, выбираем среди их значений максимальное и
# присваиваем этому ключу (например, в словаре_1 есть ключ «а» со значением 5, и в словаре_2 есть ключ «а»,
# но со значением 9. Выбираем максимальное значение, т. е. 9, и присваиваем ключу «а» уже в новом словаре).
# Если ключ не повторяется, то он просто переносится со своим значением в новый словарь (например, ключ «с»
# встретился только у одного словаря, а у других его нет. Следовательно, переносим в новый словарь этот ключ
# вместе с его значением). Сформированный словарь возвращаем.
# Вторая функция sum_dct(*dicts) суммирует значения повторяющихся ключей.
# Значения остальных ключей остаются исходными. (Проводятся операции по аналогу первой функции,
# но берутся не максимумы, а суммы значений одноименных ключей). Функция возвращает сформированный словарь.


first_dict, second_dict = {}, {}

print("Количество пар ключ-значение в 1 словаре:")
count_first_dict = int(input())
print("Введите содержимое 1 словаря в формате ключ-значение:")
for i in range(count_first_dict):
    data = input().split()
    first_dict.update({data[0]: int(data[1])})

print("Количество пар ключ-значение во 2 словаре:")
count_second_dict = int(input())
print("Введите содержимое 2 словаря в формате ключ-значение:")
for i in range(count_second_dict):
    data = input().split()
    second_dict.update({data[0]: int(data[1])})

all_keys = list(set(list(first_dict.keys())) | set(list(second_dict.keys())))

def none_max (a,b):
    if a is None:
        return b
    if b is None:
        return a
    return max(a,b)
def max_dct(dict1,dict2):
    return {k: none_max(dict1.get(k), dict2.get(k)) for k in all_keys}
def none_sum (a,b):
    if a is None:
        return b
    if b is None:
        return a
    return a+b
def sum_dct(dict1,dict2):
    return {k: none_sum(dict1.get(k), dict2.get(k)) for k in all_keys}


print("\nСодержимое 1 словаря:")
[ print(key , ":" , value, end = ", ") for (key, value) in sorted(first_dict.items(), key = lambda k: k[0])]
print("\b\b\nСодержимое 2 словаря:")
[ print(key , ":" , value, end = ", ") for (key, value) in sorted(second_dict.items(), key = lambda k: k[0])]

print("\b\b\n\nРезультат работы функции max_dct:")
[ print(res[0], ":" , res[1], end = ", ") for res in sorted(max_dct(first_dict,second_dict).items(), key = lambda k: k[0])]
print("\b\b\nРезультат работы функции sum_dct:")
[ print(res[0], ":" , res[1], end = ", ") for res in sorted(sum_dct(first_dict,second_dict).items(), key = lambda k: k[0])]
print("\b\b ")
