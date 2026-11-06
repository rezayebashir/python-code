import os

# --- Define Custom Exception Type ---
class DocumentReadError(Exception):
    """Custom wrapper exception for grouping low-level file operation failures."""
    pass


def read_robust_file():
    print("==================================================")
    print("          Robust UTF-8 Text File Reader           ")
    print("==================================================\n")

    # 1. Ask the user for a target filename
    filename = input("Enter the filename to read (e.g., sample.txt): ").strip()
    print("-" * 50)

    try:
        # 2 & 6. Use a context manager to attempt reading the file as UTF-8 text
        with open(filename, mode="r", encoding="utf-8") as file:
            content = file.read()

    # 3. Handle standard missing path errors
    except FileNotFoundError as fnf_err:
        print(f"[SYSTEM CATCH] Low-level system raised: {type(fnf_err).__name__}")
        raise DocumentReadError(f"Failed to access '{filename}': File does not exist on disk.") from fnf_err

    # 3. Handle restriction or directory permission reading errors
    except PermissionError as perm_err:
        print(f"[SYSTEM CATCH] Low-level system raised: {type(perm_err).__name__}")
        raise DocumentReadError(f"Access Denied: You do not have permissions to read '{filename}'.") from perm_err

    # 4. Handle decoding errors if the target is binary or has non-UTF-8 characters
    except UnicodeDecodeError as decode_err:
        print(f"[SYSTEM CATCH] Low-level system raised: {type(decode_err).__name__}")
        raise DocumentReadError(f"Encoding Error: '{filename}' contains invalid data patterns for UTF-8 translation.") from decode_err

    # 5. Display file content only on complete success using the try-else structure
    else:
        print("[SUCCESS] Document parsed cleanly with no exceptions raised.")
        print("\n--- File Content Start ---")
        if content.strip():
            print(content)
        else:
            print("(The file is completely empty)")
        print("--- File Content End ---")


# --- Execution Demonstration Setup ---
if __name__ == "__main__":
    # Let's create a valid sample file to make testing easy out-of-the-box
    default_test_file = "sample.txt"
    with open(default_test_file, "w", encoding="utf-8") as f:
        f.write("Hello World!\nThis is a robust UTF-8 text file parsing verification.")

    print(f"[DEMO SETUP] Generated a valid test file named '{default_test_file}'.\n")

    try:
        read_robust_file()
    except DocumentReadError as custom_err:
        # Catching the translated custom exception layer at user execution boundary
        print(f"\n[CUSTOM ERROR CAUGHT] {custom_err}")
