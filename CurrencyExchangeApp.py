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
        self.description= tk.Label(self.main_frame, text='')
        self.created_by = tk.Label(self.main_frame, text='Created by Myszanik', font=('Arial', 20), bg='beige', fg='black')
        self.created_by.place(x=440, y=700)

    def switch_scene(self):
        # Hide the welcome frame and show the main frame
        self.welcome_frame.lower()  # Hides the welcome frame
        self.main_frame.lift()  # Shows the main frame


root = tk.Tk()
ToDoApp = Currency_Exchange_App(root)
root.mainloop()
