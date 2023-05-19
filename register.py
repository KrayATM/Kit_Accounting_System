import tkinter as tk
from tkinter import filedialog
import login

def register_user():
    # Placeholder function for create account functionality
    print("Register User button clicked")
    window.destroy()  # Close the Register page
    login.show_login_page()  # Open the login page

def close_register_page():
    window.destroy()  # Close the Register page
    login.show_login_page()  # Open the login page

def select_image():
    filetypes = (("Image files", "*.png *.jpg *.jpeg *.gif"), ("All files", "*.*"))
    filepath = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)
    if filepath:
        # Do something with the selected image file path
        print("Selected image:", filepath)

def show_register():
    # Create the Register window
    global window  # Make window a global variable to access it in other functions
    window = tk.Tk()
    window.title("Register")

    # Create and position the widgets
    label_email = tk.Label(window, text="Email:")
    label_email.grid(row=0, column=0, padx=10, pady=5)

    entry_email = tk.Entry(window)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    label_phone_number = tk.Label(window, text="Phone Number:")
    label_phone_number.grid(row=1, column=0, padx=10, pady=5)

    entry_phone_number = tk.Entry(window)
    entry_phone_number.grid(row=1, column=1, padx=10, pady=5)

    label_postal_address = tk.Label(window, text="Postal Address:")
    label_postal_address.grid(row=2, column=0, padx=10, pady=5)

    entry_postal_address = tk.Entry(window)
    entry_postal_address.grid(row=2, column=1, padx=10, pady=5)

    label_physical_address = tk.Label(window, text="Physical Address:")
    label_physical_address.grid(row=3, column=0, padx=10, pady=5)

    entry_physical_address = tk.Entry(window)
    entry_physical_address.grid(row=3, column=1, padx=10, pady=5)

    label_password = tk.Label(window, text="Password:")
    label_password.grid(row=4, column=0, padx=10, pady=5)

    entry_password = tk.Entry(window, show="*")
    entry_password.grid(row=4, column=1, padx=10, pady=5)

    label_confirm_password = tk.Label(window, text="Confirm Password:")
    label_confirm_password.grid(row=5, column=0, padx=10, pady=5)

    entry_confirm_password = tk.Entry(window, show="*")
    entry_confirm_password.grid(row=5, column=1, padx=10, pady=5)

    button_select_image = tk.Button(window, text="Select Image", command=select_image)
    button_select_image.grid(row=6, column=0, padx=10, pady=5)

    button_register = tk.Button(window, text="Register", command=register_user)
    button_register.grid(row=7, column=0, padx=10, pady=5)

    button_cancel = tk.Button(window, text="Cancel", command=close_register_page)
    button_cancel.grid(row=7, column=1, padx=10, pady=5, columnspan=2)

    # Run the Register window
    window.mainloop()