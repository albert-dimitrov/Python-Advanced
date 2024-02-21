import re

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class MoreThanOneAtSymbol(Exception):
    pass

class InvalidNameError(Exception):
    pass

VALID_DOMAINS = ("com", "bg", "net", "org")
MIN_NAME_SYMBOL_COUNT = 4

email_is_valid = False
password_is_valid = False
pattern_name = r'\w+'

email = input()


while not email_is_valid:

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    elif '@' not in email:
        raise MustContainAtSymbolError("Email must contain @!")
    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOL_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")
    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {' .'.join([d for d in VALID_DOMAINS])}")
    elif re.findall(pattern_name, email.split("@")[0])[0] != email.split('@')[0]:
        raise InvalidNameError('Name must contain only letters, digits and underscores!')

    print('Email is valid')
    email_is_valid = True

while not password_is_valid:

    password = input('Enter your password:')

    

