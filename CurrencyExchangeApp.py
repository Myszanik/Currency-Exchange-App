import tkinter as tk

class Currency_Exchange_App:
    def __init__(self, master):
        self.master = master
        master.title("Currency Exchange App")
        master.configure(bg='beige')
        master.geometry("1200x700")
        master.resizable(False, False)

        self.welcome_frame = tk.Frame(master, bg='beige')
        self.main_frame = tk.Frame(master, bg='beige')

        #self.welcome_screen_frame()
        #self.main_screen_frame()

    def welcome_screen_frame(self):
        self.welcome = tk.Label(self.welcome_frame, text='Welcome to Currency Exchange App', font=('Papyrus', 60), fg='black', bg='beige')
        self.welcome.place(x=110, y= 270)
        #self.welcome.bind('<Button-1>', self.welcome_screen_frame)
        #self.continue_button = tk.Button(master, text='Welcome to Currency Exchange App', font=('Papyrus', 60), fg='black', bg='beige', width=26, height=8)
        #self.continue_button.place(x=0, y=0)

    #def main_screen_frame(self):
     #   self.created = tk.Label(self.main_frame, text='Created by Myszanik', font=('Arial', 20), bg='beige', fg='black')
      #  self.created.grid(row=0, column=0)

root = tk.Tk()
ToDoApp = Currency_Exchange_App(root)
root.mainloop()