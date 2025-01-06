from tkinter import ttk

def apply_styles():
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12))
    style.configure("TCombobox", font=("Helvetica", 12))
    style.configure("TProgressbar", thickness=20)

# Add any other utility functions here if needed
