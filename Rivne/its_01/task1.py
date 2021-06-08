try:
    spending = int(input("Enter spending: "))
    cost = float(input("Enter cost: "))
    distance = float(input("Enter distance: "))
    if spending <= 0 or cost <= 0 or distance <=0:
        raise ValueError

    money = spending / 100 * distance * cost

    print(f"You must pay {money} UAH")
except ValueError:
    print("\nERROR! Uncorrect value!")
