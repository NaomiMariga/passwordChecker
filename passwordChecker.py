import re

def passwordChecker(password):
    if len(password) >= 8:
        res = re.search("\s", password)
        if not res:
            res = re.search("[a-z]", password)
            if res:
                res = re.search("[A-Z]", password)
                if res:
                    res = re.search("[0-9]", password)
                    if res:
                        res = re.search("[`,~,@,#,$,%,^,&,*,(,),_,-,+,=,.,?]", password)
                        if res:
                            message = "Password check passed"
                            print(message)
                            return True
                            
                        else:
                            message = "password must contain special characters"
                    else:
                        message = "password must contain numbers"    
                else:
                    message = "password must contain uppercase characters"
            else:
                message = "password must contain lowercase characters"
        else:
            message = "password can not contain spaces"
    else:
        message = "password must be 8 characters long or more"
    print(message)
    return False
    

