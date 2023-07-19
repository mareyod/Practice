# Используя списочное выражение и подходящую стандартную функцию,
# найдите длину самого длинного из введённых слов.

print("Введите текст:")
words = input().split()
data = [(i,len(i)) for i in words]
longest = max(data, key = lambda x: x[1])
print("Самое длинное слово:", longest[0], "-", longest[1], "символов")
