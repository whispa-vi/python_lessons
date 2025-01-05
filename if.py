age = 40
name = "Vika"
if age == 25 and name == "Vika":
    print(f"Мне {age} и меня зовут {name}")
elif age > 25:
    print("Мне больше 25")
else:
    print("Мне меньше 25 лет")

age = 40
name = "Vika"
if age == 25 or name == "Vika":
    print(f"Мне {age} и меня зовут {name}")
else:
    print("Мне меньше 25 лет")


name = "Vika"
if "V" in name == "Vika":
    print(f"Моё имя {name}")
else:
    print(f"Моё имя не {name}")
#
# pin = 1234
# print("Введите, пожалуйста, Ваш пин-код")
# user_pin = int(input())
#
# if pin == user_pin:
#     print("Введите сумму для снятия наличных")
# else:
#     print("Ошибка, Вы ввели неверный пин-код. У Вас осталось 2 попытки")
#     user_pin = int(input())
#     if pin == user_pin:
#         print("Введите сумму для снятия наличных")
#     else:
#         print("Ошибка, Вы ввели неверный пин-код. У Вас осталось 1 попытка")
#         user_pin = int(input())
#         if pin == user_pin:
#             print("Введите сумму для снятия наличных")
#         else:
#             print("Ошибка, Ваша карта заблокирована. Обратитеть в отделение банка")
#
#
# num_1 = int(input())
# num_2 = int(input())
# if num_1 > 0:
#     print(f"{num_1}")
# elif num_2 > 0:
#     print(f"{num_2}")
# else:
#     print(f"{num_1} и {num_2} < or = 0")
#
#
# num_1 = int(input())
# num_2 = int(input())
# if num_1 > 0:
#     print(float(num_1))
# elif num_2 > 0:
#     print(float(num_2))
# else:
#     print(float(num_1) + " и " + float(num_2))

# выведите на печать большее значение
# num_1 = float(input())
# num_2 = float(input())
# if num_1 > num_2:
#     print(f"{num_1}")
# elif num_2 > num_1:
#     print(f"{num_2}")
# else:
#     print(f"{num_1} и {num_2} равны")


# выведите на печать значение, в котором есть слово Python.
# input_text_1 = "I am learning Python"
# input_text_2 = "I know Python"
# if "Python" in input_text_1 and "Python" in input_text_2:
#     print(input_text_1)
#     print(input_text_2)
# elif "Python" in input_text_1:
#     print(f"{input_text_1}")
# elif "Python" in input_text_2:
#     print(f"{input_text_2}")
# else:
#     print(f"Никто не любит Python")


# Если число четное - разделите его на 4
# Если число нечетно - умножьте на 3
# num_1 = float(input())
# if num_1 % 2 == 0:
#     print(num_1 / 4)
# elif num_1 % 2 == 1:
#     print(num_1 * 3)
# else:
#     print(f"nothing")


# Если число меньше 18 - вывести сообщение - Рано
# Если число находится в диапазоне от 18 до 28 включительно  - вывести сообщение  - Пора
# Если число больше 28 - вывести сообщение - Поздно
number = 29
if number < 18:
    print("Рано")
elif 18 <= number <= 28:
    print("Пора")
else:
    print("Поздно")


# выведите на печать значение, в котором есть слова с буквами t или w.
input_text_1 = "I am learning Pyhon"
input_text_2 = "I kno Pyhon"
if "t" in input_text_1.lower() or "w" in input_text_1.lower():
    print(input_text_1)

if "t" in input_text_2.lower() or "w" in input_text_2.lower():
    print(input_text_2)

if not ("t" in input_text_1.lower() or "w" in input_text_1.lower() or "t" in input_text_2.lower() or "w" in input_text_2.lower()):
    print("Никто не любит Python")
