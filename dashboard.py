import tkinter as tk
from tkinter import ttk

def show_dashboard():
    # Create the dashboard window
    window = tk.Tk()
    window.title("Dashboard")

    # Create a notebook (tabbed interface)
    notebook = ttk.Notebook(window)

    # Create the Manage Clients tab
    manage_clients_tab = ttk.Frame(notebook)
    notebook.add(manage_clients_tab, text="Manage Clients")

    # Add content to the Manage Clients tab
    label_manage_clients = tk.Label(manage_clients_tab, text="Manage Clients Content")
    label_manage_clients.pack(padx=10, pady=10)

    # Create the Client Invoices tab
    client_invoices_tab = ttk.Frame(notebook)
    notebook.add(client_invoices_tab, text="Client Invoices")

    # Add content to the Client Invoices tab
    label_client_invoices = tk.Label(client_invoices_tab, text="Client Invoices Content")
    label_client_invoices.pack(padx=10, pady=10)

    # Pack the notebook widget
    notebook.pack(fill="both", expand=True)

    # Run the dashboard window
    window.mainloop()