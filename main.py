def encode(user_password):
    new_password = ""
    for i in user_password:
        if int(i) == 7:
            new_password += "0"
        elif int(i) == 8:
            new_password += "1"
        elif int(i) == 9:
            new_password += "2"
        else:
            new_password += str(int(i) + 3)
    return new_password
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            user_password = input("Please enter your password to encode: ")
            encoder = encode(user_password)
            print("Your password has been encoded and stored!\n")
        elif user_input == 2:
            print(f"The encoded password is {encoder}, and the original password is {user_password}\n")
        else:
            break


if __name__ == "__main__":
    main()