from management import Management
from reports import Report
from Users import Users

if __name__ == "__main__":

    manager = Management()

    option = int(input("[1] Log In \n[2] Sign Up \n[3] Add Report \n[4] View Graph \n[5] Exit\n"))
    user_id = -1

    while True:
        if option == 2:
            username = input("Create a username: ")
            password = input("Create a password: ")
            age = input("Type your age: ")
            sex = input("Type your sex: ")
            # user_id = input("TYPE USER_ID")
            # user = Users(username, password, user_id, age, sex)
            manager.add_user(username, password, age, sex)

        elif option == 1:
            user_found = False
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for user in manager.users:
                if user.get_username() == username:
                    user.log_in(password)
                    user_found = True
                    if user.logged_in:
                        user_id = user.get_id()


            if not user_found:
                print("User does not exist")

        elif option == 3:
            if manager.users[user_id-1].logged_in == True:
                a = int(input("Enter your stress level from 1-10: "))

                report = Report(a, user_id)
                manager.users[user_id-1].add_report(report)
                #manager.reports_number += 1
                manager.reports_number += 1


        elif option == 4:


        elif option == 5:
            break


        else:
            print("Invalid input")
            break
        option = int(input("[1] Log In \n[2] Sign Up \n[3] Add Report \n[4] View Graph \n[5] Exit\n"))
