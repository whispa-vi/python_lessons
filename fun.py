# num_1 = 10
# num_2 = 20
# result = num_2 + num_1
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_2 + num_1
# print(result)
#чтобы не писать повторяющиеся строчки кода можно создать фкц sum

def summ(num_1, num_2): #def - создание функции
    result = num_1 + num_2
    print(result)

summ(10, 20)
summ(30, 40)

name = "Vika"
def hi(name, age):
    print("Меня зовут " + name + " мне " + age + " лет")

hi(name, "40")

# ФУНКЦИЯ ВСЕГД должна что-то возвращать
name_1 = "Aleks"
age = "39"
def person(name_1, age):
    result = name_1 + " " + age
    #print(result)
    return result

h = person(name_1, age)
#person(name,age)
print(h)
