# В стране проходят выборы президента. Каждый житель старше 18 лет может отдать
# свой голос за одного из кандидатов. Вам необходимо написать программу для подсчёта голосов.
# Для каждого кандидата, за которого проголосовал хоть кто-нибудь, выведите его фамилию и
# через пробел количество отданных за него голосов. Упорядочьте кандидатов по убыванию числа голосов.
# При равенстве числа голосов выведите фамилии в лексикографическом порядке.
# Каждую фамилию нужно вывести ровно один раз.

peoples, peoples_array = {}, []

print("Количество бюллетеней:")
kol_bul = int(input())

for i in range(kol_bul):
    print("Кандидат, отмеченный","во" if i == 1 else "в", i+1, "бюллетени:")
    data = input()
    peoples[data] = peoples.get(data, 0) + 1

for name, count in peoples.items():
    peoples_array.append([name, count])

peoples_array.sort(key=lambda x:  (-x[1], x[0]))

print("\nИтоги голосования")
for pair in peoples_array: print(pair[0], pair[1],"голоса" if pair[1] == 2 else "голос")
