class Decoder:
    @staticmethod
    def decode(password):
        decoded = ''
        for val in password:
            decoded += str(int(val) - 3)
        return decoded
