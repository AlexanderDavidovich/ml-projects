a, b, c = map(int, input('введите три стороны трегуольника: ').split())

def triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    elif a > b + c or b > a + c or c > a + b:
        return False
    else:
        return True

if triangle(a, b, c):
    print('треугольник существует')
else:
    print('треугольник не существует')