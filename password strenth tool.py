def check_password_strength():
        print("---password Strength Tool ---")
        password = input ("Enter Password to test: ")

        length = len(password)
        if length >= 8:
                print("Length: Good (8+ characters)")
        else:
                print("Length: Too short (Needs 8+ characters)")

        has_digit = any(char.isdigit() for char in password)
        if has_digit:
                print("Number: Good (Contains at least one digit)")
        else:
                print("Number: Missing (Needs at least one digit)")

        has_special = any(not char.isalnum() for char in password)
        if has_special:
                print("Special Characters: Good")
        else:
                print("Special Characters: Missing(Add !, @, #, etc)")
check_password_strength()
