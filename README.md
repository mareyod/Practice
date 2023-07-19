Имеется ряд словарей с пересекающимися ключами (значения — положительные числа). Напишите 2 функции, которые делают с массивом словарей следующие операции:

Первая функция max_dct(*dicts) формирует новый словарь по правилу:

Если в исходных словарях есть повторяющиеся ключи, выбираем среди их значений максимальное и присваиваем этому ключу (например, в словаре_1 есть ключ «а» со значением 5, и в словаре_2 есть ключ «а», но со значением 9. Выбираем максимальное значение, т. е. 9, и присваиваем ключу «а» уже в новом словаре). Если ключ не повторяется, то он просто переносится со своим значением в новый словарь (например, ключ «с» встретился только у одного словаря, а у других его нет. Следовательно, переносим в новый словарь этот ключ вместе с его значением). Сформированный словарь возвращаем. 

Вторая функция sum_dct(*dicts) суммирует значения повторяющихся ключей. Значения остальных ключей остаются исходными. (Проводятся операции по аналогу первой функции, но берутся не максимумы, а суммы значений одноименных ключей). Функция возвращает сформированный словарь.
