from Existing_Spy import Spy_Name, Spy_Code_Name, Spy_Age


My_Name = raw_input("My Name Is.:-")
if len(My_Name)>3:
    print "Hello My Name Is " + My_Name
    print "Welcome To SpyChat."

    Existing_Spy = raw_input("Are You A New User. (yes or no) ")
    if Existing_Spy == "no":
        print "Welcome Back Agent " + Spy_Name +  ". \nCode Name " + Spy_Code_Name +  "\nAge " + str(Spy_Age)
        print "You Are Online."

    elif Existing_Spy == "yes":

            Spy_Name = raw_input("What's Your Name? ")
            if len(Spy_Name)>3:
                print "Welcome " + Spy_Name + " Glad to see you."
                Spy_Salutation = raw_input("What should we call you (Mr. or Ms.)? ")
                if Spy_Salutation == "Mr.".upper() or Spy_Salutation == "Ms.".upper() or\
                                Spy_Salutation == "Mr.".lower() or Spy_Salutation == "Ms.".lower():
                    print Spy_Salutation + " " + Spy_Name
                    Spy_Name = Spy_Salutation + " " + Spy_Name
                    print "Alright " + Spy_Name + " " + "We Would Like To Know A Little Bit More About You..."
                    Spy_Code_Name = raw_input("Please Select Code Name For You.:-")
                    if len(Spy_Code_Name)>0 and len(Spy_Code_Name)<10:
                        print "Welcome " + Spy_Code_Name + " " + "Now You Can Proceed Further."
                        Spy_Age = input("Enter Your Age.:-")
                        if 50>Spy_Age>18:
                            print "You Are Eligible To Be A Spy."
                            Spy_Decision = raw_input("Are You Sure To Be A Spy?"\
                                                     "(yes , no or may be)?")
                            if Spy_Decision == "yes":
                                print "Congrats You Are In. "
                                print Spy_Code_Name + " " + "You Are Online."
                            elif Spy_Decision == "no":
                                print "Thank you See you Again."
                            elif Spy_Decision == "may be":
                                print "Please Be Sure And Then Come Again."
                            else:
                                print "Hope We Will See You Again"
                        else:
                            print "You Are Not Eligible."
                    else:
                        print "Enter A Valid Code Name."
                else:
                    print "Please Choose A Valid Salutation."
            else:
                print "Please Enter your Name Correctly."

else:
    print "Please Enter A Valid Name."

