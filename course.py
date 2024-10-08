from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk,messagebox
import sqlite3
class courseclass :
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")  
        self.root.config(bg="white")
        self.root.focus_force()


# ===title===
        title = Label(self.root, text="manage course details", 
                      font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)
        
#=====variable====
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        
        
        
        
        
###===widgets===
        lbl_courseName=Label(self.root,text="course Name",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,'bold'),bg="white").place(x=10,y= 100  )
        lbl_charges=Label(self.root,text="charges",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=180) 
  
  #====entryfields=====
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.txt_courseName.place(x=150,y=60,width=200)
        
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,'bold'),bg="lightyellow").place(x=150,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,'bold'),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=500,height=130)
        
#===buttons===
        self.btn_add=Button(self.root,text='save',font=("goudt old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='update',font=("goudt old style",15,"bold"),bg="green",fg="white",cursor="hand2")
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='delete',font=("goudt old style",15,"bold"),bg="red",fg="white",cursor="hand2")
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='clear',font=("goudt old style",15,"bold"),bg="blue",fg="white",cursor="hand2")
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        
#====search panel====
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text=" course name",font=("goudy old style",15,'bold'),bg="white").place(x=720,y=60)
        
        txt_search_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.txt_courseName.place(x=870,y=60,width=180)
        
        btn_search=Button(self.root,text='search',font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2").place(x=1070,y=60,width=120,height=28)
        
#===conent=====


        self.c_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_Frame.place(x=720,y=100,width=470,height=340)
        
        scrolly=Scrollbar(self.c_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_Frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.c_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)
        
        self.courseTable.heading("cid",text="course ID")
        self.courseTable.heading("name",text="name")
        self.courseTable.heading("duration",text="duration")
        self.courseTable.heading("charges",text="charges")
        self.courseTable.heading("description",text="description")
        self.courseTable["show"]="headings"
        self.courseTable.column("cid",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("duration",width=100)
        self.courseTable.column("charges",width=100)
        self.courseTable.column("description",width=150)
        self.courseTable.pack(fill=BOTH,expand=1)
        
        #========================================================
def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                    messagebox.showerror("Error","course name should be required",parent=self.root)
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","course name a")    
            else:
                 cur.execute("select* from course where name=?",(self.var_course.get(),))   
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        
        
        
        
        
if __name__=="__main__":
        root=Tk()
        obj=courseclass(root)
        root.mainloop()