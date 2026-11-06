import base64
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox


class ImageProfileCard(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Practical Lab 3 - Image Profile Card")
        self.geometry("400x500")
        self.resizable(False, False)  # Fixed dimensions fit for a profile card layout
        self.config(bg="#F4F6F7")

        # Define consistent spacing padding configurations
        self.pad_options = {"padx": 15, "pady": 8}

        self._build_profile_card()

    def _build_profile_card(self):
        # ----------------------------------------------------
        # 1. CORE CARD CONTAINER (Using a Frame)
        # ----------------------------------------------------
        self.card_frame = tk.Frame(
            self,
            bg="white",
            bd=1,
            relief=tk.SOLID,
            highlightbackground="#BDC3C7",
            highlightthickness=1
        )
        self.card_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

        # ----------------------------------------------------
        # 2. IMAGE DISPLAY SECTION (PhotoImage + Reference Preservation)
        # ----------------------------------------------------
        # Generic small base64 encoded PNG user avatar placeholder icon string
        # to ensure instant compilation without missing external files.
        avatar_png_base64 = (
            "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkBAMAAACCzIocAAAAMFBMVEUAAADb29vV"
            "1dXW1tbY2Njh4eHj4+Po6Ojp6enq6urr6+vs7Ozt7e3u7u7v7+/w8PD////79Z0A"
            "AAAHRSTlMAEDM0O0RI6vN8AAAARElEQVRYw+3QwQkAMAgEMDHdf1un6AsE8Z4IAt"
            "fKVEvV0uOqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpXF8mBD7vS0P"
            "YpAAAAAElFTkSuQmCC"
        )

        try:
            # Creating the PNG image with PhotoImage
            self.profile_image = tk.PhotoImage(data=avatar_png_base64)

            # --- CRITICAL LAB REQUIREMENT: Keeping the image reference alive ---
            # Storing it explicitly as an instance attribute (self.profile_image) or
            # explicitly binding it to the label ensures Python's garbage collector
            # doesn't destroy the graphic memory layout behind the canvas scene.

            self.image_label = tk.Label(self.card_frame, image=self.profile_image, bg="white")
            self.image_label.image = self.profile_image  # Double layer reference safety
            self.image_label.pack(pady=(20, 10))

        except Exception as e:
            # Clean text fallback block if underlying display drivers fail
            self.image_label = tk.Label(self.card_frame, text="[ Profile Image Canvas ]", font=("Arial", 10, "italic"),
                                        bg="white")
            self.image_label.pack(pady=20)

        # ----------------------------------------------------
        # 3. PROFILE DATA TEXT FIELDS (Using Labels)
        # ----------------------------------------------------
        # Define specific, cleanly separated typography weights
        name_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        info_font = tkfont.Font(family="Arial", size=11, weight="normal")
        label_header_font = tkfont.Font(family="Arial", size=9, weight="bold")

        # Name Display Label
        self.lbl_name = tk.Label(self.card_frame, text="Alex Mercer", font=name_font, bg="white", fg="#2C3E50")
        self.lbl_name.pack(pady=(5, 15))

        # Department Display Sector
        self.lbl_dept_title = tk.Label(self.card_frame, text="DEPARTMENT", font=label_header_font, bg="white",
                                       fg="#7F8C8D")
        self.lbl_dept_title.pack(anchor="w", padx=30)
        self.lbl_dept = tk.Label(self.card_frame, text="Software Engineering", font=info_font, bg="white", fg="#34495E")
        self.lbl_dept.pack(anchor="w", padx=30, pady=(0, 12))

        # Email Display Sector
        self.lbl_email_title = tk.Label(self.card_frame, text="EMAIL ADDRESS", font=label_header_font, bg="white",
                                        fg="#7F8C8D")
        self.lbl_email_title.pack(anchor="w", padx=30)
        self.lbl_email = tk.Label(self.card_frame, text="alex.mercer@university.edu", font=info_font, bg="white",
                                  fg="#34495E")
        self.lbl_email.pack(anchor="w", padx=30, pady=(0, 20))

        # ----------------------------------------------------
        # 4. ACTION INTERFACE BUTTONS
        # ----------------------------------------------------
        self.button_container = tk.Frame(self.card_frame, bg="white")
        self.button_container.pack(fill=tk.X, side=tk.BOTTOM, pady=20, padx=20)

        # Configure container grid for uniform side-by-side splitting layout proportions
        self.button_container.columnconfigure(0, weight=1)
        self.button_container.columnconfigure(1, weight=1)

        # Edit Profile Button
        self.btn_edit = tk.Button(
            self.button_container,
            text="Edit Profile",
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            relief=tk.FLAT,
            padx=10,
            pady=6,
            command=self.edit_profile_action
        )
        self.btn_edit.grid(row=0, column=0, padx=5, sticky="ew")

        # Close App Button
        self.btn_close = tk.Button(
            self.button_container,
            text="Close",
            bg="#95A5A6",
            fg="white",
            activebackground="#7F8C8D",
            activeforeground="white",
            relief=tk.FLAT,
            padx=10,
            pady=6,
            command=self.destroy
        )
        self.btn_close.grid(row=0, column=1, padx=5, sticky="ew")

    def edit_profile_action(self):
        """Standard alert dialog triggered upon pressing the edit layout button."""
        messagebox.showinfo("Edit Action Requested", "Profile metadata edit pipeline interface would launch here.")


if __name__ == "__main__":
    app = ImageProfileCard()
    app.mainloop()
