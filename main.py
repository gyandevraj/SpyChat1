from Existing_Spy import Spy_Name, Spy_Code_Name, Spy_Age


print "Hello!!! \nWelcome To SpyChat."

Existing_Spy = raw_input("Are You A New User (Y/N) ")
if Existing_Spy == "N".lower() or Existing_Spy == "n".upper() :
    print "Welcome Back Agent " + Spy_Name + ". \nCode Name " + Spy_Code_Name + "\nAge " + str(Spy_Age)
    print "You Are Online."

elif Existing_Spy == "Y".lower() or Existing_Spy == "y".upper():

            Spy_Name = raw_input("What's Your Name? ")
            if len(Spy_Name)>3:
                print "Welcome " + Spy_Name + " Glad to see you."

                Spy_Salutation = raw_input("What should we call you (Mr. or Ms.)? ")
                if Spy_Salutation == "Mr.".upper() or Spy_Salutation == "Ms.".upper() or\
                                Spy_Salutation == "Mr.".lower() or Spy_Salutation == "Ms.".lower() or\
                                Spy_Salutation == "Mr.".isspace():

                    Spy_Name = Spy_Salutation + " " + Spy_Name

                    print "Alright " + Spy_Name + " " + "We Would Like To Know A Little Bit More About You..."
                    Spy_Code_Name = raw_input("Please Select Code Name For You.:-")

                    if 0 < len(Spy_Code_Name) < 10:
                        print "Welcome " + Spy_Code_Name + " " + "Now You Can Proceed Further."

                        Spy_Age = input("Enter Your Age.:-")
                        if 50>Spy_Age>18:

                            Spy_Country = raw_input("Enter Your Country Name. ")
                            if Spy_Country == "INDIA".lower() or Spy_Country == "INDIA".upper() or \
                                            Spy_Country == "INDIA".isspace():
                                print "You Are Eligible To Be A Spy."

                                Spy_Decision = raw_input("Are You Sure To Be A Spy?"
                                                         "(yes , no or may be)?")
                                if Spy_Decision == "yes":
                                    print "Congrats You Are In. "

                                    print "Your Entered Details Are:- " \
                                          "\n Name = " + Spy_Name + "\n Your Code Name Will Be = " + Spy_Code_Name + \
                                          "\n Your Age = " + str(Spy_Age) + "\n Location = " + Spy_Country

                                elif Spy_Decision == "no":
                                    print "Thank you See you Again."

                                elif Spy_Decision == "may be":
                                    print "Please Be Sure And Then Come Again."

                                else:
                                    print "Hope We Will See You Again"

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