import os
from pathlib import Path


# ==========================================
# 1. CUSTOM EXCEPTION LAYER
# ==========================================
class InvalidAmountError(ValueError):
    """Raised when a transactional monetary value is negative or zero."""
    pass


class InsufficientFundsError(Exception):
    """Raised when a withdrawal attempt exceeds the active account balance."""
    pass


# ==========================================
# 2. CORE DOMAIN MODEL LAYER
# ==========================================
class Account:
    LOG_FILE = Path("transaction_history.txt")

    def __init__(self, account_number: str, initial_balance: float = 0.0) -> None:
        self.account_number = account_number
        if initial_balance < 0:
            raise InvalidAmountError("Initial starting balance cannot be negative.")
        self._balance = float(initial_balance)

    @property
    def balance(self) -> float:
        return self._balance

    def _log_transaction(self, operation: str, amount: float) -> None:
        """Appends a recorded action row to the log file.

        Demonstrates low-level error handling for file operations.
        """
        try:
            # Open with append flag using a context manager
            with self.LOG_FILE.open(mode="a", encoding="utf-8") as file:
                file.write(
                    f"Account: {self.account_number} | Operation: {operation:<8} | Amount: ${amount:<8.2f} | End Balance: ${self._balance:.2f}\n")
        except (PermissionError, IOError) as file_err:
            # We do not suppress this silently, we output a clear alert warning
            print(f"  [SYSTEM WARNING] Failed to commit audit trail log entry to disk: {file_err}")

    def deposit(self, amount: float) -> float:
        """Credits an account balance if given an amount greater than zero."""
        if amount <= 0:
            raise InvalidAmountError(f"Deposit value ${amount:.2f} must be strictly positive.")

        self._balance += amount
        self._log_transaction("DEPOSIT", amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Debits an account balance after verifying limit criteria thresholds."""
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal value ${amount:.2f} must be strictly positive.")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Insufficient funds on {self.account_number}. Requested: ${amount:.2f} | Current: ${self._balance:.2f}")

        self._balance -= amount
        self._log_transaction("WITHDRAW", amount)
        return self._balance


# ==========================================
# 3. TRANSACTION PROCESS ROUTER (try/except/else/finally)
# ==========================================
def execute_transaction_flow(account: Account, menu_choice: str, raw_amount_input: str) -> None:
    """Processes financial operations through rigorous input validation loops,

    demonstrating proper semantic usage of try-except-else-finally blocks.
    """
    print(f"Executing: Choice '{menu_choice}' with Input Amount: '{raw_amount_input}'")

    try:
        # Validate menu options selection
        supported_options = {"1": "deposit", "2": "withdraw"}
        if menu_choice not in supported_options:
            raise ValueError(f"Menu choice '{menu_choice}' is not valid or supported.")

        # Validate numeric user input conversion
        amount = float(raw_amount_input)

        # Route operational execution matching conditions
        if menu_choice == "1":
            account.deposit(amount)
        elif menu_choice == "2":
            account.withdraw(amount)

    # Specific, granular catching layers to prevent broad hidden exception states
    except ValueError as val_err:
        print(f"  [INPUT / MENU ERROR] Parsing failed: {val_err}")
    except InvalidAmountError as amt_err:
        print(f"  [TRANSACTION ERROR] Rejected: {amt_err}")
    except InsufficientFundsError as fund_err:
        print(f"  [BALANCE ERROR] Transaction Blocked: {fund_err}")

    # Executed ONLY when the try scope processes flawlessly without exceptions
    else:
        print(f"  [SUCCESS] Transaction confirmed! New Balance: ${account.balance:.2f}")

    # Executed EVERY SINGLE TIME regardless of success or caught error failures
    finally:
        print("  [AUDIT] Action block processed.")


# ==========================================
# 4. COMPREHENSIVE TEST SUITE RUNNER
# ==========================================
if __name__ == "__main__":
    # Clean output tracking paths before starting demo
    if Account.LOG_FILE.exists():
        Account.LOG_FILE.unlink()

    # Initializing target test record
    customer_acc = Account(account_number="ACC-9945", initial_balance=500.00)

    print("======================================================================")
    print("           STARTING BANKING SIMULATOR TEST RUN EXECUTIONS             ")
    print("======================================================================")

    # Scenario 1: Successful Deposit
    print("\n--- [SCENARIO 1: SUCCESSFUL DEPOSIT] ---")
    execute_transaction_flow(customer_acc, menu_choice="1", raw_amount_input="250.50")

    # Scenario 2: Successful Withdrawal
    print("\n--- [SCENARIO 2: SUCCESSFUL WITHDRAWAL] ---")
    execute_transaction_flow(customer_acc, menu_choice="2", raw_amount_input="100.00")

    # Scenario 3: Failing Non-Numeric Character Values Input
    print("\n--- [SCENARIO 3: FAIL — INVALID NON-NUMERIC INPUT] ---")
    execute_transaction_flow(customer_acc, menu_choice="1", raw_amount_input="two_hundred")

    # Scenario 4: Failing Negative/Zero Amount Entry Bounds
    print("\n--- [SCENARIO 4: FAIL — INVALID NEGATIVE AMOUNT RANGE] ---")
    execute_transaction_flow(customer_acc, menu_choice="2", raw_amount_input="-50.00")

    # Scenario 5: Failing Over-Withdrawal Beyond Account Capital
    print("\n--- [SCENARIO 5: FAIL — INSUFFICIENT BALANCE FUNDS] ---")
    execute_transaction_flow(customer_acc, menu_choice="2", raw_amount_input="1500.00")

    # Scenario 6: Failing Unsupported Choice Menu Routing Options
    print("\n--- [SCENARIO 6: FAIL — UNSUPPORTED SELECTION MENU CODE] ---")
    execute_transaction_flow(customer_acc, menu_choice="9", raw_amount_input="50.00")

    print("\n======================================================================")
    print("                     FINAL TRANSACTION HISTORY LOG                    ")
    print("======================================================================")
    if Account.LOG_FILE.exists():
        print(Account.LOG_FILE.read_text().strip())
    print("======================================================================")
