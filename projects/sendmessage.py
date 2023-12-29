import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def sendsms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params={
        "authorization":"WRCseMupKNElJvX5BVk2jQUcnaGwqtdyDifImYghz84SPbA70F71CbuNPVxW5OiosYlcpg2ShnR4fHjQ",
        "sender_id":"TXTIND",
        "message":message,
        "language":"english",
        "route":"v3",
        "numbers":number

    }
    response=requests.get(url,params=params)
    a=response.json()
    #print(a)
    return a.get("return")







def btnclick():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r = sendsms(num,msg)
    if r:
        showinfo("send success","successfully send")
    else:
        showerror("Error","something went wrong")








#creating gui
root = Tk()
root.title("message sender")  #container's title
root.geometry("400x550")       #container's len and brea
font = ("Helvetica", 22, "bold")
textNumber=Entry(root,font=font)
textNumber.pack(fill=X,pady=20) 
textMsg=Text(root)
textMsg.pack(fill=X,pady=10)
sendBtn=Button(root,text="SEND MESSAGE",command=btnclick)
sendBtn.pack()







root.mainloop()


