str_1 = "Hello"
str_2 = "WORLD"
print(str_1)
# print(dir(str_1))
print(str_1.upper()) #переводит букву в верхний регист
print(str_1.title()) #переводит перувю букву в верхний регист
print(str_2.lower()) #переводит буквы в нижний регист

name = "Ivan"
a = "Hello {}" #{} область, куда помещаем нашу переменную
result = a.format(name)
print(result)

first_name = "Ivan"
last_name = "Ivanov"
a = '{} {}'
result = a.format(first_name, last_name)
print("My name: " + result)

result = f'{first_name} {last_name}' #вместо строк 23 и 24
print(result)