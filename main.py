from typing import Dict, Set, List, Tuple, Any, TypeVar, Iterable

# Defining a generic TypeVar for reusable helper design
T = TypeVar('T')


# --- GENERIC HELPER STRUCTURE/FUNCTION ---
def format_collection(collection: Iterable[T]) -> str:
    """Generic helper function using TypeVar to safely transform any primitive

    iterable collection into an ordered, comma-separated string for clean display.
    """
    if not collection:
        return "None"
    return ", ".join(sorted(str(item) for item in collection))


# --- SYSTEM MANAGEMENT CLASS ---
class CourseRegistrationManager:
    def __init__(self) -> None:
        # Core collection structure: Dictionary indexed by Student ID string mapping
        # to a student details dict containing a Set of registered course strings.
        self.students_db: Dict[str, Dict[str, Any]] = {}

    def add_student(self, student_id: str, name: str) -> bool:
        """Adds a new student profile to the primary registry dictionary."""
        if student_id in self.students_db:
            print(f"[ERROR] Student ID '{student_id}' already exists in system.")
            return False

        self.students_db[student_id] = {
            "name": name,
            "courses": set()  # Set initialized for natural course unique containment
        }
        print(f"[SUCCESS] Registered new student: {name} (ID: {student_id})")
        return True

    def register_course(self, student_id: str, course_code: str) -> None:
        """Adds a course code to the targeted student's course set."""
        if student_id not in self.students_db:
            print(f"[ERROR] Registration failed. Student ID '{student_id}' not found.")
            return

        # Appending to a set natively prevents duplicate course tracking
        self.students_db[student_id]["courses"].add(course_code.upper())
        print(f"[REGISTERED] Enrolled student '{self.students_db[student_id]['name']}' into {course_code.upper()}.")

    def drop_course(self, student_id: str, course_code: str) -> None:
        """Safely drops a course from a student's profile if enrolled."""
        if student_id not in self.students_db:
            print(f"[ERROR] Operation failed. Student ID '{student_id}' not found.")
            return

        course_set: Set[str] = self.students_db[student_id]["courses"]
        normalized_code = course_code.upper()

        if normalized_code in course_set:
            course_set.discard(normalized_code)
            print(f"[DROPPED] Removed {normalized_code} from student '{self.students_db[student_id]['name']}'.")
        else:
            print(f"[INFO] Student is not registered in '{normalized_code}'.")

    def search_student(self, student_id: str) -> None:
        """Finds and lists descriptive profile statistics for a selected student ID."""
        print(f"--- Searching Database for ID: {student_id} ---")
        if student_id in self.students_db:
            record = self.students_db[student_id]
            formatted_courses = format_collection(record["courses"])
            print(f"Name: {record['name']}\nEnrolled Courses: {formatted_courses}")
        else:
            print("[NOT FOUND] No record exists with that identifier.")

    def get_all_unique_courses(self) -> Set[str]:
        """Gathers every course currently active across all students using a set comprehension."""
        return {course for profile in self.students_db.values() for course in profile["courses"]}

    def find_students_sharing_course(self, course_code: str) -> List[Tuple[str, str]]:
        """Locates all unique student names/IDs holding a specific target course code."""
        normalized_code = course_code.upper()
        # List comprehension processing relational lookup matching parameters efficiently
        return [(s_id, info["name"]) for s_id, info in self.students_db.items() if normalized_code in info["courses"]]

    def display_sorted_students(self) -> None:
        """Displays entire system roster alphabetized by student name keys."""
        print("\n--- Sorted Master Student Directory ---")
        if not self.students_db:
            print("System directory is currently empty.")
            return

        # Sort the dictionary items according to the nested 'name' value string
        sorted_profiles = sorted(self.students_db.items(), key=lambda items: items[1]["name"])

        for s_id, info in sorted_profiles:
            courses_str = format_collection(info["courses"])
            print(f"• [ID: {s_id}] {info['name']} — Enrolled in: [{courses_str}]")


# --- SYSTEM DEMONSTRATION RUN ---
if __name__ == "__main__":
    manager = CourseRegistrationManager()

    print("--- 1. Testing Core Profile Initialization ---")
    manager.add_student("S101", "Charlie Baker")
    manager.add_student("S102", "Alice Smith")
    manager.add_student("S103", "Bob Miller")

    print("\n--- 2. Testing Course Registrations ---")
    manager.register_course("S101", "CS101")
    manager.register_course("S101", "MATH201")
    manager.register_course("S102", "CS101")  # Shared course
    manager.register_course("S102", "ENG102")
    manager.register_course("S103", "MATH201")  # Shared course
    # Natural duplicate test:
    manager.register_course("S101", "CS101")

    print("\n--- 3. Testing Complete Unique Catalog Compilation ---")
    unique_catalog = manager.get_all_unique_courses()
    print(f"Global Dynamic Course Catalog: {format_collection(unique_catalog)}")

    print("\n--- 4. Testing Course Overlap Filter (Sharing a Course) ---")
    target_course = "CS101"
    matches = manager.find_students_sharing_course(target_course)
    print(f"Students registered in {target_course}:")
    for s_id, name in matches:
        print(f"  - {name} ({s_id})")

    print("\n--- 5. Testing Deletion Operations (Drop Course) ---")
    manager.drop_course("S101", "MATH201")

    print("\n--- 6. Testing Lookup Engine ---")
    manager.search_student("S101")

    print("\n--- 7. Testing Final System Directory State Output ---")
    manager.display_sorted_students()
