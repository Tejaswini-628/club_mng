import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import END 
from tkinter import *
from .join import JoinWindow
import mysql.connector 

class Secondpage(tk.Frame):
    def __init__(self, parent, controller, username=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = username
        self.callback = None
        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(main_frame)
        canvas.pack(side="left", fill="both", expand=True)

        canvas.focus_set()

        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)

        # def on_mousewheel(event):
        #     canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        # canvas.bind_all("<MouseWheel>", on_mousewheel)

        # Create a frame to hold the labels
        label_container = tk.Frame(canvas)
        canvas.create_window((0, 0), window=label_container, anchor="nw")

        # Function to configure the canvas scroll region
        def configure_canvas(event):
            canvas.config(scrollregion=canvas.bbox("all"))

        label_container.bind("<Configure>", configure_canvas)

        # Create labels
        label_frame1 = tk.Frame(label_container, bg='#FBF9F1', bd=10, width=670, height=200, highlightbackground="black", highlightthickness=1)
        label_frame1.pack(fill="both", expand="yes", padx=(60, 120), pady=20)  

        square_label = tk.Label(label_frame1, bg="blue", width=30, height=10)
        square_label.place(x=10, y=10) 
        
        heading_label = tk.Label(label_frame1, text="MATH CLUB", bg="#FBF9F1", justify="left", font=("Arial", 20 , "italic", "bold"))
        heading_label.place(x=250, y=10)

        description_text = "Where enthusiasts explore the beauty and intricacies of mathematics through engaging discussions, problem-solving, and competitions."
        styled_text = f'"{description_text}"'
        description_label1 = tk.Label(label_frame1, text=styled_text, bg="#FBF9F1", justify="left", font=("Arial", 12), wraplength=350)
        description_label1.place(x=250, y=55)

        more_info_button = tk.Button(label_frame1, text="More Info", bg="gray", fg="white", font=("Arial", 12),command=lambda: controller.show_frame(Mathpage))
        more_info_button.place(x=250, y=130)

        join_button = tk.Button(label_frame1, text="Join", bg="gray", fg="white", font=("Arial", 12), command=self.join_action1, width=8, height=1)
        join_button.place(x=450, y=130)
        self.join_button = join_button



        label_frame2 = tk.Frame(label_container, bg='#FBF9F1', bd=10, width=670, height=200, highlightbackground="black", highlightthickness=1)
        label_frame2.pack(fill="both", expand="yes", padx=(60, 120), pady=20)
        square_label = tk.Label(label_frame2, bg="blue", width=30, height=10)
        square_label.place(x=10, y=10)

        heading_label = tk.Label(label_frame2, text="MUSIC CLUB", bg="#FBF9F1", justify="left", font=("Arial", 20 , "italic", "bold"))
        heading_label.place(x=250, y=10)

        description_text = "Harmonizing creativity and passion, fostering musical talents through collaboration, practice, and performance."
        styled_text = f'"{description_text}"'
        description_label1 = tk.Label(label_frame2, text=styled_text, bg="#FBF9F1", justify="left", font=("Arial", 12), wraplength=350)
        description_label1.place(x=250, y=55)

        more_info_button = tk.Button(label_frame2, text="More Info", bg="gray", fg="white", font=("Arial", 12),command=lambda: controller.show_frame(Musicpage))
        more_info_button.place(x=250, y=130)
        join_button = tk.Button(label_frame2, text="Join", bg="gray", fg="white", font=("Arial", 12), command=self.join_action2, width=8, height=1)
        join_button.place(x=450, y=130)
        self.join_button = join_button




        label_frame3 = tk.Frame(label_container, bg='#FBF9F1', bd=10, width=670, height=200, highlightbackground="black", highlightthickness=1)
        label_frame3.pack(fill="both", expand="yes", padx=(60, 120), pady=20)
        square_label = tk.Label(label_frame3, bg="blue", width=30, height=10)
        square_label.place(x=10, y=10)

        heading_label = tk.Label(label_frame3, text="DANCE CLUB", bg="#FBF9F1", justify="left", font=("Arial", 20 , "italic", "bold"))
        heading_label.place(x=250, y=10)
        description_text = "Experience the rhythm of campus life with our vibrant university dance club."
        styled_text = f'"{description_text}"'
        description_label1 = tk.Label(label_frame3, text=styled_text, bg="#FBF9F1", justify="left", font=("Arial", 12), wraplength=350)
        description_label1.place(x=250, y=55)

        more_info_button = tk.Button(label_frame3, text="More Info", bg="gray", fg="white", font=("Arial", 12),command=lambda: controller.show_frame(Dancepage))
        more_info_button.place(x=250, y=130)
        join_button = tk.Button(label_frame3, text="Join", bg="gray", fg="white", font=("Arial", 12), command=self.join_action3, width=8, height=1)
        join_button.place(x=450, y=130)
        self.join_button = join_button




        label_frame4 = tk.Frame(label_container, bg='#FBF9F1', bd=10, width=670, height=200, highlightbackground="black", highlightthickness=1)
        label_frame4.pack(fill="both", expand="yes", padx=(60, 120), pady=20)
        square_label = tk.Label(label_frame4, bg="blue", width=30, height=10)
        square_label.place(x=10, y=10)

        heading_label = tk.Label(label_frame4, text="HAPPY  CLUB", bg="#FBF9F1", justify="left", font=("Arial", 20 , "italic", "bold"))
        heading_label.place(x=250, y=10)

        description_text = " Spreading joy and fostering positivity through shared experiences and supportive community."
        styled_text = f'"{description_text}"'
        description_label1 = tk.Label(label_frame4, text=styled_text, bg="#FBF9F1", justify="left", font=("Arial", 12), wraplength=350)
        description_label1.place(x=250, y=55)

        more_info_button = tk.Button(label_frame4, text="More Info", bg="gray", fg="white", font=("Arial", 12),command=lambda: controller.show_frame(Happypage))
        more_info_button.place(x=250, y=130)
        join_button = tk.Button(label_frame4, text="Join", bg="gray", fg="white", font=("Arial", 12), command=self.join_action4, width=8, height=1)
        join_button.place(x=450, y=130)
        self.join_button = join_button



        label_frame5 = tk.Frame(label_container, bg='#FBF9F1', bd=10, width=670, height=200, highlightbackground="black", highlightthickness=1)
        label_frame5.pack(fill="both", expand="yes", padx=(60, 120), pady=20)
        square_label = tk.Label(label_frame5, bg="blue", width=30, height=10)
        square_label.place(x=10, y=10)

        heading_label = tk.Label(label_frame5, text="ARTS CLUB", bg="#FBF9F1", justify="left", font=("Arial", 20 , "italic", "bold"))
        heading_label.place(x=250, y=10)

        description_text = "Inspiring creativity and expression through various mediums, fostering artistic growth and appreciation within a vibrant community."
        styled_text = f'"{description_text}"'
        description_label1 = tk.Label(label_frame5, text=styled_text, bg="#FBF9F1", justify="left", font=("Arial", 12), wraplength=350)
        description_label1.place(x=250, y=55)

        more_info_button = tk.Button(label_frame5, text="More Info", bg="gray", fg="white", font=("Arial", 12),command=lambda: controller.show_frame(Artspage))
        more_info_button.place(x=250, y=130)
        join_button = tk.Button(label_frame5, text="Join", bg="gray", fg="white", font=("Arial", 12), command=self.join_action5, width=8, height=1)
        join_button.place(x=450, y=130)
        self.join_button = join_button


    def join_action1(self):
        join_window = JoinWindow(self.controller, "Math Club")
    def join_action2(self):
        join_window = JoinWindow(self.controller, "Music Club")
    def join_action3(self):
        join_window = JoinWindow(self.controller, "Dance Club")
    def join_action4(self):
        join_window = JoinWindow(self.controller, "Happy Club")
    def join_action5(self):
        join_window = JoinWindow(self.controller, "Arts Club")


