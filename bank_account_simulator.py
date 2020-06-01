class BankAccount:
    next_acc_number = 1

    def __init__(self):
        self.number = self.next_acc_number
        BankAccount.next_acc_number += 1
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount
            return self.cash
        else:
            return "Wartosc nie moze byc dodana, podaj poprawna wartosc"

    def withdraw_cash(self, amount):
        if amount > self.cash:
            cash2 = self.cash
            self.cash = 0
            return cash2
        else:
            self.cash -= amount
            return amount

    def print_info(self):
        return f'Numer konta: {self.number}, stan konta: {self.cash}'


if __name__ == '__main__':
    a = BankAccount()
    b = BankAccount()
    c = BankAccount()
    d = BankAccount()
    e = BankAccount()
    f = BankAccount()
    g = BankAccount()
    h = BankAccount()
    a.deposit_cash(123)
    b.deposit_cash(4232)
    c.deposit_cash(1233)
    d.deposit_cash(6433)
    e.deposit_cash(87635)
    print(a.print_info())
    print(b.print_info())
    print(c.print_info())
    print(d.print_info())
    print(e.print_info())
    print(f.print_info())
    print(g.print_info())
    print(h.print_info())
