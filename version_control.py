# Ivy Li

# Variable to store the encoded password
stored_password = 0


# Function to encode the password
def encode(password):
    encoded_password = ""
    for char in password:
        # Shift each digit up by 3 numbers
        encoded_digit = str((int(char) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# Olivia Howse
def decoder(password):
    decoded_password = ''
    for i in password:
        encoded_digit = str((int(i)-3) % 10)
        decoded_password += encoded_digit
    return decoded_password


# Main function to run the program
def main():
    global stored_password

    while True:
        # Display the menu options
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print(" ")

        # Get user's choice
        choice = input("Please enter an option: ")

        if choice == "1":
            # Encoding option
            password = input("Please enter your password to encode: ")
            stored_password = encode(password)
            print("Your password has been encoded and stored!")
            print(" ")

        elif choice == "2":
            # Decoding option
            print("The encoded password is " + stored_password + ", and the original password is " + decoder(stored_password) + ".")
            print(" ")

        elif choice == "3":
            # Quit option
            break

        else:
            # Invalid choice
            print("Invalid choice.")


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
