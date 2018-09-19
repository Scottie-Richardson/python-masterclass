import datetime
import pytz


class Account:
    # Simple account class with balance

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if  0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The withdraw amount must be greater that zero and no more than the account balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is ${:,.2f}".format(self._balance), end='\n\n')

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:17,.2f} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    scottie = Account("Scottie", 85000)
    scottie.show_balance()

    print("Deposit lottery winnings ... $500,000,000")
    scottie.deposit(500000000)

    print("Purchase a 2019 Corvette Z06 ... $120,000")
    scottie.withdraw(120000)

    print("Purchase an island ... $50,000,000")
    scottie.withdraw(50000000)

    print("Purchase a private jet ... $2,500,000")
    scottie.withdraw(2500000)

    print("Purchase a 340' yacht ... $220,000,000")
    scottie.withdraw(220000000)

    print("Purchase a helicopter for yacht ... $1,700,000")
    scottie.withdraw(1700000)

    print("Pay taxes, maintanice, fuel and assorted costs for 10 years ... $225,764,700")
    scottie.withdraw(225764700)

    print("Purchase an airline ticket home to finish college ... $295")
    scottie.withdraw(295)

    print("Purchase a cheeseburger at airport ... $15")
    scottie.withdraw(15)

    scottie.show_transactions()
