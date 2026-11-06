from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self._balance = initial_balance  # Encapsulated attribute

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"[{self.account_number}] Deposited: ${amount:.2f}. New Balance: ${self._balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        print(f"[{self.account_number}] Withdrew: ${amount:.2f}. New Balance: ${self._balance:.2f}")

    @abstractmethod
    def calculate_end_of_month(self) -> float:
        """Abstract method to calculate financial fees or benefits."""
        pass

    def __str__(self) -> str:
        return f"Account {self.account_number} | Balance: ${self._balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number: str, initial_balance: float, interest_rate: float = 0.02):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_end_of_month(self) -> float:
        # Benefits: Earns interest on the current balance
        interest_earned = self._balance * self.interest_rate
        self._balance += interest_earned
        return interest_earned


class CurrentAccount(Account):
    def __init__(self, account_number: str, initial_balance: float, monthly_fee: float = 12.00):
        super().__init__(account_number, initial_balance)
        self.monthly_fee = monthly_fee

    def calculate_end_of_month(self) -> float:
        # Fees: Monthly maintenance charge deducted
        if self._balance >= self.monthly_fee:
            self._balance -= self.monthly_fee
            return -self.monthly_fee
        else:
            # Simple handling if balance cannot cover fee
            actual_fee = self._balance
            self._balance = 0.0
            return -actual_fee


# --- Demonstration of Polymorphism ---
if __name__ == "__main__":
    # Create a heterogeneous list of accounts
    accounts: list[Account] = [
        SavingsAccount("SAV-1001", 5000.0, interest_rate=0.03),  # 3% interest
        CurrentAccount("CUR-2002", 1500.0, monthly_fee=15.00),  # $15 fee
        SavingsAccount("SAV-1002", 10000.0)  # Default 2% interest
    ]

    print("--- Processing Balance Changes ---")
    accounts[0].deposit(500.0)
    accounts[1].withdraw(200.0)
    print()

    print("--- Processing End of Month Polymorphically ---")
    for acc in accounts:
        # Polymorphic call to calculate_end_of_month
        adjustment = acc.calculate_end_of_month()

        if adjustment > 0:
            print(f"{acc.account_number}: Earned ${adjustment:.2f} in interest.")
        else:
            print(f"{acc.account_number}: Charged ${abs(adjustment):.2f} in monthly fees.")

        # Implicitly calling overridden __str__
        print(f" Updated status: {acc}\n")
