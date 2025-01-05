num_1 = 10
num_2 = 3
result = num_1 + num_2
print(type(num_1))
print(result)
print(round(10/3))

print(5/2)

# a = int(input())
# b = int(input())
# result = a + b
# print(result)

dohod = int(150)
ns = int(18)
profit = dohod * (100 - ns) / 100
print(int(profit))

num = 1
stepen = 5
result = num ** stepen
print(result)

num = 10.1234
chislo_znakov = 2
result = round(num, chislo_znakov)
print(result)

a = 5
b = 4
c = 16
print(max(a, b, c))
print(min(a, b, c))
print(int((a + b + c) / 3))


var_1 = "Hello"
var_2 = "World"
print(var_1)
print(var_1[:4])
print(var_1[::2])
print(var_1[-2])
print(var_1 + var_2)
print((var_1 * 2) + (var_2 * 3))

first = "hello"
second = 55
print(str(first) + " " + str(second))

var_1 = "***Звездочки***"
var_2 = "*"
message = var_1 + var_2
print(message.strip(var_2))

var_1 = "HeLlo"
var_2 = "WoRlD"
message = var_1 + " " + var_2
print(var_1.upper() + " " + var_2.lower())

movie = "title"
age = 1994
print(f"Фильму {movie} в 2024 году исполнится {2024 - age}")

cash = int(35000)
dollar_rate = int(93)
euro_rate = int(101)
print(f'У пользователя в наличии {cash} рублей, за них он может получить {cash//dollar_rate} долларов или {cash//euro_rate} евро')
