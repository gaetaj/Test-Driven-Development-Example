'''
Author- Jacob Gaeta
Test Driven Development Example

Program that checks for valid passwords
length between 8 and 20, one lowercase letter,
one uppercase letter, one digit, one symbol.
Returns true if requirements met, false otherwise
'''


def check_pwd(pwd):

    if len(pwd) < 8:
        return False

    if len(pwd) > 20:
        return False

    if not has_lower_case(pwd):
        return False

    return True


def has_lower_case(pwd):

    for p in pwd:
        if p.islower():
            return True

    return False
