class KockPit:

    def loginAdmin(self, passport, password):
        db = dbOperations()
        if db.loginAdmin(passport, password):
            self.controller.show_frame("Dashboard")
        else:
            tk.messagebox.showerror(title="Login Failed", message="Wrong Information")
