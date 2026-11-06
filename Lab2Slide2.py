from typing import Dict, Set, Any

# --- Core Data Model Configuration ---
# Dictionary keyed by student ID string mapping to a dictionary containing student details.
# Structure: { student_id: {"name": str, "courses": Set[str]} }
registration_system: Dict[str, Dict[str, Any]] = {
    "S01": {"name": "Alice Smith", "courses": {"CS101", "MATH201", "ENG102"}},
    "S02": {"name": "Bob Jones", "courses": {"CS101", "PHYS101"}},
    "S03": {"name": "Charlie Brown", "courses": {"MATH201", "ENG102", "HIST101"}}
}


# --- Operation Helper Functions ---
def add_course(student_id: str, course_code: str):
    """Adds a course code to a student's set. Prevents duplicates automatically."""
    if student_id in registration_system:
        # Sets naturally ignore duplicate additions without needing explicit if-statements
        registration_system[student_id]["courses"].add(course_code)
        print(f"[ADD] Added {course_code} to {registration_system[student_id]['name']}'s schedule.")
    else:
        print(f"Error: Student ID {student_id} not found.")


def drop_course(student_id: str, course_code: str):
    """Removes a course code from a student's set safely if it exists."""
    if student_id in registration_system:
        # .discard() safely removes an item if present; avoids errors if it's already missing
        student_set: Set[str] = registration_system[student_id]["courses"]
        if course_code in student_set:
            student_set.discard(course_code)
            print(f"[DROP] Dropped {course_code} from {registration_system[student_id]['name']}'s schedule.")
        else:
            print(f"[DROP] {registration_system[student_id]['name']} is not registered for {course_code}.")
    else:
        print(f"Error: Student ID {student_id} not found.")


def find_common_courses(student_id_1: str, student_id_2: str) -> Set[str]:
    """Finds common courses between two students using set intersection (&)."""
    if student_id_1 in registration_system and student_id_2 in registration_system:
        set1: Set[str] = registration_system[student_id_1]["courses"]
        set2: Set[str] = registration_system[student_id_2]["courses"]
        return set1.intersection(set2)  # Alternative syntax: set1 & set2
    return set()


def get_all_unique_courses() -> Set[str]:
    """Compiles a complete list of unique courses in the system using set union (|)."""
    all_courses: Set[str] = set()
    for student_record in registration_system.values():
        all_courses = all_courses.union(student_record["courses"])  # Alternative syntax: all_courses |= student_record["courses"]
    return all_courses


# --- Execution Demonstration ---
if __name__ == "__main__":
    print("--- 1. Testing Add and Natural Duplicate Prevention ---")
    # Add a brand new course
    add_course("S01", "DATA301")
    # Attempting to add a course Alice already has
    add_course("S01", "CS101")
    print(f"Alice's updated course list: {registration_system['S01']['courses']}\n")

    print("--- 2. Testing Drop Operations ---")
    drop_course("S02", "PHYS101")
    print(f"Bob's updated course list: {registration_system['S02']['courses']}\n")

    print("--- 3. Set Intersection: Common Courses ---")
    common: Set[str] = find_common_courses("S01", "S02")
    name1, name2 = registration_system["S01"]["name"], registration_system["S02"]["name"]
    print(f"Common courses between {name1} and {name2}: {common if common else 'None'}\n")

    print("--- 4. Set Union: Overall System Catalog ---")
    total_catalog: Set[str] = get_all_unique_courses()
    print(f"All unique courses across the entire system: {total_catalog}")
