class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(self.__balance)

account = BankAccount()

account.deposit(5000)

account.withdraw(1000)

account.show_balance()


# | Encapsulation                        | Description                                                             |   |
# | ------------------------------------ | ----------------------------------------------------------------------- | - |
# | **Encapsulation**                  | Bundling data (variables) and methods that operate on the data into a single unit called a class. |   |
# | **Private Members**                  | Variables/methods prefixed with `__` (e.g., `__var`); not directly accessible from outside the class. |   |
# | **Public Members**                   | Default members; directly accessible.                                   |   |
# | **Protected Members**                | Variables/methods prefixed with `_`; accessible within the class and subclasses. |   |
# | **Access Modifiers**                 | Not strictly enforced in Python; achieved through naming conventions (`_`, `__`). |   |
# | **Getter and Setter Methods**        | Methods used to access and modify private data.                         |   |
# | **`@property` Decorator**           | Pythonic way to create getters, setters, and deleters.                 |   |
# | **Name Mangling**                    | Python automatically modifies `__var` to `_ClassName__var` for name privacy. |   |