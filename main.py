# Jennifer Holland Final Assignment

import random
import csv
########################## Classes ###############################

class StudentAccount:

    # This module is the constructor
    def __init__(self, forename, surname, phone, email, password, accNumber):
        self.forename = forename
        self.surname = surname
        self.phone = phone
        self.email = email
        self.password = password
        self.accNumber = accNumber
        self.balance = 100

    # This module allows the user to select their modules
    def selectModules(self, x, moduleNo):

        if x == "1" and moduleNo == 1:
            module1 = "Programming 1"
            return module1
        elif x == "1" and moduleNo == 2:
            module2 = "Programming 1"
            return module2
        elif x == "2" and moduleNo == 1:
            module1 = "Programming 2"
            return module1
        elif x == "2" and moduleNo == 2:
            module2 = "Programming 2"
            return module2
        elif x == "3" and moduleNo == 1:
            module1 = "Networking 1"
            return module1
        elif x == "3" and moduleNo == 2:
            module2 = "Networking 1"
            return module2
        elif x == "4" and moduleNo == 1:
            module1 = "Mathematics"
            return module1
        elif x == "4" and moduleNo == 2:
            module2 = "Mathematics"
            return module2

    # This module allows the user to add points to their balance
    def addPoints(self, points):
        self.balance += int(points)

    # This module allows the user to pay for printing pages
    def printing(self, printCost):
        self.balance -= printCost

    # This module allows the user to pay for food portions
    def buyFood(self, portionCost):
        self.balance -= portionCost

    # This module allows the user to change their email address
    def changeEmail(self, newEmail):
        self.email = newEmail

    # This module allows the user to change their phone number
    def changePhone(self, newPhone):
        self.phone = newPhone

    # This module allows the user to change their password
    def changePass(self, newPass):
        self.password = newPass



########################## Main Body #############################

students = {}

# This code reads in information from the csv file storage.csv if it exists
#This error handling ensures that something will print if the storage.csv file does not exist yet
try:
    f = open("storage.csv", "r")
    dict_reader = csv.DictReader(f)
    ordered_dict_from_csv = list(dict_reader)[0]
    students = dict(ordered_dict_from_csv)
except FileNotFoundError:
    print("\n\t\tThere is not currently any student data stored to bring from storage.")
except IndexError:
    print("\n\t\tThere is not currently any student data stored to bring from storage.")


