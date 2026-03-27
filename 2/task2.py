volume = int(input('введите уровень шума:'))
arr = [("Отбойный молоток", 130),
        ("Газовая газонокосилка", 106),
        ("Будильник", 70),
        ("Тихая комната", 40)]

found = False
for i in range(4):
    if volume == arr[i][1]:
        print(f"ваш уровень шума ощущается как: {arr[i][0]}")
        found = True
        break

if not found:
    if volume > 130:
        print('уровень шума даже выше чем у отбойного молотка!')
    elif volume < 40:
        print('уровень шума ниже чем в тихой комнате!')
    else:
        for i in range(3):
            if volume < arr[i][1] and volume > arr[i+1][1]:
                print(f'ваш уровень звука находится между {arr[i][0]} и {arr[i+1][0]}4')