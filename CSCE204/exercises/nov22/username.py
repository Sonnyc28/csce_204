import random
# pplante@uofsc.com usernme is pplante
def get_username(email):
    return email.split("@")[0]
def get_password(phrase):
    password = ""
    conversions = {
        "a" : "@",
        "b" : "8",
        "e" : "3",
        "g" : "9",
        "i" : "!",
        "o" : "0",
        "s" : "$" ,
        "t" : "7",
    }
    for letter in phrase:
        if letter.lower() in conversions:
            password += conversions[letter.lower()]
        else:
            password += maybe_capitalize(letter)
    return password + str(random.randint(0,100))
def maybe_capitalize(letter):
    if random.randint(0, 1) == 0:
        return letter.lower()
    else:
        return letter.upper()
# Main Program
print("Login Program")
email = input("Enter email: ")
username = get_username(email)
print(f"Username: {username}")
phrase = input("Enter Phrase: ")
password = get_password(phrase)
print(f"Password: {password}")