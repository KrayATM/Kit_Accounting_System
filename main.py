import tkinter as tk
from PIL import ImageTk, Image  # Requires the Pillow library
import login

# Create the main window
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tkinter Window")

        # Load and resize the image for the window icon
        icon_image = Image.open("..\Kit_Accounting_System\images\kit-accounting-logo-removebg-preview.png")  # Replace with your icon image path
        icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)  # Adjust the size as needed
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.iconphoto(True, icon_photo)  # Set the window icon

window = MainWindow()

# Set window title
window.title("Kit Accounting System")

# Calculate the center position of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500  # Adjust as needed
window_height = 300  # Adjust as needed
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Call the show_login_page function to display the login page
def open_login_page():
    window.destroy()  # Close the current window
    login.show_login_page()  # Open the login page

# Load and resize the image
image = Image.open("..\Kit_Accounting_System\images\kit-accounting-logo-removebg-preview.png")
image = image.resize((200, 200), Image.ANTIALIAS)  # Adjust the size as needed
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=photo)
image_label.pack()

# Create the button to open the login page
button_open_login = tk.Button(window, text="Open Login Page", command=open_login_page)
button_open_login.pack(pady=20)

# Run the main event loop
window.mainloop()
