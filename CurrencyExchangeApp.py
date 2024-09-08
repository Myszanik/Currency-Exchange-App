import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

class CurrencyExchangeApp:
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
        self.fetch_country_data()  # Add this line to ensure country data is fetched

        # Bind Enter key to the conversion function
        self.master.bind('<Return>', self.on_enter_press)

        # Bind key release to capitalize first letter
        self.from_currency_entry.bind('<KeyRelease>', self.capitalize_letter)
        self.to_currency_entry.bind('<KeyRelease>', self.capitalize_letter)

        # Load and display the logo image
        self.logo_image = self.load_image("/Users/dom/Downloads/Exchange App.jpeg", (95, 95))
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Create a Label widget to hold the image
        self.logo_label = tk.Label(self.main_frame, image=self.logo_photo, bg='beige')
        self.logo_label.place(x=0, y=0)  # Adjust the position as needed

        # Create a Label widget to hold the image
        self.logo_label_1 = tk.Label(self.main_frame, image=self.logo_photo, bg='beige')
        self.logo_label_1.place(x=977, y=0)  # Adjust the position as needed

        # Initialize flag labels
        self.flag_1 = tk.Label(self.main_frame, bg='beige')
        self.flag_1.place(x=12, y=245)
        self.flag_1.place_forget()

        self.flag_2 = tk.Label(self.main_frame, bg='beige')
        self.flag_2.place(x=960, y=245)
        self.flag_2.place_forget()

    def load_image(self, image_path, size):
        # Open the image file
        image = Image.open(image_path)
        # Resize the image
        image = image.resize(size, Image.LANCZOS)  # Use LANCZOS for high-quality resizing
        return image

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
            text='Click anywhere to continue to the Currency Exchange App',
            font=('Papyrus', 60),
            width=26,
            height=8,
            wraplength=1000,  # Adjust width to fit your needs
            justify='center',
            command=self.switch_scene
        )
        self.continue_button.place(x=0, y=0)

    def main_screen_frame(self):
        # Main screen label
        self.description = tk.Label(
            self.main_frame,
            text='Welcome to Currency Exchange App',
            font=('Tisa', 55),
            fg='black',
            bg='beige'
        )
        self.description.place(x=110, y=12)

        self.description = tk.Label(
            self.main_frame,
            text='Enter country names and amount to display exchange',
            font=('Papyrus', 43, 'bold'),
            fg='black',
            bg='beige'
        )
        self.description.place(x=20, y=130)

        # From currency input
        self.from_currency_description = tk.Label(
            self.main_frame,
            text='Convert From',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.from_currency_description.place(x=190, y=230)

        self.from_currency_entry = tk.Entry(
            self.main_frame,
            font=('Verdana', 23),
            width=14,
            justify='center'
        )
        self.from_currency_entry.place(x=140, y=265)

        # Entry field for amount
        self.amount_entry_description = tk.Label(
            self.main_frame,
            text='Enter Amount to Convert',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.amount_entry_description.place(x=430, y=230)

        self.amount_entry = tk.Entry(
            self.main_frame,
            width=16,
            font=('Verdana', 25),
            bg='white',
            fg='black',
            insertbackground='black',
            justify='center'
        )
        self.amount_entry.place(x=405, y=265)  # Adjust x and y based on your window layout

        # To currency input
        self.to_currency_description = tk.Label(
            self.main_frame,
            text='Convert To',
            font=('Verdana', 16),
            bg='beige',
            fg='black'
        )
        self.to_currency_description.place(x=780, y=230)

        self.to_currency_entry = tk.Entry(
            self.main_frame,
            font=('Verdana', 23),
            width=14,
            justify='center'
        )
        self.to_currency_entry.place(x=715, y=265)

        # Convert button
        self.convert_button = tk.Button(
            self.main_frame,
            width=35,
            text='Convert',
            font=('Avenir', 22, 'bold'),
            bg='beige',
            fg='black',
            command=self.convert_currency
        )
        self.convert_button.place(x=275, y=350)

        # Labels for original and converted currencies
        self.original_currency = tk.Label(
            self.main_frame,
            text='Original Currency: ',
            font=('Verdana', 22),
            bg='beige',
            fg='black'
        )
        self.original_currency.place(x=350, y=445)
        self.original_currency.place_forget()

        self.canvas = tk.Canvas(
            self.main_frame,
            width=120,
            height=120,
            bg='beige',
            highlightthickness=0
        )
        self.canvas.place(x=470, y=510)  # Adjust x and y as needed
        self.canvas.create_line(70, 5, 70, 100, arrow=tk.LAST, fill='black', width=2)
        self.canvas.place_forget()

        self.canvas_0 = tk.Canvas(
            self.main_frame,
            width=0,
            height=110,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_0.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_0.place(x=130, y=220)

        self.canvas_1 = tk.Canvas(
            self.main_frame,
            width=0,
            height=110,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_1.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_1.place(x=370, y=220)

        self.canvas_2 = tk.Canvas(
            self.main_frame,
            width=0,
            height=110,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_2.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_2.place(x=705, y=220)

        self.canvas_3 = tk.Canvas(
            self.main_frame,
            width=0,
            height=110,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_3.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_3.place(x=945, y=220)

        self.canvas_4 = tk.Canvas(
            self.main_frame,
            width=0,
            height=300,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_4.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_4.place(x=945, y=410)

        self.canvas_5 = tk.Canvas(
            self.main_frame,
            width=0,
            height=300,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_5.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_5.place(x=135, y=410)

        self.canvas_6 = tk.Canvas(
            self.main_frame,
            width=0,
            height=80,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_6.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_6.place(x=205, y=330)

        self.canvas_7 = tk.Canvas(
            self.main_frame,
            width=0,
            height=80,
            bg='beige',
            highlightthickness=1
        )
        self.canvas_7.create_line(70, 5, 70, 100, fill='black', width=2)
        self.canvas_7.place(x=870, y=330)

        self.horizontal_line = tk.Canvas(
            self.main_frame,
            width=1200,
            height=0,
            bg='beige',
            highlightthickness=1
        )
        self.horizontal_line.create_line(0, 0, 1076, 0, fill='black', width=3)
        self.horizontal_line.place(x=0, y=100)

        self.horizontal_line_1 = tk.Canvas(
            self.main_frame,
            width=1200,
            height=0,
            bg='beige',
            highlightthickness=1
        )
        self.horizontal_line_1.create_line(0, 0, 1076, 0, fill='black', width=3)
        self.horizontal_line_1.place(x=0, y=220)

        self.horizontal_line_2 = tk.Canvas(
            self.main_frame,
            width=1200,
            height=0,
            bg='beige',
            highlightthickness=1
        )
        self.horizontal_line_2.create_line(0, 0, 1076, 0, fill='black', width=3)
        self.horizontal_line_2.place(x=0, y=330)

        self.horizontal_line_3 = tk.Canvas(
            self.main_frame,
            width=1200,
            height=0,
            bg='beige',
            highlightthickness=1
        )
        self.horizontal_line_3.create_line(0, 0, 1076, 0, fill='black', width=3)
        self.horizontal_line_3.place(x=0, y=410)

        self.horizontal_line_4 = tk.Canvas(
            self.main_frame,
            width=1200,
            height=0,
            bg='beige',
            highlightthickness=1
        )
        self.horizontal_line_4.create_line(0, 0, 1076, 0, fill='black', width=3)
        self.horizontal_line_4.place(x=0, y=710)

        self.converted_currency = tk.Label(
            self.main_frame,
            text='Converted Currency: ',
            font=('Verdana', 22),
            bg='beige',
            fg='black'
        )
        self.converted_currency.place(x=340, y=650)
        self.converted_currency.place_forget()

        self.exchange_rate = tk.Label(
            self.main_frame,
            text='Exchange Rate: ',
            font=('Verdana', 22),
            bg='beige',
            fg='green'
        )
        self.exchange_rate.place(x=605, y=545)
        self.exchange_rate.place_forget()

        # Label for creator credit
        self.created_by = tk.Label(
            self.main_frame,
            text='Created by Myszanik',
            font=('Arial', 18, 'bold'),
            bg='beige',
            fg='#36454F'
        )
        self.created_by.place(x=450, y=715)

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

    def fetch_country_data(self):
        url = 'https://restcountries.com/v3.1/all?fields=name,flags,currencies'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.country_data = {}
            for country in data:
                try:
                    name = country['name']['common'].title()  # Normalize to title case
                    flag_url = country['flags']['png']  # Use the PNG flag URL
                    currencies = list(country['currencies'].keys())
                    if currencies:
                        self.country_data[name] = {
                            'flag': flag_url,
                            'currencies': currencies[0]
                        }
                except KeyError as e:
                    print(f"KeyError: {e} in country data: {country}")
                    continue

            # Debugging print to check available country names and flag URLs
            print("Available countries and flags:", {k: v['flag'] for k, v in self.country_data.items()})
        else:
            print("Error fetching data")
            self.country_data = {}

    def convert_currency(self):
        from_currency = self.from_currency_entry.get().strip().title()  # Capitalize properly
        to_currency = self.to_currency_entry.get().strip().title()  # Capitalize properly
        amount = self.amount_entry.get().strip()

        # Update flag images before changing country names to currency codes
        self.update_flag_images(from_currency, to_currency)

        # Replace country names with their currency codes if needed
        if from_currency in self.country_data:
            from_currency = self.country_data[from_currency]['currencies']
            self.from_currency_entry.delete(0, tk.END)
            self.from_currency_entry.insert(0, from_currency)

        if to_currency in self.country_data:
            to_currency = self.country_data[to_currency]['currencies']
            self.to_currency_entry.delete(0, tk.END)
            self.to_currency_entry.insert(0, to_currency)

        # Show labels when button pressed
        self.original_currency.place(x=350, y=445)
        self.converted_currency.place(x=340, y=650)
        self.exchange_rate.place(x=605, y=545)
        self.canvas.place(x=470, y=510)
        self.flag_1.place(x=12, y=245)
        self.flag_2.place(x=960, y=245)

        # Proceed with conversion if currency codes are valid
        if from_currency in self.currencies and to_currency in self.currencies:
            try:
                amount = float(amount)  # Convert amount to float
                from_rate = self.currencies[from_currency]
                to_rate = self.currencies[to_currency]
                conversion_rate = to_rate / from_rate
                converted_amount = amount * conversion_rate

                self.original_currency.config(text=f'Original Currency: {amount:.2f} {from_currency}')
                self.converted_currency.config(text=f'Converted Currency: {converted_amount:.2f} {to_currency}')
                self.exchange_rate.config(text=f'Exchange Rate: {conversion_rate:.2f}')
            except ValueError:
                self.original_currency.config(text='Invalid amount. Please enter a number.')
        else:
            self.original_currency.config(text='Invalid currency code(s).')

        self.master.update_idletasks()

    def update_flag_images(self, from_currency, to_currency):
        # Get flag URLs based on currency codes
        flag_url_1 = self.get_flag_url(from_currency)  # Use the actual country name here
        flag_url_2 = self.get_flag_url(to_currency)  # Use the actual country name here

        # Update flag 1
        if flag_url_1:
            try:
                response = requests.get(flag_url_1)
                image = Image.open(BytesIO(response.content))
                image = image.resize((100, 60), Image.LANCZOS)
                self.flag_1_image = ImageTk.PhotoImage(image)
                self.flag_1.config(image=self.flag_1_image)
            except Exception as e:
                print(f"Error loading flag for {from_currency}: {e}")
                self.flag_1.config(image='')
        else:
            print("No flag URL for flag 1")
            self.flag_1.config(image='')

        # Update flag 2
        if flag_url_2:
            try:
                response = requests.get(flag_url_2)
                image = Image.open(BytesIO(response.content))
                image = image.resize((100, 60), Image.LANCZOS)
                self.flag_2_image = ImageTk.PhotoImage(image)
                self.flag_2.config(image=self.flag_2_image)
            except Exception as e:
                print(f"Error loading flag for {to_currency}: {e}")
                self.flag_2.config(image='')
        else:
            print("No flag URL for flag 2")
            self.flag_2.config(image='')

    def get_flag_url(self, country_name):
        for country, data in self.country_data.items():
            if country_name == country:
                return data['flag']
        return None

    def on_enter_press(self, event):
        self.convert_currency()
        self.master.update_idletasks()

    def capitalize_letter(self, event):
        # Capitalize the first letter of the content in the entry widgets
        if event.widget == self.from_currency_entry:
            content = self.from_currency_entry.get()
            # Capitalize the first letter and set it back
            self.from_currency_entry.delete(0, tk.END)
            self.from_currency_entry.insert(0, content.upper())
        elif event.widget == self.to_currency_entry:
            content = self.to_currency_entry.get()
            # Capitalize the first letter and set it back
            self.to_currency_entry.delete(0, tk.END)
            self.to_currency_entry.insert(0, content.upper())

# Create and run the application
root = tk.Tk()
app = CurrencyExchangeApp(root)
root.mainloop()
