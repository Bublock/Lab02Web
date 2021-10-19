def work4():
    value = int(input('Введите число : '))
    a = value / 2
    b = (a + value / a) / 2
    while b != a:
        a = b
        b = (a + value / a) / 2
    print('Квадратный корень числа',value,'равен: ', a)
    return a
work4()