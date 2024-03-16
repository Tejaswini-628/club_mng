import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import END 
from tkinter import *
from std.FirP import Firstpage
from std.SecP import Secondpage
from coord.CFirP import CFirstpage
from coord.CSecP import CSecondpage
from std.SecP import Mathpage,Musicpage,Happypage,Artspage,Dancepage

class Zeropage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        border = tk.LabelFrame(self, bg='#9BB0C1', bd=10, font=('Arial', 20))
        border.pack(fill="both", expand="yes", padx=90, pady=90)

        # Label displaying "Welcome to Club Hub"
        welcome_label = tk.Label(border, text="Welcome to Club Hub", font=("Arial", 40, "italic", "bold"),  bg="#9BB0C1")
        welcome_label.place(x=25,y=40)

        self.login_type = tk.StringVar()

        style = ttk.Style()
        style.configure('TRadiobutton', font=('Arial', 15), background='#9BB0C1')
        style.map('TRadiobutton', background=[('active', '#F0F0F0')], indicatormargin=[('active', 10)], indicatordiameter=[('active', 10)])

        #E0F4FF

        student_radio = ttk.Radiobutton(border, text="Student Login", variable=self.login_type, value="student", style='TRadiobutton', command=self.navigate)
        student_radio.place(x=220,y=135)

        coordinator_radio = ttk.Radiobutton(border, text="Coordinator Login", variable=self.login_type, value="coordinator", style='TRadiobutton', command=self.navigate)
        coordinator_radio.place(x=220,y=180)

    def navigate(self):
        if self.login_type.get() == "student":
            self.controller.show_frame(Firstpage)
        elif self.login_type.get() == "coordinator":
            self.controller.show_frame(CFirstpage)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.frames = {}
        for F in (Zeropage, Firstpage, Secondpage, CFirstpage, CSecondpage, Mathpage,Musicpage,Dancepage,Artspage,Happypage):
            frame = F(window, controller=self) 
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Zeropage)

    def show_frame(self, page, username=None):
        frame = self.frames[page]
        frame.tkraise()
        if username:
            frame.username = username
        if page == Zeropage:
            self.title("Club Hub")
        elif page == Firstpage:
            self.title("Student Login")
        elif page == Secondpage:
            self.title("Clubs Info")
        elif page == Dancepage:
            self.title("Dance Club")
        elif page == Musicpage:
            self.title("Music Club")
        elif page == Artspage:
            self.title("Arts Club")
        elif page == Happypage:
            self.title("Happy Club")
        elif page == CFirstpage:
            self.title("Coordinator Login")
        elif page == CSecondpage:
            self.title("Requests")
        elif page == Mathpage:
            self.title("Math Club")


app = Application()
app.maxsize(800, 500)
app.mainloop()
