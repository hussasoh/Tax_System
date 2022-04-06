import DBController
import keyboard


def validInput(username, password):
    valid = False
    if len(username) >= 3:
        valid = True
    if len(password) >= 6:
        valid = True

    return valid



if __name__ == "__main__":
    dbController = DBController.Database("test12.db")
    userLoggedIn = False
    Running = True
    print("Press E to signUp")
    print("Press I to logIn")
    while Running:
        if keyboard.is_pressed("E"):
            KeepGoing = True
            while KeepGoing:
                newUsername = input("New Username: ")
                newPassword = input("New Password: ")
                validateInput = validInput(newUsername, newPassword)
                if validateInput:
                    valid = dbController.checkUserExists(newUsername)
                    if not valid:
                        dbController.addUser(newUsername, newPassword)
                        KeepGoing = False
                    else:
                        print("Username already Exist!.  If you want to exit press ESC")
                else:
                    print("not a valid input")

        elif keyboard.is_pressed("I"):
            while not userLoggedIn:
                username = input("Username: ")
                password = input("Password: ")
                valid = dbController.checkUserExists(username)
                if valid:
                    userLoggedIn = True
                    Running = False
                    print("LoggedIn")
                else:
                    print("Invalid Credentials")

    username = username if username is not None else ""
    print("Welcome! " + username)