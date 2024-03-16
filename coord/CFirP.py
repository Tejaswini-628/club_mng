import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import END 
import mysql.connector
from tkinter import *
from .CSecP import CSecondpage

class CFirstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        border = tk.LabelFrame(self, text=' Coordinator  Login ', bg='#F1F0E8', bd=10, font=('Arial', 18))
        border.pack(fill="both", expand="yes", padx=150, pady=150)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='#F8F6F4')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='#F8F6F4')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            username = T1.get()
            password = T2.get()
            if username == '' or password == '':
                messagebox.showerror('Enter all fields')
            else:
                try:
                    con = mysql.connector.connect(host="localhost", database="register", user="root", password="Sowmya@333")
                    c = con.cursor()
                except:
                    messagebox.showerror('connection problem !! try again')
                    return

                sqlquery = 'use register'

                sqlquery = "SELECT id, username, password FROM coordinator WHERE username=%s and password=%s"
                c.execute(sqlquery, (username, password))
                result = c.fetchone()
       
                if result: 
                    id,username,password = result 
                    messagebox.showinfo("Welcome", "Coordinator Login is successfull")
                    controller.show_frame(CSecondpage) 
                else:
                    messagebox.showerror("Error", "Invalid Login!! Try Again")

        B1 = tk.Button(border, text="Submit", bg="#D2E0FB", font=("Arial", 15), command=verify)
        B1.place(x=370, y=115)

        def register():
            root = Tk()
            root.title("Register")
            connection = mysql.connector.connect(host='localhost',user='root',password='Sowmya@333',port='3306',database='register')
            c = connection.cursor()
            bkg="#8EACCD"
            
            frame=tk.Frame(root,bg=bkg)

            label_username = tk.Label(frame, text="Username: ", font=('verdana',12),bg=bkg)
            entry_username = tk.Entry(frame)

            label_password = tk.Label(frame, text="Password: ", font=('verdana',12),bg=bkg)
            entry_password = tk.Entry(frame)

            label_cpassword = tk.Label(frame, text="Confirm Password: ", font=('verdana',12),bg=bkg)
            entry_cpassword = tk.Entry(frame)


            def insertData():
                if entry_username.get()!="" or entry_password.get()!="" or entry_cpassword.get()!="":
                    if entry_password.get()==entry_cpassword.get():
                        username = entry_username.get()
                        password = entry_password.get()
                        cpassword = entry_cpassword.get()
                        
                        insert_query = "INSERT INTO `coordinator` (`username`, `password`, `cpassword`) VALUES (%s, %s, %s)"
                        values=(username,password,cpassword)
                        c.execute(insert_query,values)
                        connection.commit()

                        entry_username.delete(0,END)
                        entry_password.delete(0,END)
                        entry_cpassword.delete(0,END)
                        messagebox.showinfo("Welcome","You are registered succesfully!!")

                        root.destroy()
                        controller.show_frame(CFirstpage)
                    else:
                        messagebox.showinfo("Welcome","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error","Please fill your details!!")


            button_insert = tk.Button(frame, text="Sign-Up", font=('verdana',14),bg='#FBF9F1',command= insertData)

            label_username.grid(row=0, column=0,sticky='e')
            entry_username.grid(row=0, column=1, pady=15 , padx=15)

            label_password.grid(row=1, column=0,sticky='e',pady=10 , padx=10)
            entry_password.grid(row=1, column=1,pady=15 , padx=15)
            
            label_cpassword.grid(row=2, column=0,sticky='e',pady=10 , padx=10)
            entry_cpassword.grid(row=2, column=1,pady=15 , padx=15)
            
            button_insert.grid(row=3,column=0, columnspan=2,pady=10 , padx=10)
            frame.grid(row=0, column=0) 

            root.mainloop()
            pass

        B2 = tk.Button(self, text="Register", bg="#8EACCD", font=("Arial", 15), command=register)
        B2.place(x=650, y=20)