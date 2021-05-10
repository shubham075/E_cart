import mysql.connector


mydb_connect=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)
print(mydb_connect)
mycursor=mydb_connect.cursor()



#mycursor.execute("create table user_reg (fname varchar(20), lname varchar(20), contact int, address varchar(255), email varchar(100), password varchar(10))")
#contact datatype changed to big int.
#mycursor.execute("create table admin_data(userID varchar(20), password int)")
#mycursor.execute("create table user_data(userID varchar(20), password int)")
#mycursor.execute()

#function for two step password verification =================================================

def pass_correction(pass1,pass2):
    while pass1!=pass2:
        print("Enter two different password:")
        print()
        pass1=input("Enter your password:")
        pass2=input("Renter your password:")
        if (pass1==pass2):
            print("password succesfully set!")

def user_reg():
    pass3=pass4=0
    print()
    print("== Welcome to user registration page==")
    fname=input("Enter your first name:")
    lname=input("Enter your last name:")
    name=fname+" "+lname
    contact=int(input("Enter your contact number:"))
    address=input("Enter your address:")
    email=input("Enter your mail address:")
    pass3=input("Enter your password:")
    pass4=input("Renter your password:")    
    pass_correction(pass3,pass4)
    print("Registration done!")
    #store date =========================?????
    sql1="insert into user_data(userID, password) values(%s,%s)"
    val1=(name, pass3)
    mycursor.execute(sql1,val1)
    sql="insert into user_reg(fname,lname,contact,address,email,password) values(%s,%s,%s,%s,%s,%s)"
    val=(fname,lname,contact,address,email,pass3)
    mycursor.execute(sql,val)
    mydb_connect.commit()
    print()
    print("Registration Done!")
    print("Login with your name and password!")
    print()
#==============================================================================================================================

user_IDlist=[]
user_passlist=[]

mycursor.execute("select userID from user_data")
for i in mycursor:
    for x in i:
        user_IDlist.append(x)
#mydb_connect.commit()

mycursor.execute("select password from user_data")
for i in mycursor:
    for x in i:
        user_passlist.append(x)
mydb_connect.commit()

#print(user_IDlist)
#print(user_passlist)



def check_user(id,passw):
    if ((id in user_IDlist) and  (passw in user_passlist)):
        print("========================Sucessfully login!====================================================")
        print("Welcome, ",id)
        print()
    
        category_list=['flour','rice','pulses','personal_care','fruits']
        for i in category_list:
            print(i)
        print()
        user_search=input("Search from the above lists ")
        print()
        if user_search in category_list:
            sql="select product_name from {}  "
            mycursor.execute(sql.format(user_search))
            for x in mycursor:
                for y in x:
                    print(y)
                    print()
            user_search1=input("Enter product name from avobe list:  ")
            if user_search1 in y:

                user_quantity=int(input("Enter quantity of the product: "))
                sql2="select quantity from {} where product_name = '{}' "
                mycursor.execute(sql2.format(user_search, user_search1))
                quant1=mycursor.fetchall()
                for a in quant1:
                    for b in a:
                        quant=b

                print(quant)
                #mydb_connect.commit()

                final_quantity=quant-user_quantity
                sql3="update {} set quantity= {} where product_name= '{}'"
                mycursor.execute(sql3.format(user_search,final_quantity,user_search1))
                sql4="select rate from {} where product_name = '{}' "
                mycursor.execute(sql4.format(user_search, user_search1))
                for i in mycursor:
                    for c in i:
                        price=c
                print(price)
                
                mydb_connect.commit()
                print()
                print("product added")
                user_final_price=user_quantity*price
                print("Your final price is: ",user_final_price)
                print()
                reg_user_list=["Press 1 for continue shopping", "Press 2 for exit"]
                for i in reg_user_list:
                    print(i)
                print()
                reg_user_input=int(input("Enter your response here: "))
                if reg_user_input==1:
                    check_user(id,passw)
                if reg_user_input==2:
                    #start.start()
                    pass
                    

    #else:
        #print("Wrong credential!!!!!!!!!!\n")
        #start.start()


          

    


