import tkinter as tk
from tkinter import messagebox

def calculate_forward():
    try:
        years = float(years_entry.get())

        if years < 0:
            raise ValueError

        days = round(years * 365.25, 2)

        result = (
            f"Total Years: {years}\n"
            f"Total Months: {round(days / 30.44, 2)}\n"
            f"Total Weeks: {round(days / 7, 2)}\n"
            f"Total Days: {days}"
        )

        messagebox.showinfo("Results", result)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number (example: 1.5)")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Years To Days Converter")
root.geometry("300x180")
root.resizable(False, False)

tk.Label(root, text="Enter Total Years", font=("Cascadia Code", 10)).pack(pady=10)
years_entry = tk.Entry(root, width=25, font=("Cascadia Code", 9))
years_entry.pack(pady=5)

tk.Button(root, text="Convert", width=15, command=calculate_forward).pack(pady=15)

root.mainloop()
