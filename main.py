from guizero import App, Text, TextBox, PushButton, CheckBox
import string
import random


def createPassword():
    password = []
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    charList = s1

    if capitals.value:
        charList += s2
    if numbers.value:
        charList += s3
    if specials.value:
        charList += s4

    for i in range(int(count.value)):
        rndChar = random.choice(charList)
        password.append(rndChar)

    result = "".join(password)
    f = open("created_password.txt", "w")
    f.write(result)
    f.close()


app = App(title="Password Generator")

message = Text(app, text="How many characters do you need in your password?")
count = TextBox(app)
specials = CheckBox(app, text="Do you need any special characters? ")
numbers = CheckBox(app, text="Do you need any numbers? ")
capitals = CheckBox(app, text="Do you need any capital letters? ")

button = PushButton(app, text="Create Password", command=createPassword)

app.display()
