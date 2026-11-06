import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AdvancedStudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Student Profile & Preferences")
        self.root.geometry("550x700")
        self.root.minsize(500, 600)

        # Configure root grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight=1)

        # --- Control Variables ---
        self.name_var = tk.StringVar()
        self.dept_var = tk.StringVar()
        self.year_var = tk.StringVar(value="First Year")

        # Checkbuttons variables
        self.hobby_sports = tk.BooleanVar(value=False)
        self.hobby_arts = tk.BooleanVar(value=False)
        self.hobby_music = tk.BooleanVar(value=False)

        # Scale variable
        self.skill_level_var = tk.IntVar(value=5)

        # =========================================================================
        # LABELFRAME 1: Academic Profile
        # =========================================================================
        profile_frame = ttk.LabelFrame(self.root, text=" Academic Profile ", padding=12)
        profile_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=8)
        profile_frame.columnconfigure(1, weight=1)

        ttk.Label(profile_frame, text="Full Name: *").grid(row=0, column=0, sticky="w", pady=4)
        self.name_entry = ttk.Entry(profile_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=4)

        ttk.Label(profile_frame, text="Department:").grid(row=1, column=0, sticky="w", pady=4)
        self.dept_box = ttk.Combobox(profile_frame, textvariable=self.dept_var, state="readonly",
                                     values=["Computer Science", "Data Science", "Cyber Security",
                                             "Electrical Engineering"])
        self.dept_box.set("Computer Science")
        self.dept_box.grid(row=1, column=1, sticky="ew", padx=5, pady=4)

        ttk.Label(profile_frame, text="Academic Year:").grid(row=2, column=0, sticky="nw", pady=6)
        radio_container = tk.Frame(profile_frame)
        radio_container.grid(row=2, column=1, sticky="w", padx=5, pady=4)

        ttk.Radiobutton(radio_container, text="First Year", variable=self.year_var, value="First Year").pack(
            side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_container, text="Second Year", variable=self.year_var, value="Second Year").pack(
            side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_container, text="Third Year+", variable=self.year_var, value="Third Year+").pack(
            side=tk.LEFT, padx=5)

        # =========================================================================
        # LABELFRAME 2: Preferences & Skills Catalog
        # =========================================================================
        pref_frame = ttk.LabelFrame(self.root, text=" Student Preferences & Skills ", padding=12)
        pref_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=8)
        pref_frame.columnconfigure(1, weight=1)

        ttk.Label(pref_frame, text="Interests / Hobbies:").grid(row=0, column=0, sticky="w", pady=4)
        check_container = tk.Frame(pref_frame)
        check_container.grid(row=0, column=1, sticky="w", padx=5, pady=4)
        ttk.Checkbutton(check_container, text="Sports", variable=self.hobby_sports).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(check_container, text="Arts & Design", variable=self.hobby_arts).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(check_container, text="Music", variable=self.hobby_music).pack(side=tk.LEFT, padx=5)

        self.scale_label = tk.Label(pref_frame, text="Coding Familiarity: 5/10", font=("Arial", 9))
        self.scale_label.grid(row=1, column=0, sticky="w", pady=4)
        self.experience_scale = ttk.Scale(pref_frame, from_=1, to=10, orient=tk.HORIZONTAL,
                                          variable=self.skill_level_var, command=self.sync_scale_label)
        self.experience_scale.grid(row=1, column=1, sticky="ew", padx=5, pady=4)

        ttk.Label(pref_frame, text="Core Electives: *").grid(row=2, column=0, sticky="nw", pady=4)
        list_container = tk.Frame(pref_frame)
        list_container.grid(row=2, column=1, sticky="ew", padx=5, pady=4)
        list_container.columnconfigure(0, weight=1)

        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL)
        self.skills_listbox = tk.Listbox(list_container, selectmode=tk.MULTIPLE, height=4,
                                         yscrollcommand=scrollbar.set, exportselection=False)
        scrollbar.config(command=self.skills_listbox.yview)

        courses = ["Python Core", "Advanced Java", "Web Architectures", "Machine Learning", "Database Systems",
                   "Cloud Security"]
        for course in courses:
            self.skills_listbox.insert(tk.END, course)

        self.skills_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # =========================================================================
        # LABELFRAME 3: Data Ledger Dashboard & Output Summary
        # =========================================================================
        summary_frame = ttk.LabelFrame(self.root, text=" Validated Profile Summary Ledger ", padding=12)
        summary_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=8)
        summary_frame.columnconfigure(0, weight=1)
        summary_frame.rowconfigure(0, weight=1)
        summary_frame.rowconfigure(1, weight=0)

        self.summary_text = tk.Text(summary_frame, wrap=tk.WORD, height=6, bg="#fcfcfc", font=("Courier", 10))
        self.summary_text.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        self.summary_text.insert(tk.END, "Awaiting active data verification compilation input...")
        self.summary_text.config(state=tk.DISABLED)

        actions_container = tk.Frame(summary_frame)
        actions_container.grid(row=1, column=0, sticky="ew")
        actions_container.columnconfigure(0, weight=1)
        actions_container.columnconfigure(1, weight=1)
        actions_container.columnconfigure(2, weight=1)

        ttk.Button(actions_container, text="Save Profile", command=self.handle_save).grid(row=0, column=0, padx=5,
                                                                                          sticky="ew")
        ttk.Button(actions_container, text="Clear/Reset", command=self.handle_reset).grid(row=0, column=1, padx=5,
                                                                                          sticky="ew")
        ttk.Button(actions_container, text="Exit Application", command=self.root.quit).grid(row=0, column=2, padx=5,
                                                                                            sticky="ew")

    # --- Callback Handlers ---
    def sync_scale_label(self, val):
        self.scale_label.config(text=f"Coding Familiarity: {int(float(val))}/10")

    def handle_save(self):
        full_name = self.name_var.get().strip()
        if not full_name:
            messagebox.showerror("Validation Error", "The required field 'Full Name' cannot be left blank.")
            return

        selected_indices = self.skills_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Validation Error", "You must select at least one elective course.")
            return

        hobbies = []
        if self.hobby_sports.get(): hobbies.append("Sports")
        if self.hobby_arts.get(): hobbies.append("Arts & Design")
        if self.hobby_music.get(): hobbies.append("Music")
        hobbies_str = ", ".join(hobbies) if hobbies else "None Selected"

        selected_courses = [self.skills_listbox.get(i) for i in selected_indices]
        courses_str = ", ".join(selected_courses)

        report_profile = (
            f"====================================================\n"
            f"          STUDENT ADVANCED PROFILE RECORD           \n"
            f"====================================================\n"
            f"• Full Name          : {full_name}\n"
            f"• Major Department   : {self.dept_var.get()}\n"
            f"• Academic Timeline  : {self.year_var.get()}\n"
            f"• Declared Hobbies   : {hobbies_str}\n"
            f"• Coding Skill Tier  : {self.skill_level_var.get()}/10\n"
            f"• Selected Electives : {courses_str}\n"
            f"===================================================="
        )

        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete("1.0", tk.END)
        self.summary_text.insert(tk.END, report_profile)
        self.summary_text.config(state=tk.DISABLED)
        messagebox.showinfo("Success", "Records saved successfully.")

    def handle_reset(self):
        self.name_var.set("")
        self.dept_box.set("Computer Science")
        self.year_var.set("First Year")
        self.hobby_sports.set(False)
        self.hobby_arts.set(False)
        self.hobby_music.set(False)
        self.skill_level_var.set(5)
        self.scale_label.config(text="Coding Familiarity: 5/10")
        self.skills_listbox.selection_clear(0, tk.END)

        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete("1.0", tk.END)
        self.summary_text.insert(tk.END, "Awaiting active data verification compilation input...")
        self.summary_text.config(state=tk.DISABLED)


# =========================================================================
# CRITICAL APP INITIALIZATION BLOCK (DO NOT REMOVE)
# =========================================================================
if __name__ == "__main__":
    window = tk.Tk()
    app = AdvancedStudentGUI(window)
    window.mainloop()
