import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    length = min(length, 15)  # Limit length to 15 characters

    if length < 1:
        raise ValueError("Password length should be at least 1.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length (up to 15 characters): "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(
        length=password_length,
        use_uppercase=include_uppercase,
        use_digits=include_digits,
        use_special_chars=include_special_chars
    )

    print("Generated Password:", generated_password)
