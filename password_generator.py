import secrets
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


try:
    length = int(input("Password length: "))

    if length < 8:
        print("Please enter a length of 8 or more.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

except ValueError:
    print("Please enter a valid number.")