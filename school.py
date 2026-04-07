import pymysql
import time

con = pymysql.connect(host="localhost", user="root", password="maoji@123", database='sm')
cu = con.cursor()

print("""------------------------------------------------------------------------------------------------------------------------
                                                SCHOOL MANAGEMENT SYSTEM
------------------------------------------------------------------------------------------------------------------------""")
def check_ele(d, a):
    cu.execute(f"SELECT * FROM {d} WHERE Admin_no={a}")
    b = cu.fetchall()
    c = cu.rowcount
    return c
def add_student():
    print("-----------------------------------------------------ADD NEW STUDENT----------------------------------------------------")
    while True:
            admn = input("Admin_no --> ")
            c = "student"
            ck = check_ele(c, admn)
            if ck>=1:
                print(f"Admin_no {admn} already exist!")
                continue
            a = len(admn)
            b = admn.isdigit()
            if b==True and a >= 3 :
                break
            else:
                print("Admin_no should be numeric and minimun 3 digit")

    while True:
        Name = input("Name [Limit = 60] --> ")
        name = Name.title()
        n = len(name)
        if n <= 60:
            break
        else:
            print("Name should not excess 60 words!")

    while True:
        cl = input("Class--> ") 
        c = len(cl)
        d = cl.isdigit()
        if  d==True and c <= 2 and int(cl)>=6 and int(cl)<=12:
            break
        else:
            print("Class should be between 6 to 12")
    while True:
        gender = input("Gender(M/F) --> ")
        gen = gender.capitalize()
        g = gen.isalpha()
        e = len(gen)
        if g==True and e==1 and (gen == "M" or gen == "F"):
            break
        else:
            print("M for male & F for female")
    while True:
        father = input("Father name --> ")
        father = father.title()
        a = len(father)
        if a <=60:
            break
        else:
            print("Name word limit is 30")
    
    while True:
        mother = input("Mother\'s name --> ")
        mother = mother.title()
        a = len(mother)
        if a <=60:
            break
        else:
            print("Name word limit is 30")
    while True:
        contact = input("Contact no.--> ")
        c = len(contact)
        d = contact.isdigit()
        if c == 10 and d == True:
            break
        else:
            print("Contact no must be numeric and of 10 characters.")
    print("DOB")

    #month
    while True:
        m = input("MM-->")
        try:
            a = m.isdigit()
        except:
            print("Month should be digit!")
            continue
        if a==True and int(m)>=1 and int(m)<=12:
            break
        else:
            print("Month should be between 01 to 12!")
    if len(m)<2:
        m = f"0{m}"

    #year
    while True:
        y = input("YYYY-->")
        try:
            a = int(y)
        except:
            print("Enter data properly!")
            continue
        if len(y)!=4:
            print("Enter data properly!")
        else: break
        


    # date
    while True:
        d = input("DD-->")
        try:
            a = int(d)
        except:
            print("Date should be numeric")
            continue
        if(m == "01" or m == "03" or m == "05" or m == "07" or m == "08" or m == "10" or m == "12") and (int(d)>31 or int(d)<1):
             print("Date should be between 01 to 31")
             continue
        elif m == "02" and (int(y)%4 == 1) and d >= "30":
            print("Leap year!") 
            continue
        elif m== "02" and (int(y)%4 != 1) and d >= "29":
            print("Date should be less then 29!")
            continue
        elif (m=="04" or m=="06" or m=="09" or m=="11") and int(d)>30:
            print("Date should be between 01 to 30!")
        else:
            break
    dob = "{:04d}-{:02d}-{:02d}".format(int(y), int(m), int(d))
    query = ("INSERT INTO student (Admin_no, Name, Gender, Class, Father_name, Mother_name, Contact_no, DOB) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (admn, name, gen, cl, father, mother, contact, dob)
    cu.execute(query, data)
    con.commit() 
    time.sleep(2)
    print("New student added successfully!")

def search_student():
    print("\n--------------------------------SEARCH STUDENT----------------------------------\n")
    while True:
        a = input("Enter Admin_no:--> ")
        c = "student"
        ck = check_ele(c, a)
        if ck==1:
            break
        else:
            print(f"Admin_no {a} does not exist!")
            continue
        try:
            c= int(a)
        except:
            print("Admin_no should be numeric!")
            continue
        if(len(a)==3):
            break
        else:
            print("Admin_no should be 3-digit")
    b = (f"SELECT * FROM student WHERE Admin_no ={a}")
    cu.execute(b)
    time.sleep(2)
    print("\n")
    for i in cu:
        print(i)
    mod = input("Want to modify?(y/N)")
    print("\n")
    if mod.lower()=="y":
        while True:
                field = input("""           Data you want to change: 
                            1. Name         2. DOB
                            3. Gender       4. Class
                            5. Father_name  6. Mother_name
                            7. Contact_no   0. Exit
                            -->  """)
                try:
                    a=int(field)
                except:
                    print("Enter Valid option")
                if field=="1":
                    while True:
                        name =  input("Enter name[Limit = 30]--> ")
                        name = name.title()
                        if len(name)<=30:
                            break
                        else:
                            print("Name should not exceed 30 letters!")
                            continue
                    cu.execute(f"UPDATE student SET Name='{name}' WHERE Admin_no={i[0]}")
                    con.commit()
                    print("Successfully modified...")
                    
                elif field == "2":
                    while True:
                        m = input("MM-->")
                        try:
                            a = m.isdigit()
                        except:
                            print("Month should be digit!")
                            continue
                        if a==True and int(m)>=1 and int(m)<=12:
                            break
                        else:
                            print("Month should be between 01 to 12!")
                    if len(m)<2:
                        m = f"0{m}"

            #year
                    while True:
                        y = input("YYYY-->")
                        try:
                            a = int(y)
                        except:
                            print("Enter data properly!")
                            continue
                        if len(y)!=4:
                            print("Enter data properly!")
                        else: break
                


            # date
                    while True:
                        d = input("DD-->")
                        try:
                            a = int(d)
                        except:
                            print("Date should be numeric")
                            continue
                        if(m == "01" or m == "03" or m == "05" or m == "07" or m == "08" or m == "10" or m == "12") and (int(d)>31 or int(d)<1):
                            print("Date should be between 01 to 31")
                            continue
                        elif m == "02" and (int(y)%4 == 1) and d >= "30":
                            print("Leap year!") 
                            continue
                        elif m== "02" and (int(y)%4 != 1) and d >= "29":
                            print("Date should be less then 29!")
                            continue
                        elif (m=="04" or m=="06" or m=="09" or m=="11") and int(d)>30:
                            print("Date should be between 01 to 30!")
                        else:
                            break
                    dob = "{:04d}-{:02d}-{:02d}".format(int(y), int(m), int(d))
                    cu.execute(f"UPDATE student SET DOB='{dob}' WHERE Admin_no={i[0]}")
                    con.commit()
                    print("Successfully modified...")

                elif field == "3":
                    while True:
                        gender = input("Gender(M/F) --> ")
                        gen = gender.capitalize()
                        g = gen.isalpha()
                        e = len(gen)
                        if g==True and e==1 and (gen == "M" or gen == "F"):
                            break
                        else:
                            print("M for male & F for female")
                    cu.execute(f"UPDATE student SET Gender='{gender}' WHERE Admin_no={i[0]}")
                    con.commit()
                    print("Successfully modified...")
                    
                elif field == "4":
                    while True:
                        cl = input("Class--> ") 
                        c = len(cl)
                        d = cl.isdigit()
                        if  d==True and c <= 2 and int(cl)>=6 and int(cl)<=12:
                            break
                        else:
                            print("Class should be between 6 to 12")
                    cu.execute(f"UPDATE student SET Gender={cl} WHERE Admin_no={i[0]}")
                    con.commit()
                    print("Successfully modified...")
                        
                elif field == "5":
                    while True:
                        father = input("Father name --> ")
                        father = father.title()
                        a = len(father)
                        if a <=60:
                            break
                    else:
                        print("Name word limit is 60")
                    cu.execute(f"UPDATE student SET Father_name='{father}' WHERE Admin_no={i[0]}")
                    con.commit()
                    print("Successfully modified...")

                elif field=="6":
                    while True:
                        mother = input("Mother\'s name --> ")
                        mother = mother.title()
                        a = len(mother)
                        if a <=60:
                            break
                        else:
                            print("Name word limit is 60")
                    cu.execute(f"UPDATE student SET Mother_name='{mother}' WHERE Admin_no={i[0]}")
                    print("Successfully modified...")
                elif field =="7":
                    while True:
                        contact = input("Contact no.--> ")
                        c = len(contact)
                        d = contact.isdigit()
                        if c == 10 and d == True:
                            break
                        else:
                            print("Contact no must be numeric and of 10 characters.")
                    cu.execute(f"UDATE student SET Contact_no={contact} WHERE Admin_no={i[0]}")
                    con.commit()
                    print("Contact_no has been successfully modified...")
                
                elif field=="0":
                    break
        print("\n")

def exam():
    print("\n--------------------------------ADD EXAM DETAILS--------------------------------\n")
    while True:
        admn = input("Admin_no --> ")
        c = "student"
        ck = check_ele(c, admn)
        if ck!=1:
            print(f"Student details does not exist!")
            continue
        x = "exam"
        a = check_ele(x, admn)
        if a>0:
            print(f"Marks for Admin_no {admn} already exists!")
            continue
        ad = len(admn)
        try:
            a = int(admn)
        except:
            print("Admin_no must be numeric")
            continue
        if ad >= 3 and a >=101 :
            break
        else:
            print("Admn_no must be greater then 101")
    while True:
        a = input("Physics --> ")
        b = len(a)
        try:
            a = int(a)
        except:
            print("Mark should be numeric")
            continue
        if b<=2 and a >=00 and a<=70:
            break
        else:
            print("Mark should be between 00 - 70")

    while True:
        c = input("Chemistry --> ")
        d = len(c)
        try:
            c = int(c)
        except:
            print("Mark should be numeric")
            continue
        if d<=2 and c >=00 and c<=70:
            break
        else:
            print("Mark should be between 00 - 70")

    while True:
        e = input("Biology --> ")
        f = len(e)
        try:
            e = int(e)
        except:
            print("Mark should be numeric")
            continue
        if f<=2 and e >=00 and e<=70:
            break
        else:
            print("Mark should be between 00 - 70")

    while True:
        g = input("Maths --> ")
        h = len(g)
        try:
            g = int(g)
        except:
            print("Mark should be numeric")
            continue
        if h<=2 and g>=00 and g<=80:
            break
        else:
            print("Mark should be between 00 - 80")

    while True:
        i = input("Computer Science --> ")
        j = len(i)
        try:
            i = int(i)
        except:
            print("Mark should be numeric")
            continue
        if j<=2 and i>=00 and i<=70:
            break
        else:
            print("Mark should be between 00 - 70")

    while True:
        k = input("Hindi --> ")
        l = len(k)
        try:
            k = int(g)
        except:
            print("Mark should be numeric")
            continue
        if l<=2 and k>=00 and k<=80:
            break
        else:
            print("Mark should be between 00 - 80")

    while True:
        m = input("English --> ")
        n = len(m)
        try:
            m = int(m)
        except:
            print("Mark should be numeric")
            continue
        if n<=2 and m>=00 and m<=80:
            break
        else:
            print("Mark should be between 00 - 80")
    total = int(a) + int(c) + int(e) + int(g) + int(i) + int(k) + int(m) 
    if (g == 0 and k == 0 and  a>=23 and c>=23 and e>=23 and i>=23 and m>=27):
        p_f = "P"
    elif(e==0 and k==0 and a>=23 and c>=23 and g>=27 and i>=23 and m>=27):
        p_f = "P"
    elif(g==0 and i==0 and a>=23 and c>=23 and e>=23 and k>=27 and m>=27):
        p_f = "P"
    elif(e==0 and i==0 and a>=23 and c>=23 and g>=27 and k>=27 and m>=27):
        p_f = "P"
    else:
        p_f = "F"
    query = ("INSERT INTO exam (Admin_no, Physics, Chemistry, English, CS, Hindi, Maths, Bio, Total, Pass_Fail)"
             "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data = (admn, a, c, m, i, k, g, e, total, p_f)
    cu.execute(query, data)
    con.commit()
    print("Marks added succesfully!")

def result():
    print("\n")
    a = input("Enter class: ")
    print("Admin, P,  C,  E, CS, H, M,  B,   T, P/F")
    cu.execute(f"SELECT * FROM exam")
    for i in cu :
        print(i)

def result2_0():
    print("\n")
    while True:
        admn = input("Admin_no --> ")
        x = "exam"
        a = check_ele(x, admn)
        if a!=1:
            print(f"Marks for Admin_no {admn} does not exists!")
            continue
        ad = len(admn)
        try:
            a = int(admn)
        except:
            print("Admin_no must be numeric")
            continue
        if ad >= 3 and a >=101 :
            break
        else:
            print("Admn_no must be greater then 100")
    
    quary = (f"SELECT * FROM exam WHERE Admin_no = {admn}")
    cu.execute(quary)
    for i in cu:
        print(i)
    a = input("\n Press enter to continue...")

def deletes():
    print("\n------------------------------DELETE STUDENT INFO-----------------------------")
    while True:
        admn = input("Enter Admin_no(or 0 to cancel) --> ")
        x = "exam"
        a = check_ele(x, admn)
        if admn=="0":
            break
        if a!=1:
            print(f"Marks for Admin_no {admn} does not exists!")
            continue
        try:
            b = int(a)
        except:
            print("Admin_no must be numeric...")
            continue
        if len(a)==3:
            print(f"Details of Admin_no {a} has been deleted successfully!")
            break
        else:
            print("Admin_no should be 3-digit no.")
    print()
    q = (f"DELETE FROM student WHERE Admin_no={a}")
    cu.execute(q)
    

def students():
    while True: 
        print("--------------------------------OPERATIONS--------------------------------")
        time.sleep(1)
        a = input('''
            1. Add new student                      2. Search student data
            3. Add Exam detail                      4. Result
            5. Search result (Admin_no)             6. Delete student info
            0. Exit\n
            --> ''')
        try:
            b = int(a)
        except :
            print("\n\nInput correct option!")
            continue
        if a == "1":
            add_student()
        elif a == "2":
            search_student()
        elif a == "3":
            exam()
        elif a =="4":
            result()
        elif a == "5":
            result2_0()
        elif a == "6":
            deletes()
        elif a=="0":
            break
        else:
            print("Invalid choice!")
students()

