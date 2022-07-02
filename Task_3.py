def summ_num(n):
    if n < 0:
        print('Ошибка, число не положительное')
    else:

        ansver_summ = 0
        while n > 0:
            ansver_summ += n % 10
            n //= 10
        return ansver_summ


def count_num(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


number = int(input('Введите число: '))
summ_number = summ_num(number)
count_number = count_num(number)

print('\n\nСумма чисел:', summ_number)
print('Кол-во цифр в числе:', count_number)
print('Разность суммы и кол-ва цифр:', summ_number - count_number)