import random
import string

def generate_random_password(length):
    """
    Generates a random password with a mix of lowercase, uppercase letters, and numbers.

    Args:
        length (int): The desired length of the password.
    Return:
        str: The generated random password.
    """
    if length <= 0:
        return ""
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password_list = [random.choice(characters) for _ in range(length)]
    random.shuffle(password_list)
    password = "".join(password_list)
    return password
if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length < 1:
            print("Password length must be at least 1.")
        else:
            generated_password = generate_random_password(password_length)
            print(f"Generated Password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")