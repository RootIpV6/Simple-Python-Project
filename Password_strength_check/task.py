def password_check(password):
    length =len(password)>=8
    figure=any(char.isdigit() for char in password)
    uppercase_lower=any(char.isupper() for char in password)
    lower_case=any(char.islower() for char in password)
    special_character=any(char in "!'^+%&/()=?>£#$½¾{¾[]}}\|" for char in password)

    if length and figure and uppercase_lower and lower_case  and special_character:
        return "Password is strong"
    else:
        return"Password is weak"

password =input("Enter Password")
print(password_check(password))