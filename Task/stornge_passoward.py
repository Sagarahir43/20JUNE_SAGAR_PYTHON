import re
class registration():
    def username(self):
        usrnm = input("Enter USername :")
        usrnm_pattern = "[A-Z]+[a-z]+[0-9]"
        valid_usrnm = re.findall(usrnm_pattern,usrnm)
        if valid_usrnm:
            pass
        else:
            print("Enter valid username")
            registration.username(self)
    def user_pass(self):
        usrpass = input("Enter password (Password Should include capital letter and special character) :")
        if len(usrpass) < 8 or len(usrpass) > 13:
            print("Password Must contain Minimum 8 character and maximum 12")
            registration.user_pass(self)
        else :    
           verfiy_pass = input("Re Enter Your password :")
           if usrpass == verfiy_pass:
               usrpass_pattern = "[A-Za-z\W]+[a-z][\W]+[0-9]"
               valid_pass = re.findall(usrpass_pattern,usrpass)
               if valid_pass:
                print("Registration Succesfully....")
               else:
                print("Enter Strong Password")
                registration.user_pass(self)
r = registration()
r.username()
r.user_pass()                                


              