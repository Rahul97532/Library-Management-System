##import pymysql

import MySQLdb
from datetime import *

def display_all_data():
    db=MySQLdb.connect(host='localhost',database='library',user='root',password='3131Rahul@Gupta')
    cursor=db.cursor()
    cursor.execute("select * from books order by book_id")
    data=cursor.fetchall()
##    print(data)
    db.close()
    return data
##display_all_data()


def add_book(l):
    
    db=MySQLdb.connect(host='localhost',database='library',user='root',password='3131Rahul@Gupta')
    cursor=db.cursor()
    cursor.execute("select max(Book_Id) from books")
    data=cursor.fetchone()
    id=data[0]+1

    l.insert(0,id)
    l=tuple(l)
    sql="Insert into books(Book_Id,Book_Name,Book_Author,genre,copies,available_copies,cost,language,rack_no,Publisher) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,l)
    db.commit()
    db.close()                                                                                                                                                                   


def remove_book(Id):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
    sql="Update books set Status=%s, copies=0, available_copies= 0 where Book_Id=%s"
    val=("Unavailable",Id)
    cursor.execute(sql,val)
    db.commit()
    db.close()     


def max_book_id_check(Id):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
    cursor.execute("Select max(Book_Id) from books")
    data=cursor.fetchone()
    if (int(data[0])<int(Id)):
        return "Id greater error"
    db.close()
def check_book_status(Id):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
    sql="Select Status from books where Book_Id=%s"
    val=(str(Id))
    cursor.execute(sql,val)
    data=cursor.fetchone()
    if data[0]=="Unavailable":
        return "Not available"
    db.close()
    
def update_book(Id,qty):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
    sql="Update books set copies=%s, available_copies=%s, status='Available' where Book_Id=%s"
    val=(qty,qty,Id)
    cursor.execute(sql,val)
    db.commit()
    db.close()
def book_availability_check(Id):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
    sql="Select available_copies from books where Book_Id=%s"
    val=(str(Id))
    cursor.execute(sql,val)
    data=cursor.fetchone()
    if data[0]==0:
        return "Not available"
    db.close()

def student_book_validity_check(r_no,Id):
    db=MySQLdb.connect(host='localhost',database='library',user='root',password='3131Rahul@Gupta')
    cursor=db.cursor()
    sql="Select count(*) from issue_record where Roll_No=%s"
    val=(str(r_no),)
    cursor.execute(sql,val)
    data=cursor.fetchone()
    if data[0]==3:
        return "overflow"
    sql="select count(*) from issue_record where Roll_no=%s and Book_Id=%s"
    val=(str(r_no),str(Id))
    cursor.execute(sql,val)
    data=cursor.fetchone()
    if data[0]==1:
        return "Duplicate request"
    db.close()
def issue_book(r_no,b_id):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
##    if book_availability_check(b_id):
##        return "NA"
##    if student_book_validity_check(r_no,b_id) =="overflow":
##        return "overflow"
##    if student_book_validity_check(r_no,b_id) =="Duplicate request":
##        return "Duplicate request"
##    if user_check(r_no):
##        return "Unknown User"
    sql="select * from users where Roll_No=%s"
##    sql="Select name from users where Roll_No=%s"
    val=(str(r_no),)
    cursor.execute(sql,val)
    user=cursor.fetchone()
    sql="Select * from books where Book_Id=%s"
    val=(str(b_id),)
    cursor.execute(sql,val)
    book=cursor.fetchone()

    idt,rdt=issue_return_date()
    sql="Insert into issue_record values(%s,%s,%s,%s)"
    val=(str(r_no),str(b_id),idt,rdt)
    cursor.execute(sql,val)
    cursor.execute("Update books set available_copies=available_copies-1 where Book_Id=%s", (str(b_id),) )
    db.commit()
    db.close()
    return (user,book,idt,rdt)

def issue_return_date():
    issue=date.today()
    ret=issue+timedelta(days=15)
    return(issue,ret)

##issue_book('20003','4')


def user_check(r_no):
    db=MySQLdb.connect(host='localhost',database='library',user='root',password='3131Rahul@Gupta')
    cursor=db.cursor()
    sql="Select count(*) from users where roll_no=%s"
    val=(str(r_no),)
    cursor.execute(sql,val)
    data=cursor.fetchone()
    db.close()
    if data[0]==0:
        return "Unknown User"

##print(issue_book(20005,10))
