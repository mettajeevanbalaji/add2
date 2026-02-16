def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase, one lowercase, and one digit
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    return has_upper and has_lower and has_digit


def create_password():
    while True:
        password = input("Create a password: ")
        if is_valid_password(password):
            print("Password accepted!")
            break
        else:
            print("Invalid password. It must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one digit.")


# Run the validator
create_password()