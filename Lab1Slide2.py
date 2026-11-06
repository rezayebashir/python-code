# 1. Create a list of at least 10 student scores (including duplicates)
scores = [78, 55, 92, 45, 60, 85, 78, 60, 99, 67, 40, 88]

# 2. Calculate minimum, maximum and average
min_score = min(scores)
max_score = max(scores)
avg_score = sum(scores) / len(scores)

print("--- 1 & 2. Basic List Statistics ---")
print(f"All Scores: {scores}")
print(f"Minimum Score: {min_score}")
print(f"Maximum Score: {max_score}")
print(f"Average Score: {avg_score:.2f}\n")


# 3. Create a new list containing scores >= 60 using a list comprehension
passing_scores = [score for score in scores if score >= 60]
print("--- 3. List Comprehension (Scores >= 60) ---")
print(f"Passing Scores: {passing_scores}\n")


# 4. Convert the list to a set and explain the result
scores_set = set(scores)
print("--- 4. Set Conversion ---")
print(f"Scores Set: {scores_set}")
# Explanation: Sets in Python only store unique values. Converting a list containing
# duplicate values (like 78 and 60) automatically filters out those repeats, leaving
# only one instance of each unique score. It also removes the original insertion order.
print()


# 5. Create a dictionary mapping student IDs to names
student_directory = {
    "S01": "Alice",
    "S02": "Bob",
    "S03": "Charlie",
    "S04": "David",
    "S05": "Eva",
    "S06": "Frank",
    "S07": "Grace",
    "S08": "Henry",
    "S09": "Ivy",
    "S10": "Jack"
}


# 6. Search for one student by ID
search_id = "S04"
print("--- 6. Search Student by ID ---")
if search_id in student_directory:
    print(f"Found! Student ID {search_id} belongs to: {student_directory[search_id]}")
else:
    print(f"Student ID {search_id} not found.")
print()


# 7 & 8. Sort student records by score using zip() and enumerate()
# Since we have 10 names/IDs, let's take the first 10 scores to match exactly
student_ids = list(student_directory.keys())
student_names = list(student_directory.values())
subset_scores = scores[:10]

# Combine the collections using zip() into a structured record format
# Record format: (ID, Name, Score)
student_records = list(zip(student_ids, student_names, subset_scores))

# Sort the records by score in descending order (highest score first)
# x[2] corresponds to the score element in each record tuple
sorted_records = sorted(student_records, key=lambda x: x[2], reverse=True)

print("--- 7 & 8. Sorted Records using zip() and enumerate() ---")
print("Ranked Student Performance:")
# Use enumerate() to easily number and display the leaderboard
for rank, (s_id, name, score) in enumerate(sorted_records, start=1):
    print(f"Rank {rank}: [ID: {s_id}] {name} - Score: {score}")
