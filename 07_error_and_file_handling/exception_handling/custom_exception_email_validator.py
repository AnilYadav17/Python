#Validate Email Address.

class DotException(Exception):
    pass

class AteTheRateException(Exception):
    pass

class DomainException(Exception):
    pass

def validate(email):
    if email.count("@") != 1:
        raise AteTheRateException("Invalid @ Uses!")
    if "." not in email or email.endswith("."):
        raise DotException("Invalid . Uses!")
    DotException_flag = True
    if email.endswith(".in") or email.endswith(".com") or email.endswith(".gov"):
        DotException_flag = False
    if DotException_flag:
        raise DomainException("Invalid Domain!")


email = input("Enter Email: ")

try:
    validate(email)
    print("Valid Email")
except AteTheRateException as e:
    print("AteTheRateException",e)
    print("Invalid Email address")
except DotException as e:
    print("DotException",e)
    print("Invalid Email address")
except DomainException as e:
    print("DomainException",e)
    print("Invalid Email address")