class Mathpage(tk.Frame):
    def __init__(self, parent, controller, username=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = username
        self.callback = None

        side_nav = tk.Frame(self, bg="lightgray", width=200)  # Increased width
        side_nav.pack(fill="y", side="left")

        events_button = tk.Button(side_nav, text="Events", font=("Arial", 12), width=15)
        events_button.pack(pady=(50, 10), padx=10)
        
        gallery_button = tk.Button(side_nav, text="Gallery", font=("Arial", 12), width=15) 
        gallery_button.pack(pady=10, padx=10)

        notifications_button = tk.Button(side_nav, text="Notifications", font=("Arial", 12), width=15)
        notifications_button.pack(pady=10, padx=10) 

        content_frame = tk.Frame(self)
        content_frame.pack(fill="both", expand=True)

        title_label = tk.Label(content_frame, text="Math Club", font=("Arial", 35, "italic", "bold"), anchor="w")  
        title_label.pack(padx=10, pady=10, fill="x") 
        
        theory_label = tk.Label(content_frame, text="Welcome to the Math Club! We aim to foster a community of ""math enthusiasts and promote mathematical learning ""through various events and programs.",font=("Arial", 13), wraplength=600, justify="left", anchor="w") 
        theory_label.pack(padx=10, pady=(0, 20), fill="x")
        events_label = tk.Label(content_frame, text="Our club organizes regular events such as guest lectures, ""workshops, and problem-solving competitions. We also ""offer tutoring sessions and study groups to support ""students in their mathematical endeavors.",font=("Arial", 13), wraplength=600, justify="left", anchor="w")
        events_label.pack(padx=10, fill="x")  

        back_button = tk.Button(content_frame, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Secondpage))
        back_button.place(x=30, y=300)

