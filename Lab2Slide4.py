# ==========================================
# 1. CUSTOM EXCEPTION TYPE DEFINITION
# ==========================================
class InvalidGradeError(Exception):
    """Raised when a numeric grade value falls outside the acceptable range of 0 to 100."""
    pass


# ==========================================
# 2. SEPARATED VALIDATION LOGIC LAYER
# ==========================================
def validate_grade(value: any) -> float:
    """Safely converts input into a numeric float representation and validates

    that the score falls strictly within the acceptable 0 to 100 range boundaries.

    Raises:
        ValueError: If input cannot be converted to a numeric representation.
        InvalidGradeError: If numeric input is out of bounds (< 0 or > 100).
    """
    # Attempt to convert input to numeric form safely
    try:
        numeric_grade = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Input conversion failed. '{value}' is not a valid numeric pattern.")

    # Accept only grades from 0 to 100 bounds
    if numeric_grade < 0 or numeric_grade > 100:
        raise InvalidGradeError(f"Out-of-bounds error. Grade {numeric_grade} must be between 0 and 100.")

    return numeric_grade


# ==========================================
# 3. SEPARATED USER-INTERFACE (UI) LAYER
# ==========================================
def process_and_display_grade(test_input: any):
    """Acts as the UI presenter layer, routing test inputs into the validation

    engine and mapping resulting exception contexts to user-friendly messages.
    """
    print(f"Testing Input: {repr(test_input)}")
    try:
        # Route logic parameters out of UI execution boundary
        valid_score = validate_grade(test_input)
        print(f"  [SUCCESS] Valid Grade Approved: {valid_score:.1f}")

    except ValueError as ve:
        print(f"  [INPUT ERROR] {ve} — Please type numbers only (e.g., 85.5).")

    except InvalidGradeError as ige:
        print(f"  [RANGE ERROR] {ige} — Double-check entries for typo errors.")
    print("-" * 65)


# ==========================================
# 4. EXECUTION DEMONSTRATION & TESTING RUN
# ==========================================
if __name__ == "__main__":
    print("=========================================================")
    print("        RUNNING STUDENT GRADE VALIDATION ENGINE          ")
    print("=========================================================\n")

    # Comprehensive test matrices requested by assignment guidelines
    test_cases = [
        "85",  # 1. Valid integer string
        92.5,  # 2. Valid float numeric
        "abc",  # 3. Non-numeric text string input
        "  ",  # 4. Whitespace non-numeric test
        "-15.5",  # 5. Negative numeric score out of bounds
        "105",  # 6. Greater than 100 score out of bounds
        0,  # 7. Boundary edge case minimum (Valid)
        100  # 8. Boundary edge case maximum (Valid)
    ]

    for case in test_cases:
        process_and_display_grade(case)
