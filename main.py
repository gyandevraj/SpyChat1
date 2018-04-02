from Existing_Spy import Spy
from steganography.steganography import Steganography
from datetime import datetime

print "Hello!!! \nWelcome To SpyChat."

STATUS_MESSAGE = ["gOOD mORNInG", "HeLLo", "NAmaStE"]

friends = []


def add_status(c_status):
    global new_status
    if c_status != None:
        print "your current status is " + c_status
    else:
        print "you don't have any status currently"
    existing_status = raw_input("Do you want to add new status? Y/N ")
    if existing_status.upper() == "Y":
        new_status = raw_input("Enter your status: ")
        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)

    elif existing_status.upper() == "N":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice = input("Enter your choice: ")
        new_status = STATUS_MESSAGE[user_choice - 1]
    update_status = new_status
    return update_status


def add_friend():
    frnd_detail = {"Name": raw_input("What is your name? "), "Age": input("What is your age? "),
                   "Code_Name": raw_input("What is your code name? "), "is_online": True, "chats":[]}

    if len(frnd_detail["Name"]) > 3 and 18 < frnd_detail["Age"] < 50 and frnd_detail["Code_Name"] > 3:

        friends.append(frnd_detail)

    else:
        print "Friend's Can't be added"

    return len(friends)

def select_frnd():
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + ". " + frnd["Name"]
        serial_no = serial_no + 1
    user_selected_friend = input("Choose Your Friend To Send or Read Message: ")
    user_selected_friend_index = user_selected_friend - 1
    return user_selected_friend_index


def send_message():
    selected_friend = select_frnd()
    original = raw_input("What is the name of original image: ")
    text = raw_input("enter message: ")
    output = "out.jpg"
    Steganography.encode(original, output, text)
    print "send"
    new_chat = {"message": text,
               "time": datetime.now(),
               "send by me": True}
    friends[selected_friend]['chats'].append(new_chat)


def read_message():
    selected_friend = select_frnd()
    output = raw_input("Which image you want to decode? ")
    text = Steganography.decode(output)
    print "The decoded message is " + text
    new_chat = {"message": text,
               "time": datetime.now(),
               "send by me": False}
    friends[selected_friend]['chats'].append(new_chat)


def Start_Chat(Spy):
    print Spy["Code_Name"] + " What Do You Want To Do?"

    current_status = None

    Show_Menu = True
    while Show_Menu:
        Choices = input("1. Update Status \n2. Add A Friend \n3. Send A Message \n4. Read A Message \n0. Exit ")
        if Choices == 1:

            current_status = add_status(current_status)
            print "updated status " + current_status

        elif Choices == 2:

            no_of_friends = add_friend()
            print "you have " + str(no_of_friends) + " friends"

        elif Choices == 3:
            print "Select A Friend To Send Message: "
            send_message()

        elif Choices == 4:
            print "Select A Friend To Read Message: "
            read_message()

        elif Choices == 0:
            Show_Menu = False
            print "Hope You Enjoyed The Session. \nHave A Good Day..!!"
        else:
            print "Choose A Correct Option."




Existing_Spy = raw_input("Are You A New User (Y/N) ")



if Existing_Spy == "N".lower() or Existing_Spy == "n".upper():
    print "Welcome Back Agent " + Spy["Name"] + ". \nCode Name " + Spy["Code_Name"] + "\nAge " + str(Spy["Age"])
    Start_Chat(Spy)


elif Existing_Spy == "Y".lower() or Existing_Spy == "y".upper():
    Spy ={
        "Name" : "",
        "Age" : 0,
        "Code_Name" : ""
    }
    Spy["Name"] = raw_input("What's Your Name? ")
    if len(Spy["Name"]) > 3:
        print "Welcome " + Spy["Name"] + " Glad to see you."

        Spy_Salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        if Spy_Salutation == "Mr.".upper() or Spy_Salutation == "Ms.".upper() or \
                        Spy_Salutation == "Mr.".lower() or Spy_Salutation == "Ms.".lower() or \
                        Spy_Salutation == "Mr.".isspace():

            Spy["Name"] = Spy_Salutation + " " + Spy["Name"]

            print "Alright " + Spy["Name"] + " " + "We Would Like To Know A Little Bit More About You..."
            Spy["Code_Name"] = raw_input("Please Select Code Name For You.:-")

            if 0 < len(Spy["Code_Name"]) < 10:
                print "Welcome " + Spy["Code_Name"]

                Spy["Age"] = input("Enter Your Age.:-")
                if 50 > Spy["Age"] > 18:

                    Spy_Country = raw_input("Enter Your Country Name. ")
                    if Spy_Country == "INDIA".lower() or Spy_Country == "INDIA".upper() or \
                                    Spy_Country == "INDIA".isspace():

                        print "Authentication Completed. \nNow You Can Start Your Chat."

                        Spy_Work_Field = input("Select Your Working Field."
                                               "\n1. Under Cover \n2. Analysis \n3. Technician ")
                        if Spy_Work_Field == 1:
                            print "Welcome Agent " + Spy["Code_Name"] + "\n" + "You Can Leave Your Message Now."
                            Start_Chat(Spy)

                        elif Spy_Work_Field == 2:
                            print "Now You Can Submit Your Report Here"
                            Start_Chat(Spy)

                        elif Spy_Work_Field == 3:
                            print "What Is Your Problem?"
                            Start_Chat(Spy)
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