class Musicpage(tk.Frame):
    def __init__(self, parent, controller, username=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = username
        self.callback = None

        side_nav = tk.Frame(self, bg="lightgray", width=200)  # Increased width
        side_nav.pack(fill="y", side="left")

        events_button = tk.Button(side_nav, text="Events", font=("Arial", 12), width=15)
        events_button.pack(pady=(50, 10), padx=10)
        
        gallery_button = tk.Button(side_nav, text="Gallery", font=("Arial", 12), width=15) 
        gallery_button.pack(pady=10, padx=10)

        notifications_button = tk.Button(side_nav, text="Notifications", font=("Arial", 12), width=15)
        notifications_button.pack(pady=10, padx=10) 

        content_frame = tk.Frame(self)
        content_frame.pack(fill="both", expand=True)

        title_label = tk.Label(content_frame, text="Music Club", font=("Arial", 35, "italic", "bold"), anchor="w")  
        title_label.pack(padx=10, pady=10, fill="x") 
        
        theory_label = tk.Label(content_frame, text="The Music Club orchestrates harmony and melody, fostering a vibrant community of musicians dedicated to exploring diverse genres and instruments.",font=("Arial", 13), wraplength=600, justify="left", anchor="w") 
        theory_label.pack(padx=10, pady=(0, 20), fill="x")
        events_label = tk.Label(content_frame, text=" From lively jam sessions to captivating performances, members collaborate, learn, and showcase their musical talents. Through rehearsals, workshops, and concerts, the club cultivates a space where passion for music thrives, creating unforgettable sonic experiences for all.",font=("Arial", 13), wraplength=600, justify="left", anchor="w")
        events_label.pack(padx=10, fill="x")  

        back_button = tk.Button(content_frame, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Secondpage))
        back_button.place(x=30, y=300)

class Dancepage(tk.Frame):
    def __init__(self, parent, controller, username=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = username
        self.callback = None

        side_nav = tk.Frame(self, bg="lightgray", width=200)  # Increased width
        side_nav.pack(fill="y", side="left")

        events_button = tk.Button(side_nav, text="Events", font=("Arial", 12), width=15)
        events_button.pack(pady=(50, 10), padx=10)
        
        gallery_button = tk.Button(side_nav, text="Gallery", font=("Arial", 12), width=15) 
        gallery_button.pack(pady=10, padx=10)

        notifications_button = tk.Button(side_nav, text="Notifications", font=("Arial", 12), width=15)
        notifications_button.pack(pady=10, padx=10) 

        content_frame = tk.Frame(self)
        content_frame.pack(fill="both", expand=True)

        title_label = tk.Label(content_frame, text="Dance Club", font=("Arial", 35, "italic", "bold"), anchor="w")  
        title_label.pack(padx=10, pady=10, fill="x") 
        
        theory_label = tk.Label(content_frame, text="The Dance Club ignites the rhythm within, offering a dynamic space for dancers of all levels to move, groove, and express themselves through various dance forms.",font=("Arial", 13), wraplength=600, justify="left", anchor="w") 
        theory_label.pack(padx=10, pady=(0, 20), fill="x")
        events_label = tk.Label(content_frame, text="Through classes, rehearsals, and electrifying performances, the club cultivates a supportive community where passion and creativity flourish on the dance floo",font=("Arial", 13), wraplength=600, justify="left", anchor="w")
        events_label.pack(padx=10, fill="x")  

        back_button = tk.Button(content_frame, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Secondpage))
        back_button.place(x=30, y=300)

