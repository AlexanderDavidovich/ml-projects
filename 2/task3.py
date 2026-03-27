print('Введите поочередно возраст каждого посетителя (пустая строка для окончания):')
data = []
price = 0

while True:
    line = input()
    if line == "":
        break
    else:
        data.append(int(line))

for age in data:
    if age < 3:
        continue
    elif 3 <= age < 12:
        price += 4.50
    elif age >= 65:
        price += 8.25
    else:
        price += 12.75

print(f"общая цена билетоа для всех посетителей: {price}")