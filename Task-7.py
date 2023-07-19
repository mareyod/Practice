# Напишите программу, которая производит вычисление выражения, 
# записанного в обратной польской нотации (ОПН).

stack = []

print("Введите выражение, записанное в обратной польской нотации:")
for i in (input().split()):
    if i not in ['+', "-", "*", "/"]:
        stack += [int(i)]
    else:
        if i == '+':
            stack[-2] = stack[-1] + stack[-2]
            del stack[-1]
        if i == '-':
            stack[-2] = stack[-2] - stack[-1]
            del stack[-1]
        if i == '*':
            stack[-2] = stack[-1] * stack[-2]
            del stack[-1]
        if i == '/':
            stack[-2] = stack[-2] / stack[-1]
            del stack[-1]
print("Ответ:", stack[0])

