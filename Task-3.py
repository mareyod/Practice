# Найдите сумму квадратов чисел из введённого набора чисел, представленных в виде диапазона.
# Например, если введены номера «2 4», то нужно найти сумму чисел, расположенных в диапазоне со 2 по 4.

print("Введите набор чисел через пробел:")
numbers = [int(i) for i in input().split()]
print("Какой отрезок нужно возвести в квадрат и просуммировать?")
range = [int(i) for i in input().split()]
print("Сумма квадратов чисел из указанного набора:")
print(sum((i)**2 for i in numbers[range[0]-1:range[1]]))

