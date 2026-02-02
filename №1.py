n = int(input()) #Добавлено int(), иначе выводит ошибку
product = 1 #Начальное значение для произведения
if n > 0: #Обрабатываем все цифры, включая последнюю
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
