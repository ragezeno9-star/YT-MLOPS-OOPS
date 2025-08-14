class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.login=False
        self.menu()
    def menu(self):
        userinput=input("""welcome to chatbook !! how would you like to proceed?
                        1.press 1 to signup
                        2.press 2 to login
                        3.press 3 to write a post
                        4.press 4 to message a friend
                        5.press any other key to exit """)
        if userinput=="1":
           self.signup()
        elif userinput=="2":
            self.signin()
        elif userinput=="3":
            pass
        elif userinput=="4":
            pass
        else:
            exit()
    def signup(self):
        email=input("enter email")
        passcode=input("enter password")
        self.username=email
        self.password=passcode
        print("you have signed up successfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by pressing 1 in main menu")
        else:
            email=input("enter email")
            passcode=input("enter your passcode here")
            if self.username==email and self.password==passcode:
                print("successfully signed in")
                self.login=True
            else:
                print("please input correct credentials")
        self.menu()

obj =chatbook()