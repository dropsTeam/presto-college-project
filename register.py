from tkinter import*
from PIL import Image,ImageTk 
from dbOperations import dbOperations



class Register:

    def __init__(self,root):
        self.root=root
        self.root.title("REGISTER WINDOW")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.db = dbOperations()
        self.UI()

    def adminRegister(self):
            try:
                self.db.registerAdmin(self.txt_firstName+ self.txt_lastName, self.txt_passwordName, self.txt_address, self.txt_passportNo, self.txt_emailId, self.txt_contactName)    
            except NameError:
                    print(NameError)


    def UI(self):
        self.bg=ImageTk.PhotoImage(file="images/pexels-felix-mittermeier-956999.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0, relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/Navjot1.png")
        left=Label(self.root,image=self.left).place(x=80,y=100, width=400,height=500)

        frameOne=Frame(self.root, bg="white")
        frameOne.place(x=480,y=100,width=700,height=500)

        title=Label(frameOne, text="REGISTER HERE", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)
# --------------------------------------------------------------------
        firstName=Label(frameOne, text="First Name", font=("arial", 12),bg="white", fg="green").place(x=50, y=100)
        self.txt_firstName=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=50,y=130, width=250)

        lastName=Label(frameOne, text="Last Name", font=("arial", 12),bg="white", fg="green").place(x=370, y=100)
        self.txt_lastName=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=370,y=130, width=250)

# ------------------------------------------------------------------
        passportNo=Label(frameOne, text="Passport No", font=("arial", 12),bg="white", fg="green").place(x=50, y=170)
        self.txt_passportNo=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=50,y=200, width=250)

        address=Label(frameOne, text="Address", font=("arial", 12),bg="white", fg="green").place(x=370, y=170)
        self.txt_address=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=370,y=200, width=250)

# ------------------------------------------------------------------
        
        contactName=Label(frameOne, text="Mobile No", font=("arial", 12),bg="white", fg="green").place(x=50, y=240)
        self.txt_contactName=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=50,y=270, width=250)

        emailId=Label(frameOne, text="Email Id", font=("arial", 12),bg="white", fg="green").place(x=370, y=240)
        self.txt_emailId=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=370,y=270, width=250)

# ------------------------------------------------------------------
        passwordName=Label(frameOne, text="Password", font=("arial", 12),bg="white", fg="green").place(x=50, y=310)
        self.txt_passwordName=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=50,y=340, width=250)

        confirmName=Label(frameOne, text="Confirm Password", font=("arial", 12),bg="white", fg="green").place(x=370, y=310)
        self.txt_confirmName=Entry(frameOne, font=("arial",15),bg="whitesmoke").place(x=370,y=340, width=250)
# ------------------------------------------------------------------

        check=Checkbutton(frameOne,text="I Agree to the terms and conditon",onvalue=1,offvalue=0,bg="white",font=("arial",12)).place(x=50, y=380)


        btn_register=Button(frameOne, text="Register Now" ,font=("arial",20),bg="whitesmoke" ,bd=0,cursor="hand2").place(x=50,y=420)



root=Tk()
obj=Register(root)
root.mainloop()
