import tkinter as tk
from tkinter import ttk
import requests

class Currency_Exchange_App:
    def __init__(self, master):
        self.master = master

        # Window settings
        master.title("Currency Exchange App")
        master.configure(bg='beige')
        master.geometry("1076x748")
        master.resizable(False, False)

        # Welcome frame that shows first
        self.welcome_frame = tk.Frame(master, bg='beige')
        self.welcome_frame.place(x=0, y=0, width=1076, height=748)

        # Main frame that is hidden initially
        self.main_frame = tk.Frame(master, bg='beige')
        self.main_frame.place(x=0, y=0, width=1076, height=748)
        self.main_frame.lower()  # Hide main frame initially

        # Setup the screens
        self.welcome_screen_frame()
        self.main_screen_frame()

        # Fetch currencies when the app starts
        self.fetch_currencies()

    def welcome_screen_frame(self):
        # Welcome label
        self.welcome = tk.Label(
            self.welcome_frame,
            text='Welcome to Currency Exchange App',
            font=('Papyrus', 60),
            fg='black',
            bg='beige'
        )
        self.welcome.place(x=110, y=270)

        # Full-screen button
        self.continue_button = tk.Button(
            self.welcome_frame,
            text='Welcome to Currency Exchange App',
            font=('Papyrus', 60),
            bg='beige',
            width=26,
            height=8,
            command=self.switch_scene
        )
        self.continue_button.place(x=0, y=0)

    def main_screen_frame(self):
        # Main screen label
        self.description = tk.Label(
            self.main_frame,
            text='Welcome!',
            font=('Papyrus', 60),
            fg='black',
            bg='beige'
        )
        self.description.place(x=415, y=5)

        self.description = tk.Label(
            self.main_frame,
            text='Please choose currency you want to exchange and the amount',
            font=('Papyrus', 38),
            fg='black',
            bg='beige'
        )
        self.description.place(x=5, y=100)

        # From currency selection
        self.from_currency_description = tk.Label(
            self.main_frame,
            text='Select from currency',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.from_currency_description.place(x=170, y=180)

        self.from_currency_var = tk.StringVar(self.main_frame)
        self.from_currency_var.set("From")  # Default text

        # Using ttk.Combobox for searchable dropdown
        self.from_currency = ttk.Combobox(
            self.main_frame,
            textvariable=self.from_currency_var,
            font=('Verdana', 23),
            width=10
        )
        self.from_currency.place(x=170, y=225)
        self.from_currency.bind("<KeyRelease>", self.filter_currencies_from)  # Bind for real-time filtering

        # Entry field for amount
        self.entry_description = tk.Label(
            self.main_frame,
            text='Enter amount below',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.entry_description.place(x=455, y=180)

        self.entry = tk.Entry(
            self.main_frame,
            width=16,
            font=('Verdana', 25),
            bg='white',
            fg='black',
            insertbackground='black'
        )
        self.entry.place(x=405, y=220)  # Adjust x and y based on your window layout
        self.entry.focus_set()  # Set focus to the entry widget

        # To currency selection
        self.to_currency_description = tk.Label(
            self.main_frame,
            text='Select to currency',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.to_currency_description.place(x=720, y=180)

        self.to_currency_var = tk.StringVar(self.main_frame)
        self.to_currency_var.set("To")  # Default text

        # Using ttk.Combobox for searchable dropdown
        self.to_currency = ttk.Combobox(
            self.main_frame,
            textvariable=self.to_currency_var,
            font=('Verdana', 23),
            width=10
        )
        self.to_currency.place(x=720, y=225)
        self.to_currency.bind("<KeyRelease>", self.filter_currencies_to)  # Bind for real-time filtering

        # Convert button
        self.convert_button = tk.Button(
            self.main_frame,
            width=35,
            text='Convert',
            font=('Avenir', 22),
            bg='beige',
            fg='black'
        )
        self.convert_button.place(x=295, y=310)

        # Labels for original and converted currencies
        self.original_currency = tk.Label(
            self.main_frame,
            text='Original Currency: ',
            font=('Verdana', 22),
            bg='beige',
            fg='black'
        )
        self.original_currency.place(x=440, y=380)

        self.canvas = tk.Canvas(
            self.main_frame,
            width=120,
            height=120,
            bg='beige',
            highlightthickness=0
        )
        self.canvas.place(x=470, y=440)  # Adjust x and y as needed
        self.canvas.create_line(70, 5, 70, 100, arrow=tk.LAST, fill='black', width=2)

        self.converted_currency = tk.Label(
            self.main_frame,
            text='Converted Currency: ',
            font=('Verdana', 22),
            bg='beige',
            fg='black'
        )
        self.converted_currency.place(x=430, y=580)

        self.exchange_rate = tk.Label(
            self.main_frame,
            text='Exchange Rate: ',
            font=('Verdana', 22),
            bg='beige',
            fg='black'
        )
        self.exchange_rate.place(x=605, y=475)

        # Label for creator credit
        self.created_by = tk.Label(
            self.main_frame,
            text='Created by Myszanik',
            font=('Arial', 20),
            bg='beige',
            fg='black'
        )
        self.created_by.place(x=440, y=710)

    def switch_scene(self):
        # Hide the welcome frame and show the main frame
        self.welcome_frame.lower()  # Hides the welcome frame
        self.main_frame.lift()  # Shows the main frame

    # Fetch currencies from the API
    def fetch_currencies(self):
        # Your API key
        api_key = "REMOVED_OLD_KEY"
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.currencies = list(data['conversion_rates'].keys())  # Fetch currency codes

            # Update both comboboxes (from and to)
            self.update_combobox(self.from_currency, self.currencies)
            self.update_combobox(self.to_currency, self.currencies)
        else:
            print("Error fetching data")

    # A method to update any combobox
    def update_combobox(self, combobox, currencies):
        combobox['values'] = currencies
        combobox.set("")  # Default placeholder text

    # Filter the currencies based on user input (for from_currency)
    def filter_currencies_from(self, event):
        value = self.from_currency_var.get().lower()
        filtered_currencies = [cur for cur in self.currencies if value in cur.lower()]
        self.from_currency['values'] = filtered_currencies

    # Filter the currencies based on user input (for to_currency)
    def filter_currencies_to(self, event):
        value = self.to_currency_var.get().lower()
        filtered_currencies = [cur for cur in self.currencies if value in cur.lower()]
        self.to_currency['values'] = filtered_currencies

# Create and run the application
root = tk.Tk()
ToDoApp = Currency_Exchange_App(root)
root.mainloop()
