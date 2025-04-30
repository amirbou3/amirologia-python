#this code is for sign_up
def sign_up():
    print("------sign up------")
    name = input("type your name: ")
    password = input("type your password: ")
    birth = input("type your birth year: ")
    age = 2025 - int(birth)
    print("you are " + str(age) + " years old")
    print("your seccesfully signed!")
    print("this is your info about your sign up")
    print("your name is: " + name)
    print("your password is: " + password)
    print("your birth year= is: " + birth)
    print("your age is: " + str(age))
#this code is for log_in    
def log_in():
    print("------log in------")
    email = input("type your email: ")
    passcode = input("type your passcode: ")
    print("your secesfully loged!")
    print("this is your info about your log in")
    print("your email is: " + email)
    print("your passcode is: " + passcode)
chose = input("chose sign up(1) or log in(2): ")
sign = "1"
log = "2"
if chose == sign:
    sign_up()
if chose == log:
    log_in()
    
