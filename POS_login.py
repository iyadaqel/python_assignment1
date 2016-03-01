from tkinter import *
import tkinter.messagebox as tm
'''
import vlc
def playsound () :
sound = vlc.MediaPlayer("file:////Users/begum/Documents/Bomboncito.mp3")
sound.play()
'''

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)
        if username == "iyad" and password == "password":
            tm.showinfo("Login info", "Welcome Iyad")
            sound.play()
        elif username == "carmen" and password == "password":
            tm.showinfo("Login info", "Welcome Carmen")
            sound.play()
        elif username == "monica" and password == "password":
            tm.showinfo("Login info", "Welcome Monica")
            sound.play()
        elif username == "begum" and password == "password":
            tm.showinfo("Login info", "Welcome Begum")
            sound.play()
        else:
            tm.showerror("Login error", "Invalid User!")




root = Tk()
root.title("Pythunicorns POS")
lf = LoginFrame(root)
root.mainloop()
