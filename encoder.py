def encode(password):
    string_pass = str(password)
    encoded_password = ""
    for i in string_pass:
        encoded_password = encoded_password + str(int(i) + 3)
    return encoded_password