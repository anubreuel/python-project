from  tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.font as font
import tkinter.tix as tkx
import sqlite3

class application:
    def __init__(self,parent):
        self.parent = parent
        self.ui_frame()
        self.ui_leftframe()

    def ui_frame(self):
        self.parent.title("company")
        self.parent.geometry("1350x800")
        self.parent.iconbitmap("wa.ico")
        self.f1=Frame(self.parent, height=800, width=1400, bg="steelblue")
        self.f1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.f1.place(x=0,y=0)
    

    def ui_home(self):

        self.f2.destroy()
        self.b_f.destroy()
        #self.b_edit.destroy()
        #self.b_search.destroy()
        

        

        self.photo21=ImageTk.PhotoImage(Image.open("new(3333).png"))
        self.b_home = Button(self.f1, text = "   Home ", font=("Rockwell",23,"normal"), fg="gold", image=self.photo21, compound=LEFT, bg="steelblue", activebackground="steel blue", relief=FLAT ,bd="0",cursor="plus" ,highlightcolor="gold",highlightbackground="gold",command=self.can_button )
        self.b_home.place(x=74,y=200)
        self.f2 =  Frame(self.parent, height=710, width=810, bg="steelblue" )
        #self.f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.f2.place(x=250 ,y=0)
        self.photo11=ImageTk.PhotoImage(Image.open("arrow.png"))
        self.arrow = Label(self.f2, text="", image=self.photo11, bg="steelblue")
        self.arrow.place(x=0,y=200)
        
        

    def ui_new(self):

        
        #--------------------------image--------------------------------------------
        self.photo11=ImageTk.PhotoImage(Image.open("arrow.png"))
        self.photo12=ImageTk.PhotoImage(Image.open("save.png"))
        self.photo13=ImageTk.PhotoImage(Image.open("cancel.png")) 
        self.photo20=ImageTk.PhotoImage(Image.open("new(111).png"))
        #-------------------------button frame--------------------------------------
        
        #button NEW
        self.b_f= Button(self.f1, text="  New ", font=("Rockwell",23,"normal"), fg="gold", image=self.photo20, compound=LEFT, bg="steelblue", activebackground="steelblue", relief=FLAT,bd="0", command=self.ui_new,cursor="plus")
        self.b_f.pack()
        self.b_f.place(x=74,y=270)
        #-----------------------LABELFRAME------------------------------------------
    
        self.f2 =  Frame(self.parent, height=700, width=800, bg="steelblue" )
        #self.f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.f2.place(x=250 ,y=0)
        #-------------------------button--------------------------------------------

        self.save_button = Button(self.f2, text = "   SAVE ", font=("Rockwell",10), fg="snow", image=self.photo12, compound=TOP, bg="steelblue", activebackground="steel blue", relief=FLAT ,bd="0"  )
        self.save_button.place(x=600,y=500)
        self.cancel_button = Button(self.f2, text = "   CANCEL ", font=("Rockwell",10), fg="snow", image=self.photo13, compound=TOP, bg="steelblue", activebackground="steel blue", relief=FLAT ,bd="0",command=self.can_button  )
        self
        self.cancel_button.place(x=700,y=500)
        #---------------------------------------------------------------------
        self.new_company = Label(self.f2, text="NEW COMPANY", fg="white",font=(" Helvetica",25,"bold"), bg="steel blue")
        self.new_company.place(x=250,y=50)
        #-------------------------------------------------------------
        self.arrow = Label(self.f2,text="",image=self.photo11,bg="steelblue")
        self.arrow.place(x=0,y=279)
        self.id = Label(self.f2, text="Id", fg="white",font=(" Helvetica",12,"bold"), bg="steel blue")
        self.id.place(x=175,y=125)
        self.id_entry = Entry(self.f2, width="22")
        self.id_entry.place(x=175,y=150)
        self.name = Label(self.f2, text="Name", fg="white", font=(" Helvetica",12,"bold"), bg="steel blue")
        self.name.place(x=175,y=180)
        self.name_entry = Entry(self.f2, width="22")
        self.name_entry.place(x=175,y=200)       
        self.contact_name = Label(self.f2, text="Contact Name", fg="white", font=(" Helvetica",12,"bold"), bg="steel blue")
        self.contact_name.place(x=400,y=180)
        self.contact_name_entry = Entry(self.f2, width="25")
        self.contact_name_entry.place(x=400,y=200)
        self.Address = LabelFrame(self.f2, text="Address", height=200, width=400, fg="white", font=(" Helvetica",12,"bold"), bg="steel blue")
        self.Address.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)#------ADDRESS-------------------
        self.Address.place(x=175,y=230)
        self.drno_st = Label(self.Address, text="Door number,Street", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.drno_st.place(x=10,y=0)
        self.drno_st_entry = Entry(self.Address,width="60")
        self.drno_st_entry.place(x=10,y=20)
        self.area = Label(self.Address, text="Area", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.area.place(x=10,y=50)
        self.area_entry = Entry(self.Address,width="60")
        self.area_entry.place(x=10,y=70)
        self.district = Label(self.Address, text="District", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.district.place(x=10,y=100)
        self.district_entry = Entry(self.Address,width="22")
        self.district_entry.place(x=10,y=120)
        self.pincode = Label(self.Address, text="Pincode", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.pincode.place(x=200,y=100)
        self.pincode = Entry(self.Address,width="22")
        self.pincode.place(x=200,y=120)
        self.contact_details = LabelFrame(self.f2, text="Contact Details", height=150, width=400, fg="white", font=(" Helvetica",12,"bold"), bg="steel blue")
        self.contact_details.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)#---------CONTACT DETAILS-----------
        self.contact_details.place(x=175,y=450)
        self.ph_1 = Label(self.contact_details, text="Phone number 1", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.ph_1.place(x=10,y=0)
        self.ph_1_entry = Entry(self.contact_details,width="22")
        self.ph_1_entry.place(x=10,y=20)
        self.ph_2 = Label(self.contact_details, text="Phone number 2", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.ph_2.place(x=200,y=0)
        self.ph_2_entry = Entry(self.contact_details,width="22")
        self.ph_2_entry.place(x=200,y=20)
        self.email_id = Label(self.contact_details, text="email id", fg="white", font=(" Helvetica",8,"bold"), bg="steel blue")
        self.email_id.place(x=10,y=50)
        self.email_id_entry = Entry(self.contact_details,width="60")
        self.email_id_entry.place(x=10,y=70)
        self.gst_no = Label(self.f2, text="GST Number", fg="white", font=(" Helvetica",12,"bold"), bg="steel blue")
        self.gst_no.place(x=175,y=610)
        self.gst_no_entry = Entry(self.f2, width="22")
        self.gst_no_entry.place(x=175,y=630)
        self.radio1_yes = Radiobutton(self.f2, text="Yes", variable=self.var, value=1,font=("Helvetica",13),cursor="hand2")
        self.var = IntVar(self.parent)
        self.radio1_yes.place(x=0,y=0)
        self.radio2_no = Radiobutton(self.f2, text="No", variable=self.var, value=0,font=("Helvetica",13),cursor="hand2",state="disabled").pack(side = TOP, ipady = 5)
        self.radio2_no.place(x=0,y=0)
        self.radio1_yes.select()
        # self.contact_name_entry = Entry(self.f2)
        # self.contact_name_entry.place(x=400,y=200)
    
    def ui_edit(self):
        self.f2.destroy()
        self.b_f.destroy()
        self.b_home.destroy()
        self.b_search.destroy()

        self.photo22=ImageTk.PhotoImage(Image.open("new(45).png"))
        self.b_edit = Button(self.f1, text = "   Edit ", font=("Rockwell",23,"normal"), fg="gold", image=self.photo22, compound=LEFT, bg="steelblue", activebackground="steel blue", relief=FLAT ,bd="0",cursor="plus" ,highlightcolor="gold",highlightbackground="gold",command=self.can_button )
        self.b_edit.place(x=74,y=340)
        self.f2 =  Frame(self.parent, height=700, width=800, bg="steelblue" )
        #self.f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.f2.place(x=250 ,y=0)
        self.photo11=ImageTk.PhotoImage(Image.open("arrow.png"))
        self.arrow = Label(self.f2,text="",image=self.photo11,bg="steelblue")
        self.arrow.place(x=0,y=350)
        
    
    def ui_search(self):
        self.f2.destroy()
        self.b_f.destroy()
        self.b_home.destroy()
        #self.b_edit.destroy()

        self.photo23 =ImageTk.PhotoImage(Image.open("new(222).png"))
        self.b_search = Button(self.f1, text = " Search ", font=("Rockwell",23,"normal"), fg="gold", image=self.photo23, compound=LEFT, bg="steelblue", activebackground="steel blue", relief=FLAT ,bd="0",cursor="plus" ,highlightcolor="gold",highlightbackground="gold",command=self.can_button )
        self.b_search.place(x=74,y=415)
        self.f2 =  Frame(self.parent, height=700, width=800, bg="steelblue" )
        #self.f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.f2.place(x=250 ,y=0)
        self.arrow = Label(self.f2,text="",image=self.photo11,bg="steelblue")
        self.arrow.place(x=0,y=425)    
    
    def ui_leftframe(self):
        #IMAGES
        self.photo=ImageTk.PhotoImage(Image.open("res.png"))
        self.photo1=ImageTk.PhotoImage(Image.open("redbutton.png"))
        self.photo3=ImageTk.PhotoImage(Image.open("new(22).png"))
        self.photo4=ImageTk.PhotoImage(Image.open("new(333).png"))
        self.photo6=ImageTk.PhotoImage(Image.open("new(55).png"))
        self.photo7=ImageTk.PhotoImage(Image.open("new.png"))
        self.photo5=ImageTk.PhotoImage(Image.open("newp(444).png"))
        self.photo2=ImageTk.PhotoImage(Image.open("logooo.png"))
     
        
        #BUTTONS

        #button home
        self.b1 = Button(self.f1, text = "   Home ", font=("Rockwell",20,"normal"), fg="snow", image=self.photo4, compound=LEFT, bg="steelblue", activebackground="steel blue", relief=FLAT ,bd="0",cursor="plus" ,highlightcolor="gold",highlightbackground="gold",command=self.ui_home )
        self.b1.place(x=75,y=200)
        
        #button NEW
        self.b2= Button(self.f1, text="   New ", font=("Rockwell",20,"normal"), fg="SNOW", image=self.photo5, compound=LEFT, bg="steelblue", activebackground="steel blue", relief=FLAT,bd="0", command=self.ui_new,cursor="circle")
        self.b2.pack()
        self.b2.place(x=75,y=275)
        #Button Edit
        self.b3 = Button(self.f1, text="   Edit ", font=("Rockwell",20), fg="SNOW", image=self.photo7, compound=LEFT,bg="steelblue", activebackground="steel blue",relief=FLAT,bd="0",cursor="hand1",command=self.ui_edit)
        self.b3.place(x=75,y=350)
        #Button search
        self.b4 = Button(self.f1, text="   Search ", font=("Rockwell",20), fg="SNOW",image=self.photo3, compound=LEFT,bg="steelblue", activebackground="steel blue",relief=FLAT,bd="0",cursor="man",command=self.ui_search )
        self.b4.place(x=75,y=425)
        #Button delete
        self.b5 = Button(self.f1, text="   Delete ", font=("Rockwell",20), fg="SNOW",image=self.photo6, compound=LEFT,bg="steelblue", activebackground="steel blue",relief=FLAT ,bd="0",cursor="boat")
        self.b5.place(x=75,y=500)
        #logo label
        self.logo_label = Label(self.f1,text="",image=self.photo2,bg="steelblue")
        self.logo_label.place(x=1200,y=20)
    def can_button(self):
        self.f2.destroy()
        self.b_f.destroy()
        self.b_home.destroy()
        self.b_edit.destroy()
        self.b_search.destroy()

        
root = Tk()
app = application(root)
mainloop()

