import tkinter as tk
import mysql.connector 
from tkinter import messagebox

class JoinWindow(tk.Toplevel):
    def __init__(self, controller, club_name):  # Pass club_name as a parameter
        super().__init__()
        self.controller = controller
        self.club_name = club_name  # Store the club name

        self.title("Join")
        self.geometry("400x200")
        self.configure(bg="#3876BF")

        self.username_label = tk.Label(self, text="Username : ", font=("Arial", 14), bg="#3876BF", fg="white")
        self.username_label.place(x=50, y=70)  # Adjusted placement to the left side
        self.username_entry = tk.Entry(self, width=20, font=("Arial", 12)) 
        self.username_entry.place(x=153, y=73)  

        self.join1_button = tk.Button(self, text="JOIN", font=("Arial", 12), command=self.join_action, bg="#F3F0CA")  
  
        self.join1_button.place(x=170, y=120)

        # self.no_requests_label = tk.Label(self, text="No requests", font=("Arial", 14), bg="#3876BF", fg="white")

    def join_action(self):
        username = self.username_entry.get()
        if username:
            try:
                conn = mysql.connector.connect(
                    host="localhost", database="register", user="root", password="Sowmya@333"
                )
                
                cursor = conn.cursor()
                
                # Check if username exists in the student table
                cursor.execute("SELECT * FROM student WHERE username = %s", (username,))
                if cursor.fetchone():  # If username exists
                    # Check if the accept status is 1
                    cursor.execute("SELECT accept FROM joinclub WHERE username = %s AND club_name = %s", (username, self.club_name))
                    row = cursor.fetchone()
                    if row and row[0] == 1:  # If accept status is 1
                        messagebox.showinfo("Already Joined", "You have already joined this club!")
                    else:
                        # Insert into joinclub table
                        cursor.execute("INSERT INTO joinclub (username, club_name) VALUES (%s, %s)", (username, self.club_name))
                        conn.commit()
                        conn.close()

                        self.controller.logged_in_username = username
                        self.controller.event_generate("<<LoginSuccess>>")
                        self.destroy()  
                        messagebox.showinfo("Success", "Join request sent successfully!")
                else:
                    messagebox.showerror("Error", "Username does not exist.")
            except mysql.connector.Error as err:
                print("Error:", err) 
        else:
            tk.messagebox.showerror("Error", "Please enter a username.")

