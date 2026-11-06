import os

FILE_NAME = "students.txt"


# Helper to ensure file exists and is cleanly reset for the lab demonstration
def initialize_file():
    print("--- 1 & 2. Creating file and writing initial 5 records ---")
    initial_records = [
        "S101,Alice Smith,Computer Science\n",
        "S102,Bob Jones,Mathematics\n",
        "S103,Charlie Brown,Physics\n",
        "S104,David Miller,Chemistry\n",
        "S105,Eva Green,Biology\n"
    ]
    # Context manager used to write initial data
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.writelines(initial_records)
    print(f"'{FILE_NAME}' created successfully with 5 student records.\n")


# 3. Read and display all records
def read_and_display_records():
    print("--- 3. Reading and Displaying All Records ---")
    try:
        # Context manager used to read data
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print("The file is empty.")
            else:
                print(content.strip())
    except FileNotFoundError:
        print(f"[ERROR] Cannot read file. '{FILE_NAME}' does not exist.")
    print()


# 4. Search for a student by ID
def search_student_by_id(student_id: str):
    print(f"--- 4. Searching for Student ID: {student_id} ---")
    try:
        found = False
        # Context manager used to safely read lines one by one
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                # Split CSV style string row data fields
                fields = line.strip().split(",")
                if fields and fields[0] == student_id:
                    print(f"Match Found! -> ID: {fields[0]} | Name: {fields[1]} | Major: {fields[2]}")
                    found = True
                    break
        if not found:
            print(f"No student record matches ID: {student_id}")
    except FileNotFoundError:
        print(f"[ERROR] Cannot search file. '{FILE_NAME}' does not exist.")
    print()


# 5. Append a new student
def append_student_record(student_id: str, name: str, major: str):
    print(f"--- 5. Appending New Student: {name} ---")
    new_record = f"{student_id},{name},{major}\n"
    try:
        # Context manager with 'a' flag ensures data appends to the end of file
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(new_record)
        print("Record appended successfully.")
    except FileNotFoundError:
        print(f"[ERROR] Cannot append data. '{FILE_NAME}' does not exist.")
    print()


# 6. Count total records
def count_total_records() -> int:
    print("--- 6. Counting Total Records ---")
    count = 0
    try:
        # Context manager used to loop lines and increment counter
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():  # Only count lines containing actual content
                    count += 1
        print(f"Total Student Records Found: {count}")
    except FileNotFoundError:
        print(f"[ERROR] Cannot count records. '{FILE_NAME}' does not exist.")
    print()
    return count


# --- Demonstration Run Execution ---
if __name__ == "__main__":
    # Setup initial test state
    initialize_file()

    # Test reading state
    read_and_display_records()

    # Test searching existing record
    search_student_by_id("S103")

    # Test appending a brand new entry
    append_student_record("S106", "Frank Wright", "Engineering")

    # Test reading file again to verify changes took effect
    read_and_display_records()

    # Test counting records
    count_total_records()

    # 7. Explicitly testing file non-existence catch state handling
    print("--- 7. Testing Missing File Error Handling ---")
    # Temporarily remove file to trigger exception state manually
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    # Attempting to scan a non-existent file path string target
    search_student_by_id("S101")
