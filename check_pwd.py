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

    if not has_upper_case(pwd):
        return False

    if not has_digit(pwd):
        return False

    if not has_symbol(pwd):
        return False

    return True


def has_lower_case(pwd):

    for p in pwd:
        if p.islower():
            return True


def has_upper_case(pwd):

    for p in pwd:
        if p.isupper():
            return True


def has_digit(pwd):

    for d in pwd:
        if d.isdigit():
            return True


def has_symbol(pwd):

    valid_symbol = "~`!@#$%^&*()_+-="
    for s in pwd:
        if s in valid_symbol:
            return True
