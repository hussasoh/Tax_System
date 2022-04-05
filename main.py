import DBController

if __name__ == "__main__":
    dbController = DBController.Database("test12.db")
    userLoggedIn = False

    while not userLoggedIn:
        username = raw_input("Username: ")
        password = raw_input("Password: ")
        valid = dbController.validateUser(username, password)
        if valid:
            userLoggedIn = True
        else:
            print "Invalid Credentials"

    print "LoggedIn"
