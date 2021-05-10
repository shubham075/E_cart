import user_reg as user
import admin_data as admin


def start():
    print("=======Welcome to Ecart================")
    cart_list=["Enter 1 fr user registration page","Enter 2 for admin login page","Enter 3 for user login page"]
    for i in cart_list:
        print(i)
    print()
    
    response=int(input("Enter Your Response here: "))
    print()
    


    if response==1:
        user.user_reg()

    if response==2:
        admin_inputID=input("Enter you username here:")
        admin_input_password=int(input("Enter your password: "))
        admin.check_admin(admin_inputID, admin_input_password)

    if response==3:
        user_inputID=input("Enter you username here:")
        user_input_password=int(input("Enter your password: "))
        user.check_user(user_inputID, user_input_password)
    else:
        start()

start()
