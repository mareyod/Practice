# Вы работаете над крупным интернет-сервисом с богатой историей. 
# Требования к логину, который выбирает пользователь, уже много лет 
# не меняются: логин должен содержать только буквы, цифры и символ подчёркивания «_». 
# Однако с первых месяцев работы вашего сервиса в базе данных до сих пор 
# остаётся «наследство»: «плохие» логины, не удовлетворяющие этим требованиям.
# Поскольку ваша компания заботится об интересах клиентов, отвечающий за эту проблему 
# менеджер решил распечатать аккуратный список всех некорректных логинов и подумать 
# над каждым из них, чтобы предложить обладателю этого логина наиболее подходящую замену. 
# Составьте для менеджера аккуратно сформатированный список.
# Выводятся все логины, не удовлетворяющие описанным в условии требованиям. 
# Каждый логин выводится на отдельной строке. Порядок — алфавитный.

print("Введите набор логинов через запятую")
passwords = [i for i in input().split(',')]
valid = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбюQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_'
out = []
for pas in passwords:
    for i in range(len(pas)):
        if not pas[i] in valid:
            out += [pas]
            break
out.sort()
print("\nЛогины, не удовлетворяющие требованиям:")
for i in out:
    print(i)
