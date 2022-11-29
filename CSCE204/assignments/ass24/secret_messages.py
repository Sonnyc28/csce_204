def encode(message):
    secMes = ""
    encode_map = {
        "a":"z",
        "b":"y",
        "c":"x",
        "d":"w",
        "e":"v",
        "f":"u",
        "g":"t",
        "h":"s",
        "i":"r",
        "j":"q",
        "k":"p",
        "l":"o",
        "m":"n",
        "n":"m",
        "o":"l",
        "p":"k",
        "q":"j",
        "r":"i",
        "s":"h",
        "t":"g",
        "u":"f",
        "v":"e",
        "w":"d",
        "x":"c",
        "y":"b",
        "z":"a",
    }
    for letter in message:
        if letter in encode_map:
            secMes += encode_map[letter.lower()]
        else:
            secMes += letter
    return secMes
def to_letters(symbols):
    message = ""
    decode_map = {
            "a":"z",
            "b":"y",
            "c":"x",
            "d":"w",
            "e":"v",
            "f":"u",
            "g":"t",
            "h":"s",
            "i":"r",
            "j":"q",
            "k":"p",
            "l":"o",
            "m":"n",
            "n":"m",
            "o":"l",
            "p":"k",
            "q":"j",
            "r":"i",
            "s":"h",
            "t":"g",
            "u":"f",
            "v":"e",
            "w":"d",
            "x":"c",
            "y":"b",
            "z":"a",
        }
    for symbol in symbols:
        if symbol in decode_map:
            message += decode_map[symbol.lower()]
        else:
            message += symbol
    return message

print("Secret Messages")
while True:
    choice = input("(E)ncode, (D)ecode, or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "e":
        message = input("Enter a secret message: ")
        encodeMes = encode(message)
        print(f"Your encoded message is: {encodeMes}")
    elif choice == "d":
        decode = input("Enter an encoded message: ")
        decodeMes = to_letters(decode)
        print(f"Your encoded message is: {decodeMes}")

print("Goodbye")