import tkinter as tk


class Currency_Exchange_App:
    def __init__(self, master):
        self.master = master
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

    def welcome_screen_frame(self):
        # Welcome label
        self.welcome = tk.Label(self.welcome_frame, text='Welcome to Currency Exchange App', font=('Papyrus', 60), fg='black', bg='beige')
        self.welcome.place(x=110, y=270)

        # Full-screen button
        self.continue_button = tk.Button(self.welcome_frame, text='Welcome to Currency Exchange App', font=('Papyrus', 60), bg='beige', width=26, height=8,command=self.switch_scene)
        self.continue_button.place(x=0, y=0)

    def main_screen_frame(self):
        # Main screen label
        self.description= tk.Label(self.main_frame, text='Welcome!', font=('Papyrus', 60), fg='black', bg='beige')
        self.description.place(x=415, y=5)
        self.description = tk.Label(self.main_frame, text='Please choose currency you want to exchange and the amount', font=('Papyrus', 35), fg='black', bg='beige')
        self.description.place(x=50, y=80)
        self.from_currency_description = tk.Label(self.main_frame, text='Choose from currency', font=('Verdana', 20), bg='beige', fg='black')
        self.from_currency_description.place(x=150, y=150)
        # Create a variable to store the selected value
        self.from_currency_var = tk.StringVar(self.main_frame)
        self.from_currency_var.set("From")  # Default text
        self.from_currency = tk.OptionMenu(self.main_frame, self.from_currency_var, *[0])
        self.from_currency.config(bd=0, width=4, height=0, font=('Verdana', 25), highlightbackground="beige", highlightcolor="beige", highlightthickness=0, relief='flat')
        self.from_currency.place(x=220, y=195)
        self.entry_description = tk.Label(self.main_frame, text='Enter amount below', font=('Verdana', 20), bg='beige', fg='black')
        self.entry_description.place(x=435, y=150)
        self.entry = tk.Entry(self.main_frame, width=16, font=('Verdana', 25), bg='white', fg='black', insertbackground='black')
        self.entry.place(x=405, y=190)  # Adjust x and y based on your window layout
        self.entry.focus_set()  # Set focus to the entry widget
        self.to_currency_description = tk.Label(self.main_frame, text='Choose to currency', font=('Verdana', 20), bg='beige', fg='black')
        self.to_currency_description.place(x=700, y=150)
        self.to_currency_var = tk.StringVar(self.main_frame)
        self.to_currency_var.set("To")  # Default text
        self.to_currency = tk.OptionMenu(self.main_frame, self.to_currency_var, *[0])
        self.to_currency.config(bd=0, width=4, height=0, font=('Verdana', 25), highlightbackground="beige", highlightcolor="beige", highlightthickness=0, relief='flat')
        self.to_currency.place(x=760, y=195)
        self.created_by = tk.Label(self.main_frame, text='Created by Myszanik', font=('Arial', 20), bg='beige', fg='black')
        self.created_by.place(x=440, y=710)

    def switch_scene(self):
        # Hide the welcome frame and show the main frame
        self.welcome_frame.lower()  # Hides the welcome frame
        self.main_frame.lift()  # Shows the main frame


root = tk.Tk()
ToDoApp = Currency_Exchange_App(root)
root.mainloop()