class Happypage(tk.Frame):
    def __init__(self, parent, controller, username=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = username
        self.callback = None

        side_nav = tk.Frame(self, bg="lightgray", width=200)  # Increased width
        side_nav.pack(fill="y", side="left")

        events_button = tk.Button(side_nav, text="Events", font=("Arial", 12), width=15)
        events_button.pack(pady=(50, 10), padx=10)
        
        gallery_button = tk.Button(side_nav, text="Gallery", font=("Arial", 12), width=15) 
        gallery_button.pack(pady=10, padx=10)

        notifications_button = tk.Button(side_nav, text="Notifications", font=("Arial", 12), width=15)
        notifications_button.pack(pady=10, padx=10) 

        content_frame = tk.Frame(self)
        content_frame.pack(fill="both", expand=True)

        title_label = tk.Label(content_frame, text="Happy Club", font=("Arial", 35, "italic", "bold"), anchor="w")  
        title_label.pack(padx=10, pady=10, fill="x") 
        
        theory_label = tk.Label(content_frame, text="The Happy Club is a community-driven organization dedicated to fostering joy, positivity, and well-being among its members.",font=("Arial", 13), wraplength=600, justify="left", anchor="w") 
        theory_label.pack(padx=10, pady=(0, 20), fill="x")
        events_label = tk.Label(content_frame, text="Through various activities and events, it aims to spread happiness and create a supportive environment where individuals can thrive emotionally and mentally.Members of the Happy Club come together to share experiences, laughter, and support, creating lasting bonds and uplifting each other's spirits along the way.",font=("Arial", 13), wraplength=600, justify="left", anchor="w")
        events_label.pack(padx=10, fill="x")  

        back_button = tk.Button(content_frame, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Secondpage))
        back_button.place(x=30, y=300)

class Artspage(tk.Frame):
    def __init__(self, parent, controller, username=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = username
        self.callback = None

        side_nav = tk.Frame(self, bg="lightgray", width=200)  # Increased width
        side_nav.pack(fill="y", side="left")

        events_button = tk.Button(side_nav, text="Events", font=("Arial", 12), width=15)
        events_button.pack(pady=(50, 10), padx=10)
        
        gallery_button = tk.Button(side_nav, text="Gallery", font=("Arial", 12), width=15) 
        gallery_button.pack(pady=10, padx=10)

        notifications_button = tk.Button(side_nav, text="Notifications", font=("Arial", 12), width=15)
        notifications_button.pack(pady=10, padx=10) 

        content_frame = tk.Frame(self)
        content_frame.pack(fill="both", expand=True)

        title_label = tk.Label(content_frame, text="Arts Club", font=("Arial", 35, "italic", "bold"), anchor="w")  
        title_label.pack(padx=10, pady=10, fill="x") 
        
        theory_label = tk.Label(content_frame, text="The Arts Club provides a vibrant platform for creative expression, where members explore various artistic mediums such as painting, sculpting, and performing arts. ",font=("Arial", 13), wraplength=600, justify="left", anchor="w") 
        theory_label.pack(padx=10, pady=(0, 20), fill="x")
        events_label = tk.Label(content_frame, text="Through workshops, exhibitions, and collaborative projects, it fosters a community of artists who inspire and encourage each other's growth. Whether novice or seasoned, everyone finds a welcoming space to unleash their imagination and passion for the arts.",font=("Arial", 13), wraplength=600, justify="left", anchor="w")
        events_label.pack(padx=10, fill="x")  

        back_button = tk.Button(content_frame, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Secondpage))
        back_button.place(x=30, y=300)


if __name__ == "__main__":
    root = tk.Tk()
    second_page = Secondpage(root, None)
    second_page.pack(fill="both", expand=True)
    root.mainloop()
