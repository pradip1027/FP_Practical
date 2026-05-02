import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")


class BankAccount:
    MIN_BALANCE = 1000

    def __init__(self, customer_name, account_type, balance):
        self.customer_name = customer_name
        self.account_type = account_type.lower()
        self.balance = 0
        self.setbalance(balance)

    def setbalance(self, amount):
        if amount < self.MIN_BALANCE:
            raise ValueError(f"Minimum balance of {self.MIN_BALANCE} must be maintained.")
        self.balance = amount

    def getbalance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        new_balance = self.balance - amount
        if new_balance < self.MIN_BALANCE:
            raise ValueError(f"Minimum balance of {self.MIN_BALANCE} must be maintained.")

        self.balance = new_balance

    def show_info(self):
        print("\nCustomer Name :", self.customer_name)
        print("Account Type  :", self.account_type)
        print("Balance       :", self.getbalance())


def create_account():
    name = input("Enter customer name :: ")

    while True:
        account_type = input("Enter account type (saving or current):: ").strip().lower()
        if account_type in ("saving", "current"):
            break
        print("Error: Account type must be either saving or current.")

    while True:
        try:
            starting_balance = int(input("Enter Starting Balance: "))
            return BankAccount(name, account_type, starting_balance)
        except ValueError as err:
            print(f"Error: {err}")


def main():
    account = create_account()

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Show Info")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a valid numeric choice.")
            continue

        if choice == 1:
            try:
                amount = int(input("Enter deposit amount: "))
                account.deposit(amount)
                print("Amount deposited successfully.")
            except ValueError as err:
                print(f"Error: {err}")
        elif choice == 2:
            try:
                amount = int(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print("Amount withdrawn successfully.")
            except ValueError as err:
                print(f"Error: {err}")
        elif choice == 3:
            account.show_info()
        elif choice == 4:
            print("Thank you for banking with us.")
            break
        else:
            print("Error: Please choose from options 1 to 4.")


if __name__ == "__main__":
    main()