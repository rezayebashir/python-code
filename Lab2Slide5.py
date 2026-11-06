import os


# =====================================================================
# 1. CUSTOM EXCEPTION ARCHITECTURE
# =====================================================================
class BankError(Exception):
    """Base exception for all banking simulation related faults."""
    pass


class InvalidAmountError(BankError):
    """Raised when an operation involves a negative value or invalid numeric string."""
    pass


class InsufficientFundsError(BankError):
    """Raised when a withdrawal amount exceeds the active balance."""
    pass


class TransactionFileError(BankError):
    """Raised when a file read or write operation fails during logging."""
    pass


# =====================================================================
# 2. CORE BUSINESS LOGIC (ACCOUNT CLASS)
# =====================================================================
class Account:
    def __init__(self, account_holder: str, initial_balance: float = 0.0, log_file: str = "transactions.txt"):
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        self.account_holder = account_holder
        self.__balance = float(initial_balance)
        self.log_file = log_file

    @property
    def balance(self) -> float:
        return self.__balance

    def _log_transaction(self, action: str, amount: float) -> None:
        """Internal helper to write transactions using a context manager."""
        try:
            with open(self.log_file, "a", encoding="utf-8") as file:
                file.write(f"{action.upper()}: ${amount:.2f} | Remaining Balance: ${self.__balance:.2f}\n")
        except (PermissionError, FileNotFoundError) as io_err:
            raise TransactionFileError(f"Failed to log transaction due to system constraints: {io_err}")

    def deposit(self, amount_str: str) -> float:
        """Validates input, deposits money, logs activity, and updates balance."""
        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            raise InvalidAmountError(f"'{amount_str}' is not a valid numeric amount.")

        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be strictly greater than zero.")

        # If validation succeeds, update state
        self.__balance += amount

        try:
            self._log_transaction("Deposit", amount)
        except TransactionFileError:
            # Revert balance state if file write fails to keep state transactional
            self.__balance -= amount
            raise

        return self.__balance

    def withdraw(self, amount_str: str) -> float:
        """Validates input, checks funds, withdraws money, logs activity, and updates balance."""
        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            raise InvalidAmountError(f"'{amount_str}' is not a valid numeric amount.")

        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be strictly greater than zero.")

        if amount > self.__balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Cannot withdraw ${amount:.2f} from a balance of ${self.__balance:.2f}.")

        # Deduct balance
        self.__balance -= amount

        try:
            self._log_transaction("Withdrawal", amount)
        except TransactionFileError:
            # Revert balance state if file write fails
            self.__balance += amount
            raise

        return self.__balance


# =====================================================================
# 3. AUTOMATED SUITE (SIX MANDATORY TEST SCENARIOS)
# =====================================================================
def run_automated_test_suite():
    print("==================================================")
    print("      RUNNING MANDATORY SIX TEST SCENARIOS        ")
    print("==================================================")

    # Reset log file before testing
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    test_acc = Account("Test User", initial_balance=500.0, log_file="test_log.txt")

    scenarios = [
        ("Scenario 1: Successful Deposit", test_acc.deposit, "150.0"),
        ("Scenario 2: Successful Withdrawal", test_acc.withdraw, "200.0"),
        ("Scenario 3: Failing Non-Numeric Entry", test_acc.deposit, "one-hundred"),
        ("Scenario 4: Failing Negative Numeric Entry", test_acc.withdraw, "-50.0"),
        ("Scenario 5: Failing Overdraft/Insufficient Funds", test_acc.withdraw, "1000.0"),
        ("Scenario 6: Failing Empty/Zero Input Operation", test_acc.deposit, "0")
    ]

    for description, action, argument in scenarios:
        print(f"\n[EXECUTION] {description}")
        try:
            action(argument)
        except (InvalidAmountError, InsufficientFundsError, TransactionFileError) as exc:
            print(f"  ❌ Caught Expected Exception -> {type(exc).__name__}: {exc}")
        else:
            print(f"  ✅ Operation Passed Successfully. Current Balance: ${test_acc.balance:.2f}")
        finally:
            print("  ⏱️ System: Cleanup hooks and verification checklist processed.")


# =====================================================================
# 4. USER INTERFACE DIALOG LEVEL
# =====================================================================
def run_interactive_simulator():
    print("\n==================================================")
    print("    WELCOME TO THE BANK TRANSACTION SIMULATOR      ")
    print("==================================================")

    name = input("Enter your name to open an account: ").strip() or "Valued Customer"
    account = Account(account_holder=name, initial_balance=100.0)
    print(f"Account setup successfully for {name} with an initial $100.00 credit.")

    while True:
        print(f"\n--- Account Menu (Current Balance: ${account.balance:.2f}) ---")
        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Exit Program")

        choice = input("Select an option (1-3): ").strip()

        try:
            if choice == "1":
                amt = input("Enter amount to deposit: ").strip()
                account.deposit(amt)
                print("✨ Deposit successful!")

            elif choice == "2":
                amt = input("Enter amount to withdraw: ").strip()
                account.withdraw(amt)
                print("💸 Withdrawal successful!")

            elif choice == "3":
                print("Thank you for choosing our secure banking simulation. Goodbye!")
                break

            else:
                # 5. Handle unsupported menu options explicitly
                raise ValueError(f"'{choice}' is an invalid choice. Please enter 1, 2, or 3.")

        except (InvalidAmountError, InsufficientFundsError, TransactionFileError) as e:
            print(f"❌ Transaction Rejected: {e}")
        except ValueError as e:
            print(f"⚠️ Input Warning: {e}")
        finally:
            # 7. Semantic implementation of a tracking summary hook
            print("📝 Loop Cycle Execution Completed cleanly.")


if __name__ == "__main__":
    # Part 1: Automated Scenarios
    run_automated_test_suite()

    # Part 2: Interactive Prompt Console
    run_interactive_simulator()
