from Existing_Spy import Spy_Name, Spy_Code_Name, Spy_Age

print "Hello!!! \nWelcome To SpyChat."

def Start_Chat(Spy_Code_Name, Spy_Age):
    print Spy_Code_Name + " What Do You Want To Do?"
    Show_Menu = True
    while Show_Menu:
        Choices = input ("1. Update Status \n2. Add A Friend \n3. Send A Message \n0. Exit ")
        if Choices == 1:
            Status = raw_input("Enter A Status ")
            print "Your Status Is. " + Status
        elif Choices == 2:
            Add_Friend = raw_input("Enter Friend Name To Add ")
            print "Your Friend " + Add_Friend + " Is Added."
        elif Choices == 3:
            Message = raw_input("Type A Message To Send. ")
            print "Your Message \n" + Message
        elif Choices == 0:
            Show_Menu = False
            print "Hope You Enjoyed The Session. \nHave A Good Day..!!"
        else:
            print "Choose A Correct Option."

Existing_Spy = raw_input("Are You A New User (Y/N) ")

if Existing_Spy == "N".lower() or Existing_Spy == "n".upper():
    print "Welcome Back Agent " + Spy_Name + ". \nCode Name " + Spy_Code_Name + "\nAge " + str(Spy_Age)
    Start_Chat(Spy_Code_Name,Spy_Age)


elif Existing_Spy == "Y".lower() or Existing_Spy == "y".upper():
    Spy_Name = raw_input("What's Your Name? ")
    if len(Spy_Name) > 3:
        print "Welcome " + Spy_Name + " Glad to see you."

        Spy_Salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        if Spy_Salutation == "Mr.".upper() or Spy_Salutation == "Ms.".upper() or \
                        Spy_Salutation == "Mr.".lower() or Spy_Salutation == "Ms.".lower() or \
                        Spy_Salutation == "Mr.".isspace():

            Spy_Name = Spy_Salutation + " " + Spy_Name

            print "Alright " + Spy_Name + " " + "We Would Like To Know A Little Bit More About You..."
            Spy_Code_Name = raw_input("Please Select Code Name For You.:-")

            if 0 < len(Spy_Code_Name) < 10:
                print "Welcome " + Spy_Code_Name

                Spy_Age = input("Enter Your Age.:-")
                if 50 > Spy_Age > 18:

                    Spy_Country = raw_input("Enter Your Country Name. ")
                    if Spy_Country == "INDIA".lower() or Spy_Country == "INDIA".upper() or \
                                    Spy_Country == "INDIA".isspace():

                        print "Authentication Completed. \nNow You Can Start Your Chat."

                        Spy_Work_Field = input("Select Your Working Field." 
                                                    "\n1. Under Cover \n2. Analysis \n3. Technician ")
                        if Spy_Work_Field == 1:
                            print "Welcome Agent " + Spy_Code_Name + "\n" + "You Can Leave Your Message Now."
                            Start_Chat(Spy_Code_Name, Spy_Age)

                        elif Spy_Work_Field == 2:
                            print "Now You Can Submit Your Report Here"
                            Start_Chat(Spy_Code_Name, Spy_Age)

                        elif Spy_Work_Field == 3:
                            print "What Is Your Problem?"
                            Start_Chat(Spy_Code_Name, Spy_Age)
                        else:
                            print "Select Your Working Field Properly."

                    else:
                        print "You Should Be An INDIAN."


                else:
                    print "You Are Not Eligible."

            else:
                print "Enter A Valid Code Name."

        else:
            print "Please Choose A Valid Salutation."

    else:
        print "Please Enter your Name Correctly."

else:
    print "Please select You Are A New User Or Not?"
