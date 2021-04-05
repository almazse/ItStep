max, count_max, num_cons, number, num_input, i = 0, 0, 0, 0, 0, 1

while True:
    x = int(input("число: "))
    if x == 0:
        break
    else:
        if x > max:
            max = x
            count_max = 1
        elif x == max:
            count_max += 1

        if num_input == x:
            i += 1
        else:
            if num_cons < i:
                number = num_input
                num_cons = i
            i = 1
    num_input = x

print(f"Максимальное значение: число {max} встречается {count_max} раза")
print(f"Самая длинная серия: число {number} подряд {num_cons} раза")
