import mysql.connector


mydb_connect=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)
print(mydb_connect)
mycursor=mydb_connect.cursor()


'''
category_list=[]
def getting_list():
    mycursor.execute("show tables")
    for i in mycursor:
        category_list.append(i)
    print(category_list)
'''

admin_IDlist=[]
admin_passlist=[]

mycursor.execute("select userID from admin_data")
for i in mycursor:
    for x in i:
        admin_IDlist.append(x)
#mydb_connect.commit()

mycursor.execute("select password from admin_data")
for i in mycursor:
    for x in i:
        admin_passlist.append(x)
mydb_connect.commit()

#print(admin_IDlist)
#print(admin_passlist)

def check_admin(id,passw):
    print()
    if ((id in admin_IDlist) and  (passw in admin_passlist)):
        print("========================Sucessfully login!====================================================")
        print()
        admin_entry()
    #else:
        #print("You have entered worng crenditials!")
        #start.start()

def admin_entry():
    admin_list=["Enter 1 for add product","Enter 2 for update product"]
    for i in admin_list:
        print(i)
    admin_response=int(input("Enter your response for next action "))
    if admin_response==1:
        add_product()
    if admin_response==2:
        update_product()

#========================================================================================================================================
def add_product():
    #getting_list()
    category_list=['flour','rice','pulses','personal_care','fruits']
    for i in category_list:
        print(i)
    category=input("Enter product category name from above list: ")
    print()
    if (category in category_list):
        product_name=input("Enter product name: ")
        product_price=int(input("Enter price of product in kg: "))
        product_quantity=int(input("Enter product quantity: "))

        sql="insert into {} (product_name, rate, quantity) values(%s,%s,%s)"
        val=(product_name,product_price,product_quantity)

        mycursor.execute(sql.format(category),val)
        mydb_connect.commit()
        print("product successfully added!")
        print("==========================================================================================")
        print()
        admin_entry()
    else:
        print("Entered worng product name")
        action=int(input("press any key to return to previous or press 1 for retry "))
        if action==1:
            add_product()
        else:
            print("===============================================================================================")
            print("Entered worng key word!")
            admin_entry()

#===================================================================================================================================        
            
def update_product():
    category_list=['flour','rice','pulses','personal_care','fruits']
    for i in category_list:
        print(i)
    update_product_name1=input("Enter product name to be updated: ")
    print()
    if update_product_name1 in category_list:
        sql2="select product_name from {}"
        mycursor.execute(sql2.format(update_product_name1))
        print("product lists in database")
        for i in mycursor:
            print(i)
        update_product_name2=input("\nEnter product name: ")
        #update_product_price=int(input("Enter price of product in kg: "))
        update_product_quantity=int(input("Enter product quantity: "))

        sql3="select quantity from {} where product_name = '{}' "
        mycursor.execute(sql3.format(update_product_name1,update_product_name2))
        #quant1=mycursor.fetchall()
        for a in mycursor:
            for b in a:
                quantity=b
        
        final_quantity=quantity+update_product_quantity
        sql4="update {} set quantity = {} where product_name = '{}'"
        mycursor.execute(sql4.format(update_product_name1,final_quantity,update_product_name2))
        mydb_connect.commit()
        print("Product updated!")
        admin_response1=int(input("press 1 for next update or press 2 for exit"))
        if admin_response1==2:
            pass
        if admin_response1==1:
            update_product()
            



        



