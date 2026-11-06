# ==========================================
# 1. CORE LOGIC / CUSTOM EXCEPTIONS
# ==========================================

class InvalidGradeError(Exception):
    """Custom exception raised when a grade is outside the 0-100 range."""
    pass


def validate_grade(value):
    """
    Validates a grade input.
    - Safely converts input to numeric form (float).
    - Accepts only grades from 0 to 100.
    """
    # Convert input to numeric form safely
    try:
        numeric_grade = float(value)
    except (ValueError, TypeError):
        raise ValueError("The grade must be a valid number.")

    # Accept only grades from 0 to 100
    if numeric_grade < 0 or numeric_grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100.")

    return numeric_grade


# ==========================================
# 2. USER INTERFACE (UI) LOGIC & TESTING
# ==========================================

def run_test_case(test_value, description):
    """Helper function to run test cases and display user-friendly messages."""
    print(f"Testing: {description} (Input: '{test_value}')")
    try:
        validated_grade = validate_grade(test_value)
        print(f"  Success: Grade '{validated_grade}' is valid!")
    except ValueError as e:
        print(f"  Error: {e}")
    except InvalidGradeError as e:
        print(f"  Error: {e}")
    print("-" * 50)


def test_grade_validator():
    """Tests valid, non-numeric, negative, and >100 values."""
    print("--- Running Automated Tests ---\n")

    # Test valid value
    run_test_case("85.5", "Valid grade")
    run_test_case(90, "Valid grade as integer")

    # Test non-numeric value
    run_test_case("abc", "Non-numeric grade")
    run_test_case("", "Empty input")

    # Test negative value
    run_test_case("-15", "Negative grade")

    # Test >100 value
    run_test_case("105", "Grade greater than 100")


def interactive_menu():
    """Allows manual user entry with a friendly UI loop."""
    print("\n--- Student Grade Validator Console ---")
    while True:
        user_input = input("Enter a student grade to validate (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting validator. Goodbye!")
            break

        try:
            grade = validate_grade(user_input)
            print(f" Success: Grade {grade} is valid and recorded.")
        except (ValueError, InvalidGradeError) as error:
            print(f" Validation Failed: {error}")
        print()


if __name__ == "__main__":
    # First run the required test suite cases
    test_grade_validator()

    # Start the interactive UI
    interactive_menu()
