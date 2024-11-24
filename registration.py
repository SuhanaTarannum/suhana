import tkinter as tk
from tkinter import messagebox

# Function to handle registration logic
def register():
    username = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    address = entry_address.get()

    if username and email and password and confirm_password and address:
        if password == confirm_password:
            messagebox.showinfo("Registration", f"User {username} registered successfully!")
        else:
            messagebox.showerror("Password Error", "Passwords do not match!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Setting up the main window
root = tk.Tk()
root.title("Registration Form")

# Set window size
root.geometry("500x600")  # Width x Height in pixels

# Setting a common font for all labels and entry fields
font_large = ("Helvetica", 14)

# Creating and placing the labels and entry fields in the center
tk.Label(root, text="Name:", font=font_large).pack(pady=10)
entry_name = tk.Entry(root, width=25, font=font_large)
entry_name.pack(pady=5)

tk.Label(root, text="Email:", font=font_large).pack(pady=10)
entry_email = tk.Entry(root, width=25, font=font_large)
entry_email.pack(pady=5)

tk.Label(root, text="Password:", font=font_large).pack(pady=10)
entry_password = tk.Entry(root, show='*', width=25, font=font_large)
entry_password.pack(pady=5)

tk.Label(root, text="Confirm Password:", font=font_large).pack(pady=10)
entry_confirm_password = tk.Entry(root, show='*', width=25, font=font_large)
entry_confirm_password.pack(pady=5)

tk.Label(root, text="Address:", font=font_large).pack(pady=10)
entry_address = tk.Entry(root, width=25, font=font_large)
entry_address.pack(pady=5)

# Register button
register_button = tk.Button(root, text="Register", command=register, width=15, font=font_large)
register_button.pack(pady=20)

# Running the main loop
root.mainloop()
