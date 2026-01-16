class chatbook:

    __user_id = 0


    def __init__(self):
        self.id = chatbook.__user_id + 1
        self.__name = "Default User"
        self.username = " "
        self.passward = " "
        self.loggedin = False
        self.menu()

    def get_name(self):
        return self.__name
    
    def get_name(self, value):
        self_name = value


    def menu(self):
        user_input = input("""
                           Welcome to chatbook !! How would you proceed
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to me
                           ssage a friend
                           5. Press any key to exit
                           
                           """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()

        elif user_input == '3':
            self.my_post()
        
        elif user_input == '4':

            self.sendmsg()

        else:
            exit()
    
    def signup(self):
        email = input("Enter your email id:")
        pwd = input("Enter your passward:")
        self.username = email
        self.passward = pwd
        print("you have signed up successfully !")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.passward == '':
            print("Please signup first by pressing 1 the main ma=enu")

        else:
            uname = input(f"Enter your email/username here --> ")
            pwd = input("Enter your password here -->  ")
            if self.username == uname and self.passward == pwd:
                print("You have logged in successfully !")
                self.loggedin = True

            else:
                print("Invalid credentials, please try again !")

        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Write your post here --> ")
            print(f"Following content has been posted --> {txt}")

        else:
            print("You need to login first to post something")

        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here --> ")
            friend = input("Whom to send the message --> ")
            print(f"Your message has been send to {friend}")

        else:
            print("You need to first signin first to post something.. ")

        print("\n")
        self.menu()


obj = chatbook()




        
        