# This  while loop contains the whole program and ensures it will run until stopped by the user
while True:
    print("\n\t\tThank you for using the self-service student registration program!")
    print("""\n\t\tPlease select one of the following options:
                1. Student Registration
                2. Module Selection and Verification
                3. Student Account Top-Up
                4. Shopping
                5. Check Balance
                6. Edit Information
                7. Reporting Information
                q. Quit the Program""")
    option = input("\n\t\tPlease enter your option:")

    # This loop dictates which section of the code the user will jump to, a.k.a which option they pick
    # This option allows the user to quit the program
    if option.lower() == "q":
        break

    # This option allows the user to register
    elif option == "1":
        forename = input("\n\t\tPlease enter your forename.")
        # This loop ensures that the user enters a forename
        while forename == "":
            print("\n\t\tYou must enter a forename.")
            forename = input("\n\t\tPlease enter your forename.")

        surname = input("\n\t\tPlease enter your surname.")
        # This loop ensures that the user enters a surname
        while surname == "":
            print("\n\t\tYou must enter a surname.")
            surname = input("\n\t\tPlease enter your surname.")

        phone = input("\n\t\tPlease enter your contact phone number.")
        # This loop ensures that the user enters a phone number
        while phone == "":
            print("\n\t\tYou must enter a phone number.")
            phone = input("\n\t\tPlease enter your contact phone number.")

        email = input("\n\t\tPlease enter your contact email address.")
        # This loop ensures that the user enters an email address
        while email == "":
            print("\n\t\tYou must enter an email address.")
            email = input("\n\t\tPlease enter your contact email address.")
        else:
            # This loop ensures that the email contains an "@" symbol
            while "@" not in email:
                print("\n\t\tSorry, that email address is not valid because it does not contain an @ symbol. Please try again.")
                email = input("\n\t\tPlease enter your contact email address.")

        while True:
                password = input("\n\t\tPlease enter a password. It must be more than 8 characters.")
                # This loop ensures that the user enters a password
                while password == "":
                    print("\n\t\tYou must enter a password.")
                    password = input("\n\t\tPlease enter a password.")
                # This loop ensures that the password is longer than 8 characters.
                while len(password) <= 8:
                    print("\n\t\tYour password must be more than 8 characters.")
                    password = input("\n\t\tPlease enter a password.")
                confirmpass = input("\n\t\tPlease confirm your password.")

                # This loop ensures that the two passwords that the user enters match
                if password == confirmpass:
                    break
                else:
                    print("\n\t\tSorry, those passwords do not match. Please try again.")

        accNumber = random.randint(1,1000)
        # This loop ensures that the randomly generated accNumber is unique
        while accNumber in students.keys():
            accNumber = random.randint(1,1000)
        # This option allows the registration to be completed once the accNumber is unique
        if accNumber not in students.keys():
            object = StudentAccount(forename, surname, phone, email, password, accNumber)
            students[accNumber] = object
            print("\n\t\tMr/Ms", forename, surname, "Your account number is:", accNumber)

    # This option allows the user to select and view modules
    elif option == "2":
        while True:
            # This code ensures that the account number entered exists in the students dictionary
            try:
                accountNumber = int(input("\n\t\tPlease enter your account number."))
            except ValueError:
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            if accountNumber not in students.keys():
                print("\n\t\tThat is not a valid account number, please try again.")
                break
            # This code ensures that the password matches the password stored for that account number
            else:
                passcheck = input("\n\t\tPlease enter your password.")
                if passcheck != students[accountNumber].password:
                    print("\n\t\tThat password is not valid, please try again.")
                    break
                # If the account number and password match then the user will be granted access to this section of the program
                else:
                        print("""\n\t\tPlease select one of the following option:
                                1) Select modules
                                2) View selected modules
                                q) Exit to main page""")
                        initialOption = input("\n\t\tPlease select your option:")

                        # This option allows the user to select their two modules
                        if initialOption == "1":

                            print("""\n\t\tPlease select two of the following modules or enter q to return to the main page:
                                    1) Programming 1
                                    2) Programming 2
                                    3) Networking 1
                                    4) Mathematics
                                    q) Exit to main page""")

                            option1 = input("\n\t\tPlease select your first module.")
                            # This loop ensures that option1 is valid
                            while option1 != "1" and option1 != "2" and option1 !="3" and option1 != "4" and option1.lower() != "q":
                                print("\n\t\tSorry, that is not a valid option. Please try again.")
                                option1 = input("\n\t\tPlease select your first module.")

                            option2 = input("\n\t\tPlease select your second module.")
                            # This loop ensures that option2 is valid
                            while option2 != "1" and option2 != "2" and option2 != "3" and option2 != "4" and option2.lower() != "q":
                                print("\n\t\tSorry, that is not a valid option. Please try again.")
                                option2 = input("\n\t\tPlease select your second module.")

                            # This loop ensures that the user has not picked the same module twice
                            while option1 == option2:
                                print("\n\t\tSorry, you cannot pick the same module twice. Please try again.")
                                option1 = input("\n\t\tPlease select your first module.")
                                option2 = input("\n\t\tPlease select your second module.")

                            # Call statements to the module that will assign the correct modules to the user
                            module1 = students[accNumber].selectModules(option1, 1)
                            module2 = students[accNumber].selectModules(option2, 2)

                        # This option allows the user to view their currently selected modules
                        elif initialOption == "2":
                            #This error handling prints a line if the user does not have any modules currently selected
                            try:
                                print("\n\t\tYour selected modules are:", module1, "and", module2)
                            except NameError:
                                print("\n\t\tSorry, you do not currently have any modules selected. Please select your modules and try again.")

                        # This option allows the user to exit to the main page
                        elif initialOption.lower() == "q":
                            break

                        # This option ensures that the user enters a valid option
                        else:
                            print("\n\t\tSorry, that is not a valid option. Please try again.")

    # This option allows the user to top-up their points balance
    elif option == "3":
        while True:
            # This code ensures that the account number entered exists in the students dictionary
            try:
                accountNumber = int(input("\n\t\tPlease enter your account number."))
            except ValueError:
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            if accountNumber not in students.keys():
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            # This code ensures that the password matches the password stored for that account number
            else:
                passcheck = input("\n\t\tPlease enter your password.")
                if passcheck != students[accountNumber].password:
                    print("\n\t\tThat password is not correct, please try again.")
                    break
                # If the account number and password match then the user will be granted access to this section of the program
                else:
                    points = input("\n\t\tHow many points would you like to deposit?")

                    print("\n\t\tYou are going to deposit", points, " points to account number", accNumber)
                    confirm = input("\n\t\tConfirm? Y/N:")
                    # This code allows the user to confirm or deny whether they want to add the points
                    if confirm.lower() == "y":
                        #This error handling ensures that the user enters a valid number of points
                        try:
                            students[accNumber].addPoints(points)
                            print("\n\t\tGreat!", points, "points have been added to your account, and your new balance is", students[accNumber].balance, "points.")
                            break

                        except ValueError:
                            print("\n\t\tThat is not a valid number of points. Please try again.")

                    else:
                        print("\n\t\tNo points have been added to your account.")
                        break

    #This option allows the user to shop for page prints and food portions
    elif option == "4":
        currentBalance = students[accNumber].balance

        while True:
            # This code ensures that the account number entered exists in the students dictionary
            try:
                accountNumber = int(input("\n\t\tPlease enter your account number or q to exit."))
            except ValueError:
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            if accountNumber == "q":
                break

            elif accountNumber not in students.keys():
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            # This code ensures that the password matches the password stored for that account number
            else:
                passcheck = input("\n\t\tPlease enter your password.")
                if passcheck != students[accountNumber].password:
                    print("\n\t\tThat password is not correct, please try again.")
                    break

                # If the account number and password match then the user will be granted access to this section of the program
                else:

                    print("""\n\t\tPlease select one of the following options:
                                1) Print
                                2) Buy Food Portions
                                q) Exit to main page""")
                    option = input("\n\t\tPlease enter your option:")

                    while True:
                        # This option allows the user to buy printing pages
                        if option == "1":
                            print("\n\t\tEach page print (single or double) costs 0.2 points. Your current balance is", students[accNumber].balance, "points")
                            #This error handling ensures that the user enters a valid number of pages
                            try:
                                pages = int(input("\n\t\tHow many pages would you like to print?"))
                            except ValueError:
                                print("\n\t\tThat is not a valid number of pages, please try again.")
                                break

                            printCost = pages * 0.2

                            # This code ensures that the user has enough points for the number of pages they are attempting to print
                            if students[accNumber].balance >= printCost:
                                students[accNumber].printing(printCost)
                                print("\n\t\tYou have printed", pages, "pages. Your new balance is", students[accNumber].balance, "points.")
                                break

                            else:
                                print("\n\t\tYou do not have enough money for that many pages!")
                                break

                        # This option allows the user to buy food portions
                        elif option == "2":
                            print("\n\t\tEach food portion costs 2 points. Your current balance is", students[accNumber].balance, "points")
                            #This error handling ensures that the user enters a valid number of food portions
                            try:
                                portions = int(input("\n\t\tHow many portions would you like to buy?"))
                            except ValueError:
                                print("\n\t\tThat is not a valid number of portions, please try again.")
                                break

                            portionCost = portions * 2

                            # This code ensures that the user has enough points for the number of food portions
                            if students[accNumber].balance >= portionCost:
                                students[accNumber].buyFood(portionCost)
                                print("\n\t\tYou have bought", portions, "portions. Your new balance is", students[accNumber].balance, "points")
                                break

                            else:
                                print("\n\t\tYou do not have enough money for that many portions!")
                                break


                        # This option allows the user to exit to the main page and displays their total shopping cost and coupon upon exiting
                        elif option == "q":
                            print("\n\t\tYour total cost for shopping is", (currentBalance - students[accNumber].balance), " points and your new balance is", students[accNumber].balance, "points.")
                            coupon = random.randint(1,10000)
                            print("\n\t\tYour shopping coupon is", coupon)
                            break

                        # This option ensures that the user selects a valid option
                        else:
                            print("\n\t\tSorry, that is not a valid option.")
                            break

    #This option allows the user to check their current balance
    elif option == "5":
        while True:
            # This code ensures that the account number entered exists in the students dictionary
            try:
                accountNumber = int(input("\n\t\tPlease enter your account number."))
            except ValueError:
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            if accountNumber not in students.keys():
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            # This code ensures that the password matches the password stored for that account number
            else:
                passcheck = input("\n\t\tPlease enter your password.")
                if passcheck != students[accountNumber].password:
                    print("\n\t\tThat password is not correct, please try again.")
                    break

                # If the account number and password match then the user will be granted access to this section of the program
                else:
                    print("\n\t\tYour current balance is", students[accNumber].balance, "points.")
                    break

    #This option allows the user to edit their information
    elif option == "6":
        while True:
            # This code ensures that the account number entered exists in the students dictionary
            try:
                accountNumber = int(input("\n\t\tPlease enter your account number."))
            except ValueError:
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            if accountNumber not in students.keys():
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            # This code ensures that the password matches the password stored for that account number
            else:
                passcheck = input("\n\t\tPlease enter your password.")
                if passcheck != students[accountNumber].password:
                    print("\n\t\tThat password is not correct, please try again.")
                    break

                # If the account number and password match then the user will be granted access to this section of the program
                else:

                    print("""\n\t\tPlease select an option:
                                1)Edit E-mail Address
                                2)Edit Phone Number
                                3)Edit Password
                                q)Quit to main page""")
                    option = input("\n\t\tPlease select your option:")

                    # This option allows the user to exit to the main page
                    if option == "q":
                        break

                    # This option allows the user to change their e-mail address
                    elif option == "1":
                        newEmail = input("\n\t\tPlease enter the new e-mail address:")

                        while newEmail == "":
                            print("\n\t\tYou must enter a new email address.")
                            newEmail = input("\n\t\tPlease enter the new e-mail address:")
                        else:
                            while "@" not in newEmail:
                                print("\n\t\tSorry, that email address is not valid because it does not contain an @ symbol. Please try again.")
                                newEmail = input("\n\t\tPlease enter the new email address.")

                        students[accNumber].changeEmail(newEmail)
                        print("\n\t\tYour new email address is", students[accNumber].email)

                    # This option allows the user to change their phone number
                    elif option == "2":
                        newPhone = input("\n\t\tPlease enter the new phone number:")

                        while newPhone == "":
                            print("\n\t\tYou must enter a new phone number.")
                            newPhone = input("\n\t\tPlease enter the new phone number:")
                        students[accNumber].changePhone(newPhone)
                        print("\n\t\tYour new phone number is", students[accNumber].phone)

                    #This option allows the user to change their password
                    elif option == "3":
                        newPass = input("\n\t\tPlease enter the new password:")

                        while newPass == "":
                            print("\n\t\tYou must enter a new password.")
                            newPass = input("\n\t\tPlease enter a password.")

                        while len(newPass) <= 8:
                            print("\n\t\tYour password must be more than 8 characters.")
                            newPass = input("\n\t\tPlease enter a password.")

                        confirm = input("\n\t\tPlease confirm your password:")

                        if confirm == newPass:
                            students[accNumber].changePass(newPass)
                            print("\n\t\tYour new password is:", students[accNumber].password)
                        else:
                            print("\n\t\tSorry those passwords do not match.")

                    #This option ensures that the user enters a valid option
                    else:
                        print("\n\t\tThat is not a valid option, please try again.")

    #This option allows the user to see the information stored about themselves
    elif option == "7":
        while True:
            # This code ensures that the account number entered exists in the students dictionary
            try:
                accountNumber = int(input("\n\t\tPlease enter your account number."))
            except ValueError:
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            if accountNumber not in students.keys():
                print("\n\t\tThat is not a valid account number, please try again.")
                break

            # This code ensures that the password matches the password stored for that account number
            else:
                passcheck = input("\n\t\tPlease enter your password.")
                if passcheck != students[accountNumber].password:
                    print("\n\t\tThat password is not correct, please try again.")
                    break

                # If the account number and password match then the user will be granted access to this section of the program
                else:
                    print("\n\t\tAccount number:", students[accNumber].accNumber)
                    print("\t\tForename:", students[accNumber].forename)
                    print("\t\tSurname:", students[accNumber].surname)
                    print("\t\tPhone number:", students[accNumber].phone)
                    print("\t\tE-mail address:", students[accNumber].email)
                    print("\t\tBalance:", students[accNumber].balance, "points")
                    #This error handling occurs if the user has not selected modules yet
                    try:
                        print("\t\tModules selected:", module1, "and", module2)
                    except NameError:
                        print("\t\tYou have not yet selected any modules")
                    break

    #This option ensures that the user selects a valid option
    else:
        print("\n\t\tThat is not a valid option, please try again.")

#This code writes the students dictionary to students.csv when the user quits the program
with open('storage.csv', 'w') as w:
    w = csv.DictWriter(w, students.keys())
    w.writeheader()
    w.writerow(students)