def encode(password):
    encoded_pass = ''

    for digit in password:
        num = int(digit)
        if num < 7:
            num = num + 3
        elif 7 <= num <= 9:
            num = num - 7
        encoded_pass += str(num)

    return encoded_pass


def decode(encoded_password):


if __name__ == "__main__":
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        password = ""
        new_pass = ""
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:

        else:
            break

