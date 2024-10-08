from tkinter import *
from PIL import Image, ImageTk
from course import courseclass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # ===icons===
        self.logo_dash = ImageTk.PhotoImage(file="images/download.jpeg")
        
        # ===title===
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)
        
        # ===menu===
        M_Frame = LabelFrame(self.root, text="Menus", font=("Times New Roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)
        
        # ===buttons===
        btn_course = Button(M_Frame, text="Course", font=("Goudy Old Style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=("Goudy Old Style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_student.place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("Goudy Old Style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_result.place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Student Result", font=("Goudy Old Style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_view.place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("Goudy Old Style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_logout.place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("Goudy Old Style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=root.quit)
        btn_exit.place(x=1120, y=5, width=200, height=40)

        # Load and resize the image
        self.bg_img = Image.open("images/bg.png").resize((920, 350))
        self.bg_img_Tk = ImageTk.PhotoImage(self.bg_img)
        
        # Create and place the label for background image
        self.lbl_bg = Label(self.root, image=self.bg_img_Tk)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        # === Update Details ===
        self.lbl_course = Label(self.root, text="Total Course\n[0]", font=("Goudy Old Style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)              
        self.lbl_student = Label(self.root, text="Total Students\n[0]", font=("Goudy Old Style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)  
        self.lbl_result = Label(self.root, text="Total Results\n[0]", font=("Goudy Old Style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)                          

        # === Footer ===
        footer = Label(self.root, text="SRMS - Student Result Management System\nContact us for any technical issues: 987xxxx01", font=("Goudy Old Style", 12), bg="#033054", fg="white", anchor="center")
        footer.pack(side=BOTTOM, fill=X, padx=10, pady=10)
        
    def add_course(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = courseclass(self.new_win) 

# Main execution
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()