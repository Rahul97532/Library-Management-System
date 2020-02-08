##import pymysql

import MySQLdb


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

def issue_book(r_no,b_id):
    db=MySQLdb.connect(host="localhost",database="library",user="root",password="3131Rahul@Gupta")
    cursor=db.cursor()
    sql="select * from users where Roll_No=%s"
    val=(r_no)
    cursor.execute(sql,val)
    data=cursor.fetchone()
    db.commit()
    db.close()
    return data
