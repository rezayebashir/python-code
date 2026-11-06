# --- Define Custom Exception Type ---
class InvalidOperationError(Exception):
    """Raised when the user inputs an operator that is not supported by the calculator."""
    pass


def run_safe_calculator():
    print("==================================================")
    print("          Welcome to the Safe Calculator          ")
    print("==================================================\n")

    # Infinite loop to keep running so the user can retry or perform new operations
    while True:
        print("--- Start of Calculation Attempt ---")
        try:
            # 1 & 3. Ask for two numeric values and handle invalid numeric inputs
            num1_input = input("Enter the first numeric value (or type 'exit' to quit): ").strip()
            if num1_input.lower() == 'exit':
                print("\nExiting the Safe Calculator. Goodbye!")
                break

            num2_input = input("Enter the second numeric value: ").strip()

            # Convert inputs to floats, which automatically raises a ValueError if invalid
            num1 = float(num1_input)
            num2 = float(num2_input)

            # 2. Ask for an operation character string
            operator = input("Enter an operation (+, -, *, /): ").strip()

            # 5. Raise a custom InvalidOperationError for unsupported operators
            supported_operators = ['+', '-', '*', '/']
            if operator not in supported_operators:
                raise InvalidOperationError(f"'{operator}' is not a recognized operator.")

            # Perform calculations and 4. Handle division by zero scenario safely
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Explicit check or catching ZeroDivisionError naturally
                if num2 == 0:
                    raise ZeroDivisionError("Math Error: Cannot divide a number by zero.")
                result = num1 / num2

            # Display valid computed outcome state metrics
            print(f"[SUCCESS] Result: {num1} {operator} {num2} = {result}")

        # Catch-all exception handling blocks for errors
        except ValueError:
            print("[INPUT ERROR] Invalid numeric entry. Please enter numbers only (integers or decimals).")

        except ZeroDivisionError as zd_err:
            print(f"[MATH ERROR] {zd_err}")

        except InvalidOperationError as io_err:
            print(f"[OPERATOR ERROR] Unsupported operation. {io_err}")

        # 7. Add a finally block that reports completion of each calculation attempt
        finally:
            print("--- End of Calculation Attempt ---\n")


# --- Execution Control Activation ---
if __name__ == "__main__":
    run_safe_calculator()
