import twilio.rest
import random
from future.moves import tkinter
from tkinter import messagebox

root =tkinter.TK()
root.title("OTP Verification")
root.geometry("600*550")

account_sid = ""
auth_token =""

def resendOTP():
    n = random.randint(1000,9999)
    client = twilio.rest.Client(account_sid, auth_token)
    client.mesages.create(to=[""],from_="",body=n)
def checkOTP():
    global n
    try:
        user_input = int(user.get(1.0,"end01c"))
        if user_input == n :
            messagebox.showinfo("showinfo","Login Success")
            n = "done"
        elif n == "done":
            messagebox.showinfo("showinfo","Login Success")
        else:
            messagebox.showinfo("showinfo","Invalid OTP")
    except:
        messagebox.showinfo("showinfo","Invalid OTP")
c = tkinter.Canvas(root, bg="white",width=400,height=300)
c.place(x=100,y=60)
login = tkinter.Label(root,text="OTP verification",font="bold,20",bg="white")
login.place(x=210,y=90)

user = tkinter.Text(root,borderwidth=2,wrap="word",width=29,height=2)
user.place(x=190,y=160)

n = random.randint(1000,9999)
client = twilio.rest.Client(account_sid, auth_token)
client.messages.create(to=[""],from_="",body=n)

/*submit button*/
submit = tkinter.Button(root,text="Submit",command=checkOTP,font=('bold',15))
submit.button.place(x=240,y=400)

root.mainloop()