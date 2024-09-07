import tkinter as tk
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
            text='Please type currency codes and the amount below',
            font=('Papyrus', 45),
            fg='black',
            bg='beige'
        )
        self.description.place(x=30, y=100)

        # From currency input
        self.from_currency_description = tk.Label(
            self.main_frame,
            text='From currency code',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.from_currency_description.place(x=170, y=180)

        self.from_currency_entry = tk.Entry(
            self.main_frame,
            font=('Verdana', 23),
            width=10
        )
        self.from_currency_entry.place(x=170, y=225)

        # Entry field for amount
        self.amount_entry_description = tk.Label(
            self.main_frame,
            text='Enter amount below',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.amount_entry_description.place(x=455, y=180)

        self.amount_entry = tk.Entry(
            self.main_frame,
            width=16,
            font=('Verdana', 25),
            bg='white',
            fg='black',
            insertbackground='black'
        )
        self.amount_entry.place(x=405, y=220)  # Adjust x and y based on your window layout
        self.amount_entry.focus_set()  # Set focus to the entry widget

        # To currency input
        self.to_currency_description = tk.Label(
            self.main_frame,
            text='To currency code',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.to_currency_description.place(x=720, y=180)

        self.to_currency_entry = tk.Entry(
            self.main_frame,
            font=('Verdana', 23),
            width=10
        )
        self.to_currency_entry.place(x=720, y=225)

        # Convert button
        self.convert_button = tk.Button(
            self.main_frame,
            width=35,
            text='Convert',
            font=('Avenir', 22),
            bg='beige',
            fg='black',
            command=self.convert_currency
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

    def fetch_currencies(self):
        # Your API key
        api_key = "REMOVED_OLD_KEY"
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.currencies = data['conversion_rates']  # Fetch all conversion rates
        else:
            print("Error fetching data")
            self.currencies = {}  # Default to empty if there's an error

    def convert_currency(self):
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()
        amount = self.amount_entry.get()

        if from_currency in self.currencies and to_currency in self.currencies:
            try:
                amount = float(amount)
                from_rate = self.currencies[from_currency]
                to_rate = self.currencies[to_currency]
                conversion_rate = to_rate / from_rate
                converted_amount = amount * conversion_rate

                self.original_currency.config(text=f'Original Currency: {amount} {from_currency}')
                self.converted_currency.config(text=f'Converted Currency: {converted_amount:.2f} {to_currency}')
                self.exchange_rate.config(text=f'Exchange Rate: {conversion_rate:.2f}')
            except ValueError:
                self.original_currency.config(text='Invalid amount. Please enter a number.')
        else:
            self.original_currency.config(text='Invalid currency code(s).')

# Create and run the application
root = tk.Tk()
app = Currency_Exchange_App(root)
root.mainloop()
