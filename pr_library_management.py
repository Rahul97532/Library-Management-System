import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import pr_database as lib
import pr_tk as rw
window=tk.Tk()
##window.geometry('1350x690+0+0')
window.attributes('-fullscreen',True)
window.configure(background="Light Blue")
window.title("Library Management System")

f1=tk.Frame(window)
l1=tk.Label(f1,text="COLLEGE  LIBRARY",font=" Times 30",width=500)
l1.pack(fill=tk.X,expand=True,side=tk.TOP)
f1.pack()

f2=tk.Frame(window)
lb1=tk.Label(f2,bg="Light Blue")
lb1.pack(fill=tk.X,expand=True,side=tk.TOP)
##l2=tk.Label(f2,text="User Details : ",font="Times 16")
##l2.pack(fill=tk.X,side=tk.TOP)

f2.pack()



class Rows:
    Row=0
    def cells(self,name1,name2,frame):
        Column=0
        lb1=tk.Label(frame,text=name1,font="Times 14",width=12,anchor=tk.W,bg="Light Blue")
        lb1.grid(row=self.Row,column=0)
        ent1=tk.Entry(frame,font="Times 14",width=30)
        ent1.grid(row=self.Row,column=1)


        blank=tk.Label(frame,width=12,bg="Light Blue")
        blank.grid(row=self.Row,column=2)
        
        lb2=tk.Label(frame,text=name2,font="Times 14",width=12,anchor=tk.W,bg="Light Blue")
        lb2.grid(row=self.Row,column=3)
        ent2=tk.Entry(frame,font="Times 14",width=30)
        ent2.grid(row=self.Row,column=4)

        self.Row+=1
        return [ent1,ent2]



def issue_book_button():
    roll_no=u_ent2[0].get()
    book_id=b_ent1[0].get()
    try:
        int(roll_no)
        int(book_id)
    except:
        messagebox.showerror("Error","Invalid information type entered")
        
    ans=lib.issue_book(roll_no,book_id)
    print(ans)
def return_book_button():
    pass

def display_book_button():
    tx1.delete(0,tk.END)
    data=lib.display_all_data()
##    print(len(data))
    for i in data:
        st=', '.join([str(x) for x in i])
        tx1.insert(tk.END,st)

def add_book_button():
    l=[]
    flag=0
    l.append(b_ent1[1].get())
    for i in range(2):
        l.append(b_ent2[i].get())
        l.append(b_ent3[i].get())
        l.append(b_ent4[i].get())
        l.append(b_ent5[i].get())
##        l.append(b_ent6[i].get())
    for i in l:
        if i=='':
            messagebox.showerror("Error","All values in the BOOK DETAILS section are compulasry.")
            flag=1
            break
    if flag==0:
        try:
            lib.add_book(l)
        except:
            messagebox.showerror("Error","An Error occured while Adding the Book")
        messagebox.showinfo("Message","Book Added Successfully")
         
def remove_book_button():
    rw.remove_book_window()

def search_book_button():
    pass

def update_book_button():
    rw.update_book_window()

def clear_button():
    for i in range(2):
        u_ent1[i].delete(0,len(u_ent1[i].get()))
        u_ent2[i].delete(0,len(u_ent2[i].get()))
        u_ent3[i].delete(0,len(u_ent3[i].get()))
        b_ent1[i].delete(0,len(b_ent1[i].get()))
        b_ent2[i].delete(0,len(b_ent2[i].get()))
        b_ent3[i].delete(0,len(b_ent3[i].get()))
        b_ent4[i].delete(0,len(b_ent4[i].get()))
        b_ent5[i].delete(0,len(b_ent5[i].get()))
        b_ent6[i].delete(0,len(b_ent6[i].get()))
        tx1.delete(0,tk.END)

        
f_details=tk.Frame(window,bg="Light Blue")

f_outer1=tk.Frame(f_details,bg="Light Blue")            

tk.Label(f_outer1,text="User Details",font="Times 24").pack(fill=tk.X,expand=True)
##tk.Label(f_outer1,bg="Light Blue").pack(fill=tk.X,expand=True)                  #Blank Label
f3=tk.Frame(f_outer1,bg="Light Blue")
a=Rows()
u_ent1=a.cells("Name","Course",f3)
u_ent2=a.cells("Roll No.","Phone Number",f3)
u_ent3=a.cells("Address","Fine Remaining",f3)

