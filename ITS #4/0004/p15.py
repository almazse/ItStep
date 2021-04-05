
def display_deposit(PV=1000.0, n=5, r=0.1, target=10000.0):
    for i in range(n + 1):
        FV = PV * (1 + r) ** i
        print(f"{i} - {FV:,.2f} USD")
        if FV >= target:
            print("Досрочное закрытие депозита")
            break
    else:
        print("все прошло по плану")


if __name__ == '__main__':
    PV = 2000.0
    n = 9
    r = 0.15
    target=15000.0
    display_deposit(PV=PV, n=n, r=r, target=target)
