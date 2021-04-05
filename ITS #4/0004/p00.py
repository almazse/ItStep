for i in range(100):
    if i % 2 == 0:
        continue
    print(i)
    if i == 13:
        print("цикл досрочно завершен")
        break
