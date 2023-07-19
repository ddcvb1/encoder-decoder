stopper = True
password = ""
import encoder
import decoder
while stopper:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    option = int(input("Please enter an option: "))
    if option == 1:
        password = int(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")
        print()
        password = encoder.encode(password)
    if option == 2:
        if password != None:
            decoded_password = decoder.decode(password)
            print(f"The encoded password is {decoded_password}, and the original password is {password}.")
            print()
    if option == 3:
        stopper = False