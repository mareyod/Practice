# Саша с Олей — лучшие друзья, и учатся в одном классе уже восемь лет.
# Каждый год они соревнуются, кто получит оценки лучше.
# Для этого они сравнивают оценки в конце каждого учебного года.
# Победитель вычисляется по средней оценке по каждому предмету, который они проходили в этом году.
# Например, если по математике Саша за год получила пять четвёрток и пять пятёрок,
# то её средняя оценка 4,5, так как (4+4+4+4+4+5+5+5+5+5) / 10 = 4,5. Если же Оля получила
# за год по математике тройку, семь четвёрок и только две пятёрки, то Саша победила,
# так как средняя оценка Оли составила 4,1 (убедитесь в этом!)
# Для каждого предмета узнайте, кто выиграл в этом году — Саша или Оля.


olga, sasha = {}, {}

print("Количество предметов, которые проходили Саша с Олей в этом году:")
count = int(input())

print("Оценки Саши за год по следующим предметам:")
for i in range(count):
    data = input().split()
    sasha.update({data[0]:sum([int(i) for i in data[1:]])/len(data[1:])})

print("Оценки Оли за год по следующим предметам:")
for i in range(count):
    data = input().split()
    olga.update({data[0]:sum([int(i) for i in data[1:]])/len(data[1:])})
results = []

print("\nСредний балл Саши по следующим предметам:")
for subject in sorted(sasha.items(), key = lambda x: x[0]):
    print(subject[0], round(subject[1], 1))
print("\nСредний балл Оли по следующим предметам:")
for subject in sorted(olga.items(), key = lambda x: x[0]):
    print(subject[0], round(subject[1], 1))

print("\nЛучшие результаты за год по предметам:")
for subject, mark in sorted(sasha.items(), key = lambda x: x[0]):
    if sasha[subject] == olga[subject]: results.append(subject + " ничья")
    elif sasha[subject] < olga[subject]: results.append(subject + " Оля")
    elif sasha[subject] > olga[subject]: results.append(subject + " Саша")

for item in results: print(item)
