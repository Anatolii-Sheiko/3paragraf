def ancient_cipher(l):
    password = ""

    # Перебираем все возможные пары чисел от 1 до l
    for i in range(1, l):
        for j in range(i + 1, l): # Пары только с j > i
            if l % (i + j) == 0: # Если 1 делится на сумму пары
                password += str(i) + str(j)

    return password

# Вод данных
l = int(input("Введите число от 3 до 20: "))
if 3 <= l <= 20:
    result = ancient_cipher(l)
    print(f"Пароль для числа {l}: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")

