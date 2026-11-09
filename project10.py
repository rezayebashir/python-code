import tkinter as tk
from tkinter import messagebox


# Function to calculate tuition fees based on the grade
def calculate_fees(grade):
    grade = grade.strip().lower()
    if grade in ['1', '2', '3']:
        return 500
    elif grade in ['4', '5', '6']:
        return 700
    elif grade in ['7', '8', '9']:
        return 1000
    elif grade in ['10', '11', '12']:
        return 1300
    else:
        return 800  # Default fee for general entries


# Function to handle the submit action
def submit_enrollment():
    s_name = entry_name.get()
    f_name = entry_father.get()
    s_age = entry_age.get()
    s_grade = entry_grade.get()

    # Validation checks
    if not s_name or not f_name or not s_age or not s_grade:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        age_int = int(s_age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a valid number!")
        return

    # Calculate fee
    fee = calculate_fees(s_grade)

    # Display results on the text display area
    text_display.config(state=tk.NORMAL)  # Unlock text box to edit
    text_display.delete('1.0', tk.END)  # Clear old text

    receipt = (
        f"========================================\n"
        f"        ENROLLMENT RECEIPT             \n"
        f"========================================\n"
        f" Student Name : {s_name}\n"
        f" Father Name  : {f_name}\n"
        f" Age          : {age_int} years old\n"
        f" Grade        : Grade {s_grade}\n"
        f"----------------------------------------\n"
        f" Total Fee to Pay: ${fee}\n"
        f"========================================\n"
        f" Status       : Registration Successful"
    )

    text_display.insert(tk.END, receipt)
    text_display.config(state=tk.DISABLED)  # Lock text box back
    messagebox.showinfo("Success", "Student Enrolled Successfully!")


# Main Window Setup
root = tk.Tk()
root.title("School Enrollment System")
root.geometry("450x550")
root.resizable(False, False)

# Form Title
lbl_title = tk.Label(root, text="Student Enrollment Form", font=("Arial", 16, "bold"))
lbl_title.pack(pady=15)

# Form Fields Frame
frame_fields = tk.Frame(root)
frame_fields.pack(pady=10)

# Student Name
tk.Label(frame_fields, text="Student Full Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(frame_fields, width=30)
entry_name.grid(row=0, column=1, pady=5, padx=10)

# Father Name
tk.Label(frame_fields, text="Father's Name:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_father = tk.Entry(frame_fields, width=30)
entry_father.grid(row=1, column=1, pady=5, padx=10)

# Age
tk.Label(frame_fields, text="Age:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
entry_age = tk.Entry(frame_fields, width=30)
entry_age.grid(row=2, column=1, pady=5, padx=10)

# Grade
tk.Label(frame_fields, text="Grade (1 to 12):", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
entry_grade = tk.Entry(frame_fields, width=30)
entry_grade.grid(row=3, column=1, pady=5, padx=10)

# Submit Button
btn_submit = tk.Button(root, text="Enroll Student", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=20,
                       command=submit_enrollment)
btn_submit.pack(pady=15)

# Output Display Box
text_display = tk.Text(root, width=50, height=12, font=("Courier", 10), state=tk.DISABLED)
text_display.pack(pady=10, padx=20)

# Start Application Loop
root.mainloop()
