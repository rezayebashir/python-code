import json
import shutil
from pathlib import Path
from typing import Dict, Any, Optional

# --- Configuration Constants ---
DB_PATH = Path("students_db.json")
BACKUP_DIR = Path("backups")


# --- CORE IMPLEMENTATION FUNCTIONS ---

def load_database() -> Dict[str, Dict[str, Any]]:
    """Loads student records from the JSON file.

    Handles missing or corrupted files with robust fallbacks.
    """
    if not DB_PATH.exists():
        return {}

    try:
        with DB_PATH.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("[WARNING] Database file corrupted! Initializing a fresh instance.")
        return {}


def save_database(data: Dict[str, Dict[str, Any]]):
    """Saves the runtime database dictionary back to the persistent JSON file."""
    with DB_PATH.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def create_backup():
    """Creates a safety backup of the database before destructive operations."""
    if not DB_PATH.exists():
        return

    # Ensure backup directory path context exists
    BACKUP_DIR.mkdir(exist_ok=True)

    backup_file_path = BACKUP_DIR / f"{DB_PATH.stem}_backup{DB_PATH.suffix}"
    # Use shutil with pathlib objects to execute copy
    shutil.copy(DB_PATH, backup_file_path)
    print(f"[BACKUP] Safety copy created successfully at: {backup_file_path}")


def validate_fields(student_id: str, name: str, department: str, semester: str) -> bool:
    """Validates student record data types and content values formatting."""
    # Ensure none of the fields are blank or purely whitespace strings
    if not all(field.strip() for field in [student_id, name, department, semester]):
        print("[VALIDATION ERROR] All fields are mandatory and cannot be left empty.")
        return False

    # Check that Student ID follows a logical format (e.g., must start with an 'S' followed by digits)
    if not (student_id.startswith("S") and student_id[1:].isdigit()):
        print(f"[VALIDATION ERROR] Student ID '{student_id}' is invalid. Must match format 'S<number>' (e.g., S101).")
        return False

    # Check semester formatting bounds
    if not (semester.isdigit() and 1 <= int(semester) <= 8):
        print(f"[VALIDATION ERROR] Semester value must be a valid integer number between 1 and 8.")
        return False

    return True


# --- SYSTEM OPERATIONS ---

def add_student(student_id: str, name: str, department: str, semester: str) -> bool:
    """Adds a new valid student to the persistent file system registry."""
    if not validate_fields(student_id, name, department, semester):
        return False

    db = load_database()
    if student_id in db:
        print(f"[ERROR] Record skipped. Student ID '{student_id}' already exists.")
        return False

    db[student_id] = {
        "name": name.strip(),
        "department": department.strip(),
        "semester": int(semester)
    }
    save_database(db)
    print(f"[SUCCESS] Student profile saved: {name} ({student_id})")
    return True


def list_students():
    """Retrieves and lists all database records in a cleanly formatted table row setup."""
    db = load_database()
    print("\n======================= ACTIVE STUDENT REGISTRY =======================")
    if not db:
        print("   No records exist in the database yet.")
        print("=======================================================================")
        return

    print(f"{'ID':<8} | {'Student Name':<20} | {'Department':<20} | {'Semester':<8}")
    print("-" * 71)
    for s_id, info in db.items():
        print(f"{s_id:<8} | {info['name']:<20} | {info['department']:<20} | {info['semester']:<8}")
    print("=======================================================================\n")


def search_student(student_id: str) -> Optional[Dict[str, Any]]:
    """Searches the database profile registry for a specific student ID."""
    db = load_database()
    print(f"--- Querying system for Student ID: {student_id} ---")
    if student_id in db:
        info = db[student_id]
        print(
            f"• Profile Match Found!\n  - Name: {info['name']}\n  - Dept: {info['department']}\n  - Term: Semester {info['semester']}\n")
        return info
    print("[NOT FOUND] No corresponding record matches that identifier.\n")
    return None


def update_student(student_id: str, new_name: str, new_department: str, new_semester: str) -> bool:
    """Modifies student profile metrics after performing safety validation and automated backups."""
    if not validate_fields(student_id, new_name, new_department, new_semester):
        return False

    db = load_database()
    if student_id not in db:
        print(f"[ERROR] Update aborted. Student ID '{student_id}' does not exist.")
        return False

    # Trigger requirement: Create backup before destructive modification operations
    create_backup()

    db[student_id] = {
        "name": new_name.strip(),
        "department": new_department.strip(),
        "semester": int(new_semester)
    }
    save_database(db)
    print(f"[UPDATED] Record {student_id} modified successfully in persistent memory.")
    return True


def delete_student(student_id: str) -> bool:
    """Permanently deletes a student profile after committing a recovery backup instance."""
    db = load_database()
    if student_id not in db:
        print(f"[ERROR] Deletion aborted. Student ID '{student_id}' does not exist.")
        return False

    # Trigger requirement: Create backup before structural file deletion tasks
    create_backup()

    del db[student_id]
    save_database(db)
    print(f"[DELETED] Student record '{student_id}' completely dropped from active records.")
    return True


# --- EXECUTION DEMONSTRATION WINDOW ---
if __name__ == "__main__":
    # Clean workspace file paths from previous runs for validation transparency
    if DB_PATH.exists():
        DB_PATH.unlink()

    print("--- 1. Testing Add Operation & Input Field Validations ---")
    add_student("S101", "Alice Vance", "Software Engineering", "3")
    add_student("S102", "Bob Miller", "Data Science", "5")

    # Test invalid values data layout formatting checks
    add_student("INVALID_ID", "Charlie", "Physics", "1")
    add_student("S103", "Charlie", "Physics", "99")  # Invalid semester

    print("\n--- 2. Testing Listing Directory Output ---")
    list_students()

    print("--- 3. Testing Lookup Query Operations ---")
    search_student("S101")
    search_student("S999")  # Missing query test

    print("--- 4. Testing Destructive Update Operations (With Backup Checks) ---")
    update_student("S101", "Alice Vance-Smith", "Artificial Intelligence", "4")

    print("\n--- 5. Testing Destructive Deletion Operations (With Backup Checks) ---")
    delete_student("S102")

    print("\n--- 6. Final State Registry Summary ---")
    list_students()
