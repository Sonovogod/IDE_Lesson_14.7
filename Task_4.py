def rever_number(n):
    rever_int = 0
    num_int = int(n)
    num_float = n - int(n)

    while num_int > 0:
        rever = (rever_int + num_int % 10) * 10
        num_int //= 10
    rever_int //= 10


    return rever

number = float(input('Введите число: '))
rever_num = rever_number(number)

print('Первое число наоборот: ', rever_num)
print('Второе число наоборот: ')
print('Сумма: ')
