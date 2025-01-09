from Tools.scripts.generate_re_casefix import alpha
from six import integer_types

student = ["Vika", "Sofi", "Alex", "Nick", "Mari", "Franco"]

# 1
for f in student:
    print(f)

# 2
for f in student:
    var = "Engineer " + f
    print(var)

# 3
for f in student:
    if f == "Vika":
        var = "Automation Engineer " + f
        print(var)

# 4
for f in student[3:]:
    print(f)

# 5
for f in student:
    print(len(f))

# 6 Счетчик итераций
iteration_count = 0
for name in student:
    iteration_count += 1
    print(f"Всего итераций: {iteration_count}")

# 7
iteration_count = 0
for name in student:
    if "i" in name:
        print(f"В имени {name} есть 'i'")
        iteration_count += 1

print(f"Кол-во элементов, которые содержат букву 'i': {iteration_count}")

# 8 Функция enumerate()
for i, name in enumerate(student):
    print(f"Итерация {i}: {name}")

# 9 Сумма элементов списка через цикл for
numbers = [1, 2, 3]
sum_elements = 0 # Создание переменной для хранения суммы
for element in numbers:
    sum_elements += element # Добавляем текущий элемент к сумме

print(f"Сумма всех элементов списка: {sum_elements}")

# 10 вывести все нечетные числа до 10
for i in range(1, 10, 2):
    print(i)

# 2.15.2.1 код, который выводит квадраты чисел от 1 до 5
for numbers in range(1, 6):
    print(numbers**2)

print("# 2.15.2.1 код, который выводит квадраты чисел от 1 до 3")
numbers = [1, 2, 3]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)

# print("# 2.15.3 выведите на печать сумму всех элементов списка")
# numbers = list(map(int, input().split()))
# sum_elements = 0
# for element in numbers:
#     sum_elements += element
#
# print(sum_elements)
#
# print("# 2.15.4 на входе принимает список из нескольких чисел, "
#       "записанных в одну строчку через пробел. Выводить на печать все четные числа")
# numbers = list(map(int, input().split()))
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

print("# 2.15.5 Выводите на печать сумму всех четных чисел списка")
numbers = [1, 2, 3, 4]
sum_elements = 0
for number in numbers:
    if number % 2 == 0:
        sum_elements += number

print(sum_elements)

print("# 2.15.6 Выводите на печать каждый элемент списка с его индексом")
films = ["Матрица", "Скала", "Схватка", "Бэтман"]
for i, film in enumerate(films):
    print(f"Индекс {i}: {film}")

print("# 2.15.7 Выводите на печать сумму количества букв элементов")
films = ["Матрица", "Скала", "Схватка", "Бэтман"]
sum_elements = 0
for f in films:
    sum_elements += len(f)

print(sum_elements)
print("------------------------")

print("# 2.15.8 Выводите на печать результат умножения на 7 элементов списка")
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number*7)

print("------------------------")
# или
numbers = [1, 2, 3, 4]
for numb in numbers:
    f = numb * 7
    print(f)

print("------------------------")

print("# 2.15.9 Код должен выводить элементы списка с четными индексами")
numbers = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110,]
for i, number in enumerate(numbers):
    if i % 2 == 0:
        print(number)

print("------------------------")

print("# 2.15.10 Код должен вывести на печать среднее арифметическое число по списку")
numbers = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110,]
average = sum(numbers) / len(numbers)
print(average)

print("------------------------")

print("# 2.15.11 Код должен вывести на печать только буквы")
element = '1abracad5bra'
for f in element:
    if f.isalpha():
        print(f)

print("------------------------")

print("# 2.15.12 Код должен вывести на печать количество раз, которое встречается данная буква в исходной строке")
element = '1abracad5bra'
iteration_count = 0
letter = 'b'
for f in element:
    if letter in f:
        iteration_count += 1
print(iteration_count)

print("------------------------")

print("# 2.15.13 , который принимает одно значениe в виде строки, "
      "с помощью цикла for, посчитает количество раз, "
      "которое встречаются в данной строке буквы - a, b, i. Ответ должен быть в виде суммы")
element = '1abracad5bra'
iteration_count = 0
a = 'a'
b = 'b'
c = 'i'
for f in element:
    if a in f:
        iteration_count += 1
    if b in f:
        iteration_count += 1
    if c in f:
        iteration_count += 1

print(iteration_count)

print("------------------------")