import tkinter as tk
import dashboard
import register

def login():
    # Placeholder function for login functionality
    print("Login button clicked")
    window.destroy()  # Close the login page window
    dashboard.show_dashboard()  # Open the dashboard window

def create_account():
    # Placeholder function for create account functionality
    print("Create account button clicked")
    window.destroy()  # Close the login page window
    register.show_register()  # Open the dashboard window

def show_login_page():
    # Create the login page window
    global window  # Make window a global variable to access it in other functions
    window = tk.Tk()
    window.title("Login Page")

    # Create and position the widgets
    label_email = tk.Label(window, text="Email:")
    label_email.grid(row=0, column=0, padx=10, pady=5)

    entry_email = tk.Entry(window)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    label_password = tk.Label(window, text="Password:")
    label_password.grid(row=1, column=0, padx=10, pady=5)

    entry_password = tk.Entry(window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    button_login = tk.Button(window, text="Login", command=login)
    button_login.grid(row=2, column=0, padx=10, pady=5)

    button_register_account = tk.Button(window, text="Register Account", command=create_account)
    button_register_account.grid(row=2, column=1, padx=10, pady=5)

    # Run the login page window
    window.mainloop()
