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
            pass
        elif userinput=="2":
            pass
        elif userinput=="3":
            pass
        elif userinput=="4":
            pass
        else:
            exit()

obj =chatbook()