import random
import string

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = uppercase + lowercase + digits + symbols

# User input
length = int(input("Enter the desired password length: "))

# Check minimum length
if length < 4:
    print("Password length should be at least 4.")
else:
    # Ensure at least one character from each category
    password =[
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle to make the password random
    random.shuffle(password)

    # Convert list to string
    password = "".join(password)

    # Display password
    print("\nGenerated Password:", password)