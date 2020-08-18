try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont
    from tkinter import*
    import tkinter.messagebox
    from PIL import Image,ImageTk 
    from dbOperations import dbOperations
  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, UserRegister, AdminUser, Dashboard, LoginPage, EditAdmin, EditUser):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()





class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.geometry("1350x700")
        label = tk.Label(self, text="dis is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        
        button6 = tk.Button(self, text="Login Here",
                            command=lambda: controller.show_frame("LoginPage"))
        button6.pack()


class UserRegister(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def createUser(userName, address, balance, passportNumber, email, contact):
                db = dbOperations()
                try:
                        db.addUser(userName, address, balance, passportNumber, email, contact)
                        tkinter.messagebox.showinfo('Success', 'Successfully created')
                        controller.show_frame('Dashboard')
                except Exception as ex:
                        tkinter.messagebox.showerror(title="Adding Failed", message= str(ex) )



        self.bg=ImageTk.PhotoImage(file="images/pexels-felix-mittermeier-956999.jpg")
        bg=Label(self,image=self.bg).place(x=0,y=0, relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/Navjot1.png")
        left=Label(self,image=self.left).place(x=80,y=100, width=400,height=500)

        self=Frame(self, bg="white")
        self.place(x=480,y=100,width=700,height=500)

        title=Label(self, text="REGISTER HERE", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)

# ------------111111111111111111-------------------------------------------------------
        
        firstName=Label(self, text="First Name", font=("arial", 12),bg="white", fg="green").place(x=50, y=100)
        txt_firstName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_firstName.place(x=50,y=130, width=250)

        lastName=Label(self, text="Last Name", font=("arial", 12),bg="white", fg="green").place(x=370, y=100)
        txt_lastName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_lastName.place(x=370,y=130, width=250)

# ------------222222222222222222222------------------------------------------------------
        passportNo=Label(self, text="Passport No", font=("arial", 12),bg="white", fg="green").place(x=50, y=170)
        txt_passportNo=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_passportNo.place(x=50,y=200, width=250)

        address=Label(self, text="Address", font=("arial", 12),bg="white", fg="green").place(x=370, y=170)
        txt_address=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_address.place(x=370,y=200, width=250)

# -------------333333333333333333333-----------------------------------------------------
        
        contactName=Label(self, text="Mobile No", font=("arial", 12),bg="white", fg="green").place(x=50, y=240)
        txt_contactName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_contactName.place(x=50,y=270, width=250)

        emailId=Label(self, text="Email Id", font=("arial", 12),bg="white", fg="green").place(x=370, y=240)
        txt_emailId=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_emailId.place(x=370,y=270, width=250)

# # -------------44444444444444444444444-----------------------------------------------------
#         passwordName=Label(self, text="Password", font=("arial", 12),bg="white", fg="green").place(x=50, y=310)
#         self.txt_passwordName=Entry(self, font=("arial",15),bg="whitesmoke").place(x=50,y=340, width=250)

#         confirmName=Label(self, text="Confirm Password", font=("arial", 12),bg="white", fg="green").place(x=370, y=310)
#         self.txt_confirmName=Entry(self, font=("arial",15),bg="whitesmoke").place(x=370,y=340, width=250)

        
        check=Checkbutton(self,text="I Agree to the terms and conditon",onvalue=1,offvalue=0,bg="white",font=("arial",12)).place(x=50, y=380)

        btn_register=Button(self, text="Register Now" ,font=("arial",20),bg="whitesmoke", command= lambda: createUser(txt_firstName.get() + ' ' + txt_lastName.get() , txt_address.get(), 0, txt_passportNo.get(), txt_emailId.get(), txt_contactName.get()) ,bd=0,cursor="hand2" ).place(x=50,y=420)
        # button3 = tk.Button(self, text="Register Now" ,font=("arial",20),bg="whitesmoke" ,bd=0,cursor="hand2",command=lambda: controller.show_frame("Dashboard")).place(x=50,y=420)
        button4 = tk.Button(self, text="Go to Dashboard",
                            command= lambda: controller.show_frame('Dashboard') )
        # button = tk.Button(self, text="Register Now",
        #                     command=lambda: controller.show_frame("Dashboard"))
        button4.pack()
        # button.pack()
        


class AdminUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        def createUser(userName, password, address, passportNumber, email, contact):
                db = dbOperations()
                try:
                        db.registerAdmin(userName, address, balance, passportNumber, email, contact)
                        tkinter.messagebox.showinfo('Success', 'Successfully created an Admin')
                        controller.show_frame('Dashboard')
                except Exception as ex:
                        tkinter.messagebox.showerror(title="Adding Failed", message= str(ex) )


        self.bg=ImageTk.PhotoImage(file="images/pexels-felix-mittermeier-956999.jpg")
        bg=Label(self,image=self.bg).place(x=0,y=0, relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/Navjot1.png")
        left=Label(self,image=self.left).place(x=80,y=100, width=400,height=500)

        self=Frame(self, bg="white")
        self.place(x=480,y=100,width=700,height=500)

        title=Label(self, text="REGISTER HERE", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)

# ------------111111111111111111-------------------------------------------------------
        
        firstName=Label(self, text="First Name", font=("arial", 12),bg="white", fg="green").place(x=50, y=100)
        txt_firstName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_firstName.place(x=50,y=130, width=250)

        lastName=Label(self, text="Last Name", font=("arial", 12),bg="white", fg="green").place(x=370, y=100)
        txt_lastName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_lastName.place(x=370,y=130, width=250)

# ------------222222222222222222222------------------------------------------------------
        passportNo=Label(self, text="Passport No", font=("arial", 12),bg="white", fg="green").place(x=50, y=170)
        txt_passportNo=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_passportNo.place(x=50,y=200, width=250)

        address=Label(self, text="Address", font=("arial", 12),bg="white", fg="green").place(x=370, y=170)
        txt_address=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_address.place(x=370,y=200, width=250)

# -------------333333333333333333333-----------------------------------------------------
        
        contactName=Label(self, text="Mobile No", font=("arial", 12),bg="white", fg="green").place(x=50, y=240)
        txt_contactName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_contactName.place(x=50,y=270, width=250)

        emailId=Label(self, text="Email Id", font=("arial", 12),bg="white", fg="green").place(x=370, y=240)
        txt_emailId=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_emailId.place(x=370,y=270, width=250)

# -------------44444444444444444444444-----------------------------------------------------
        passwordName=Label(self, text="Password", font=("arial", 12),bg="white", fg="green").place(x=50, y=310)
        txt_passwordName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_passwordName.place(x=50,y=340, width=250)

        confirmName=Label(self, text="Confirm Password", font=("arial", 12),bg="white", fg="green").place(x=370, y=310)
        txt_confirmName=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_confirmName.place(x=370,y=340, width=250)


        check=Checkbutton(self,text="I Agree to the terms and conditon",onvalue=1,offvalue=0,bg="white",font=("arial",12)).place(x=50, y=380)

        btn_register=Button(self, text="Register Now" ,font=("arial",20),bg="whitesmoke" , command= lambda: createUser( txt_firstName.get() + ' ' + txt_lastName.get(), txt_passwordName.get(), txt_address.get(), txt_passportNo.get() , txt_emailId.get() , txt_contactName.get()), bd=0,cursor="hand2" ).place(x=50,y=420)

        button = tk.Button(self, text="Go to Dashboard",
                           command=lambda: controller.show_frame("Dashboard"))
        button.pack()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
       
        
        tk.Frame.__init__(self, parent)
        


        
        def loginAdmin( passport, password):
            db = dbOperations()
            if db.loginAdmin(passport, password):
                controller.show_frame("Dashboard")
            else:
                tkinter.messagebox.showerror(title="Login Failed", message="Wrong Information, try with correct passport and password")


        self.bg=ImageTk.PhotoImage(file="images/pexels-felix-mittermeier-956999.jpg")
        bg=Label(self,image=self.bg).place(x=0,y=0, relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/Navjot1.png")
        left=Label(self,image=self.left).place(x=80,y=100, width=400,height=500)

        self=Frame(self, bg="white")
        self.place(x=480,y=100,width=700,height=500)

        title=Label(self, text="LOGIN HERE", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)

        passportNo=Label(self, text="Passport No", font=("arial", 12),bg="white", fg="green").place(x=50, y=170)
        txt_passportNo=Entry(self, font=("arial",15),bg="whitesmoke")
        txt_passportNo.place(x=50,y=200, width=250)

        passwordName=Label(self, text="Password", font=("arial", 12),bg="white", fg="green").place(x=50, y=310)
        txt_passwordName= Entry(self, font=("arial",15),bg="whitesmoke")
        txt_passwordName.place(x=50,y=340, width=250)


        button = tk.Button(self, text="Login Now", command= lambda: loginAdmin( txt_passportNo.get() , txt_passwordName.get())  )
        button.pack()
        
        


        
        
       

class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        db = dbOperations()

        title=Label(self, text="PROFILE VIEW", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)

        title=Label(self, text="USER LIST", font=("caliber heading", 10,),bg="white", fg="green").place(x=50, y=80)

        listbox = Listbox(self)
        listbox.place(x=50,y=110, width=400, height=150) 
        scrollbar = Scrollbar(self) 
        scrollbar.place(x=520,y=110,height=150)  
        
        allAdmin = db.getAllAdmin()
        allUser = db.getAllUsers()
        
        i = 0
        for values in allUser: 
                i+=1
                listbox.insert(END, str(i) + ' ( name ) ' + values["userName"] + '  ( Address ) ' + values["address"] + '   ( Passport )  '+ values["passportNumber"] + '   ( Amount )   $'  + str(values["balance"]) ) 
        listbox.config(yscrollcommand = scrollbar.set) 
        scrollbar.config(command = listbox.yview) 

        title=Label(self, text="ADMIN LIST", font=("caliber heading", 10,),bg="white", fg="green").place(x=50, y=270)

        listbox1 = Listbox(self)
        listbox1.place(x=50,y=290, width=400, height=150) 
        scrollbar = Scrollbar(self) 
        scrollbar.place(x=520,y=290,height=150)  

        for values in range(20): 
                listbox1.insert(END, values) 

        listbox1.config(yscrollcommand = scrollbar.set) 
        scrollbar.config(command = listbox1.yview) 

        button08 = tk.Button(self, text="go to home page",
                            command=lambda: controller.show_frame("HomePage"))
        button08.pack()

        btn_addAdmin = tk.Button(self, text="Add Admin",
                            command=lambda: controller.show_frame("AdminUser") ,font=("arial",12),bg="whitesmoke" ,bd=0,cursor="hand2", width=10, height=1 ).place(x=560,y=120)

        btn_addUser = tk.Button(self, text="Add User",command=lambda: controller.show_frame("UserRegister") ,font=("arial",12),bg="whitesmoke" ,bd=0,cursor="hand2", width=10, height=1).place(x=560,y=170)
        
        btn_editUser = tk.Button(self, text="Edit User",command=lambda: controller.show_frame("EditUser") ,font=("arial",12),bg="whitesmoke" ,bd=0,cursor="hand2", width=10, height=1).place(x=560,y=300)
        
        btn_editAdmin = tk.Button(self, text="Edit Admin",command=lambda: controller.show_frame("EditAdmin") ,font=("arial",12),bg="whitesmoke" ,bd=0,cursor="hand2", width=10, height=1).place(x=560,y=370)


class EditUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title=Label(self, text="EDIT USER PROFILE", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)

        title=Label(self, text="USER DATA", font=("caliber heading", 10,),bg="white", fg="green").place(x=50, y=80)

        button = tk.Button(self, text="Go to Dashboard",
                           command=lambda: controller.show_frame("Dashboard"))
        button.pack()

        
class EditAdmin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        title=Label(self, text="EDIT ADMIN PROFILE", font=("caliber heading", 16,),bg="white", fg="red").place(x=50, y=30)

        title=Label(self, text="ADMIN DATA", font=("caliber heading", 10,),bg="white", fg="green").place(x=50, y=80)


        button = tk.Button(self, text="Go to Dashboard",
                           command=lambda: controller.show_frame("Dashboard"))
        button.pack()





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()