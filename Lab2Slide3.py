import csv

INPUT_FILE = "gradebook.csv"
OUTPUT_FILE = "results.csv"


def create_initial_gradebook():
    """Creates the initial CSV gradebook file, testing names with spaces and punctuation."""
    # Column Headers
    headers = ["student_id", "name", "midterm", "final"]

    # Test dataset with complex names (commas, quotation marks, hyphens, and spaces)
    data = [
        {"student_id": "S01", "name": "John Doe", "midterm": "85", "final": "90"},
        {"student_id": "S02", "name": "Smith, Jane", "midterm": "78", "final": "82"},  # Name contains a comma
        {"student_id": "S03", "name": "O'Connor, Tim", "midterm": "60", "final": "65"},
        # Name contains apostrophe & comma
        {"student_id": "S04", "name": "Alice \"Joy\" Miller", "midterm": "92", "final": "95"},  # Name contains quotes
        {"student_id": "S05", "name": "Bob-Sampson, Ray", "midterm": "45", "final": "50"}
    ]

    with open(INPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"[INIT] '{INPUT_FILE}' generated successfully with complex text records.")


def process_gradebook(passing_threshold: float):
    """Reads input using csv.DictReader, processes grades, filters passing students,

    and writes the calculated data to a new results.csv file.
    """
    processed_records = []
    passing_students = []

    print(f"\n--- Reading Records using csv.DictReader & Filtering (Threshold: {passing_threshold}) ---")

    with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Ensure target column configurations exist dynamically
        output_headers = reader.fieldnames + ["total", "average"] if reader.fieldnames else []

        for row in reader:
            # Extract names and cast score strings to numeric values
            name = row["name"]
            midterm = float(row["midterm"])
            final = float(row["final"])

            # Calculate metrics
            total = midterm + final
            average = total / 2

            # Update row values to keep dictionary matching layout structure
            row["total"] = f"{total:.1f}"
            row["average"] = f"{average:.1f}"
            processed_records.append(row)

            # Display checks matching passing threshold parameters
            if average >= passing_threshold:
                passing_students.append(name)
                print(f"• [PASS] {name:<22} | Avg: {average:.1f}")
            else:
                print(f"• [FAIL] {name:<22} | Avg: {average:.1f}")

    # Write performance metric updates into a secondary results file container
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=output_headers)
        writer.writeheader()
        writer.writerows(processed_records)

    print(f"\n[SUCCESS] Compiled calculations saved directly to '{OUTPUT_FILE}'.")


# --- Execution Control Window ---
if __name__ == "__main__":
    create_initial_gradebook()
    # Process grade computations filtering out metrics below an average score threshold of 70.0
    process_gradebook(passing_threshold=70.0)