f3.pack()

##tk.Label(f_outer1,bg="Light Blue").pack(fill=tk.X,expand=True)

tk.Label(f_outer1,text="Book Details",font="Times 24").pack(fill=tk.X,expand=True)
##f4=tk.Frame(f_outer1)
##tk.Label(f4,text="Other Information").pack()
##f4.pack()
##tk.Label(f_outer1,bg="Light Blue").pack(fill=tk.X,expand=True)


f5=tk.Frame(f_outer1,bg="Light Blue")
b=Rows()
b_ent1=b.cells("Book Id","Book Name",f5)
b_ent2=b.cells("Author","Cost",f5)
b_ent3=b.cells("Genre","Language",f5)
b_ent4=b.cells("Total Copies","Rack No.",f5)
b_ent5=b.cells("Copies Left","Publisher",f5)
b_ent6=b.cells("Date of Issue","Date of Return",f5)
##b_ent1[0].config(state=tk.DISABLED)
b_ent6[0].config(state=tk.DISABLED)
b_ent6[1].config(state=tk.DISABLED)


f5.pack()




##tk.Label(f_outer1,bg="Light Blue",height=10).pack(fill=tk.X,expand=True)

f_outer1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)


f_outer2=tk.Frame(f_details)
lb=tk.Label(f_outer2,bg="Light Blue",width=2)
lb.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
sb_v=tk.Scrollbar(f_outer2,orient=tk.VERTICAL)
sb_v.pack(side=tk.RIGHT,fill=tk.Y)
sb_h=tk.Scrollbar(f_outer2,orient=tk.HORIZONTAL)
sb_h.pack(side=tk.BOTTOM,fill=tk.X)
tk.Label(f_outer2,text="Message Box",font="Times 24").pack(fill=tk.X,expand=True)
tx1=tk.Listbox(f_outer2,width=50,height=25,yscrollcommand=sb_v.set,xscrollcommand=sb_h.set)
tx1.pack(expand=True,fill=tk.BOTH)
sb_v.config(command=tx1.yview)
sb_h.config(command=tx1.xview)

f_outer2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

f_details.pack()

tk.Label(window,bg="Light Blue").pack(fill=tk.BOTH,expand=True)

f_outer3=tk.Frame(window)                                                                                   #Buttons Frame1
b1=tk.Button(f_outer3,text="Issue Book",font="Times 16",command=issue_book_button)
b1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
tk.Label(f_outer3,bg="Light Blue").pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
b2=tk.Button(f_outer3,text="Return Book",font="Times 16",command=return_book_button)
b2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
tk.Label(f_outer3,bg="Light Blue").pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
b3=tk.Button(f_outer3,text="Display Books",font="Times 16",command=display_book_button)
b3.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

f_outer3.pack(fill=tk.BOTH,expand=True)

tk.Label(window,bg="Light Blue").pack(fill=tk.BOTH,expand=True)

f_outer4=tk.Frame(window)                                                                                   #Buttons Frame2
b4=tk.Button(f_outer4,text="Add Book",font="Times 16",command=add_book_button)
b4.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
tk.Label(f_outer4,bg="Light Blue").pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
b5=tk.Button(f_outer4,text="Remove Book",font="Times 16",command=remove_book_button)
b5.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
tk.Label(f_outer4,bg="Light Blue").pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
b6=tk.Button(f_outer4,text="Search Book",font="Times 16",command=search_book_button)
b6.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

f_outer4.pack(fill=tk.BOTH,expand=True)


tk.Label(window,bg="Light Blue").pack(fill=tk.BOTH,expand=True)

f_outer5=tk.Frame(window)
b7=tk.Button(f_outer5,text="Update Books",font="Times 16",width=4,command=update_book_button)
b7.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
tk.Label(f_outer5,bg="Light Blue").pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
b8=tk.Button(f_outer5,text="Clear",font="Times 16",width=4,command=clear_button)
b8.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
tk.Label(f_outer5,bg="Light Blue").pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
b9=tk.Button(f_outer5,text="Exit",font="Times 16",width=4,command=window.destroy)
b9.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

f_outer5.pack(fill=tk.BOTH,expand=True)

window.mainloop()


##w=window.winfo_screenwindth()
##h=window.winfo_screenheight()
##print(f"{w}x{h}")
