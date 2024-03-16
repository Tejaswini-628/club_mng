import tkinter as tk
from tkinter import ttk
import mysql.connector

class CSecondpage(tk.Frame):
    def __init__(self, parent, controller, callback=None, message=""):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.callback = callback

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Store the canvas frame id
        self.canvas_frame_id = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        self.load_data()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame_id, width=event.width)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")


    def load_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", database="register", user="root", password="Sowmya@333"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT username, club_name FROM joinclub")
            rows = cursor.fetchall()

            for row in rows:
                frame = tk.Frame(self.frame, relief="solid", borderwidth=1.5)
                frame.pack(fill="x", padx=10, pady=5)

                username_label = tk.Label(frame, text="Username: " + row[0], font=("Arial", 13))
                username_label.grid(row=0, column=0, padx=10, pady=5)

                clubname_label = tk.Label(frame, text="Club Name: " + row[1], font=("Arial", 13))
                clubname_label.grid(row=0, column=1, padx=(10, 30), pady=5)

                # accept_button = tk.Button(frame, text="Accept", width=10, height=2, command=lambda f=frame, u=row[0], c=row[1]: self.accept_request(f, u, c),bg="#A8CD9F")

                # accept_button.grid(row=0, column=2, padx=(0, 10), pady=5, sticky="e")

                # decline_button = tk.Button(frame, text="Decline", width=10, height=2, command=lambda f=frame, u=row[0], c=row[1]: self.decline_request(f, u, c),bg="#F28585")
                # decline_button.grid(row=0, column=3, padx=(30, 10), pady=5, sticky="w")  # Increased padx between accept and decline buttons

                accept_button = tk.Button(frame, text="Accept", width=10, height=1, command=lambda f=frame, u=row[0], c=row[1]: self.accept_request(f, u, c), bg="#A8CD9F")
                accept_button.place(x=550, y=2.5)  # Adjust x and y coordinates as needed

                decline_button = tk.Button(frame, text="Decline", width=10, height=1, command=lambda f=frame, u=row[0], c=row[1]: self.decline_request(f, u, c), bg="#F28585")
                decline_button.place(x=650, y=2.5)  # Adjust x and y coordinates as needed


            conn.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def accept_request(self, frame, username, club_name):
        try:
            conn = mysql.connector.connect(
                host="localhost", database="register", user="root", password="Sowmya@333"
            )
            cursor = conn.cursor()
            cursor.execute("UPDATE joinclub SET accept = 1 WHERE username = %s AND club_name = %s", (username, club_name))
            conn.commit()
            conn.close()
            frame.destroy()  # Destroy the frame associated with the accept button
        except mysql.connector.Error as err:
            print("Error:", err)

    def decline_request(self, frame, username, club_name):
        try:
            conn = mysql.connector.connect(
                host="localhost", database="register", user="root", password="Sowmya@333"
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM joinclub WHERE username = %s AND club_name = %s", (username, club_name))
            conn.commit()
            conn.close()
            frame.destroy()  # Destroy the frame associated with the decline button
        except mysql.connector.Error as err:
            print("Error:", err)



# # Usage example
# root = tk.Tk()
# app = CSecondpage(root, None)
# app.pack(fill="both", expand=True)
# root.mainloop()
