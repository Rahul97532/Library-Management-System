import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import pr_database as lib 


def remove_book_window():
    rem_win=tk.Toplevel()
    rem_win.lift()
    rem_win.attributes('-topmost',True)
    rem_win.focus_force()
    rem_win.title("Remove Book")
    rem_win.geometry('900x300+300+100')
    rem_win.configure(background="Light Blue")
    rem_f1=tk.Frame(rem_win,bg="Red")

    img=Image.open(r"C:\Users\hp\Desktop\images.gif")
    img=img.resize((250,250),Image.ANTIALIAS)
    p1=ImageTk.PhotoImage(img)
    ##p1=PhotoImage(file=r"C:\Users\hp\Desktop\remove.png")


    def remove_button_clicked():
        Id=rem_e1.get()
        try:
            a=int(Id)
        except:
            messagebox.showerror("Error","Please enter correct Book Id")
            return
        ans=lib.max_book_id_check(Id)
        if ans=="Id greater error":
            messagebox.showerror("Error","Please enter valid Book Id")
            return
        ans=lib.check_book_status(Id)
        if ans=="Not available":
            messagebox.showerror("Error"," Book donot exist in Library")
            return
        ans=lib.remove_book(Id)
        messagebox.showinfo("Remove Book","Book removed sucessfull!!!")

    def clear_button_clicked():
        rem_e1.delete(0,len(rem_e1.get()))


    ##logo=tk.PhotoImage(file=r"C:\Users\hp\Desktop\images.gif")
    tk.Label(rem_f1,image=p1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    rem_f1.pack(side=tk.LEFT)
    rem_f2=tk.Frame(rem_win,bg="Light Blue")
    rem_if1=tk.Frame(rem_f2,bg="Light Blue")
    tk.Label(rem_if1,bg="Light Blue",width=20).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    tk.Label(rem_if1,text="Book_Id",background="Light Blue",font="Times 20 bold").pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    tk.Label(rem_if1,bg="Light Blue",width=20).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    rem_e1=tk.Entry(rem_if1,font="Times 18")
    rem_e1.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    rem_if1.pack()
    rem_if2=tk.Frame(rem_f2,bg="Light Blue")
    tk.Label(rem_if2,bg="Light Blue",width=20,height=5).pack(fill=tk.BOTH,expand=True)
    ##tk.Label(rem_if2,bg="Light Blue",width=20).pack()
    ##tk.Label(rem_if2,bg="Light Blue",width=20).pack()
    tk.Label(rem_if2,bg="Light Blue",width=4).pack(side=tk.LEFT)
    rem_b1=tk.Button(rem_if2,text="Remove",width=20,font="Times 16",command=remove_button_clicked)
    rem_b1.pack(side=tk.LEFT)
    tk.Label(rem_if2,bg="Light Blue",width=4).pack(side=tk.LEFT)
    rem_b2=tk.Button(rem_if2,text="Clear",width=20,font="Times 16",command=clear_button_clicked)
    rem_b2.pack(side=tk.LEFT)
    rem_if2.pack()
    rem_if3=tk.Frame(rem_f2,bg="Light Blue")
    tk.Label(rem_if3,bg="Light Blue").pack()
    rem_b3=tk.Button(rem_if3,text="Exit",font="Times 16",width=20,command=rem_win.destroy)
    rem_b3.pack()
    rem_if3.pack()
    rem_f2.pack(side=tk.LEFT)
    rem_win.mainloop()


def update_book_window():
    upd_win=tk.Toplevel()
    upd_win.focus_force()
    upd_win.title("Update Books")
    upd_win.geometry("700x300+200+100")

    def update_button_clicked():
        Id=upd_e1.get()
        qty=upd_e2.get()
        try:
            a=int(Id)
            b=int(qty)
        except:
            messagebox.showerror("Error","Incorrect Book Id or Quantity type entered")
            return
        ans=lib.max_book_id_check(Id)
        if ans=="Id greater error":
            messagebox.showerror("Error","Incorrect Book Id entered")
##        try:
##            lib.update_book(Id,qty)
##        except:
##            messagebox.showerror("Error","Something went wrong while processing the Task")
##            return
        lib.update_book(Id,qty)
        messagebox.showinfo("Message","Book Updated Successfully")
    def clear_button_clicked():
        upd_e1.delete(0,len(upd_e1.get()))
        upd_e2.delete(0,len(upd_e2.get()))
    
    upd_f1=tk.Frame(upd_win,bg="Light Blue")
    upd_if1=tk.Frame(upd_f1)
    tk.Label(upd_if1,text="You Can update only the quantity of the books!!!",bg="Purple1",font="Helvetica 20 bold").pack(fill=tk.X,expand=True)
    upd_if1.pack(fill=tk.X)
    upd_if2=tk.Frame(upd_f1,bg="Light Blue")
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",height=3).grid(row=0,column=0)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",width=10).grid(row=0,column=0)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",text="Book Id").grid(row=0,column=1)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",width=10).grid(row=0,column=2)
    upd_e1=tk.Entry(upd_if2,width=10,font="Times 16 bold")
    upd_e1.grid(row=0,column=3)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",height=3).grid(row=1,column=0)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",width=10).grid(row=1,column=0)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",text="Updated Book Qty").grid(row=1,column=1)
    tk.Label(upd_if2,bg="Light Blue",font="Times 16 bold",width=10).grid(row=1,column=2)
    upd_e2=tk.Entry(upd_if2,width=10,font="Times 16 bold")
    upd_e2.grid(row=1,column=3)
    upd_if2.pack(fill=tk.X)
    upd_if3=tk.Frame(upd_f1,bg="Light Blue")
    upd_b1=tk.Button(upd_if3,text="Update",width=15,font="Ariel 16",command=update_button_clicked)
    upd_b1.pack(fill=tk.X,side=tk.LEFT)
    tk.Label(upd_if3,bg="Light Blue").pack(side=tk.LEFT,fill=tk.X)
    upd_b2=tk.Button(upd_if3,text="Clear",width=15,font="Ariel 16",command=clear_button_clicked)
    upd_b2.pack(side=tk.LEFT,expand=True)
    tk.Label(upd_if3,bg="Light Blue").pack(side=tk.LEFT,fill=tk.X)
    upd_b2=tk.Button(upd_if3,text="Exit",width=15,font="Ariel 16",command=upd_win.destroy)
    upd_b2.pack(side=tk.LEFT,expand=True)
    upd_if3.pack(fill=tk.X)
    upd_f1.pack(fill=tk.BOTH,expand=True)
    upd_win.mainloop()
