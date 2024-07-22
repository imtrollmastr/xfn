from cryptography.fernet import Fernet
import os
import sys

def textToSpeech():
    cmdPrompt = input("> ")
    os.system("say " + cmdPrompt)
    textToSpeech()
def loadXFNPanel(success, username):
    if success == True:
        print("Welcome, " + username + ".")
        print("Choose one of the following:")
        print("1) XFN TTS Service")
        print("2) XFN Image Service")
        cmdPrompt = input("> ")
        if cmdPrompt == "1":
            textToSpeech()
        elif cmdPrompt == "2":
            os.system("python3 image.py")
            exit()
        print("Successfully loaded XFN TTS Panel.")
    elif success == False:
        print("401 Unauthorized")

with open("credentials.ini", "rb") as credentialfile:
    contents = str(credentialfile.read())
    username = str.split(contents, "b'username = ")[1]
    password = str.split(contents, "\\npassword = ")[1]
    username = str.split(username, "\\npassword = ")[0]
    password = str.split(password, "\n'")[0]
    print("Enter the following credentials below.")
    print("Username: " + username)
    print("Password: " + password)

print("Enter username:")
cmdPrompt = input("> ")
if cmdPrompt == username:
    print("Enter password:")
    cmdPrompt = input("> ")
    if cmdPrompt == password:
        print("Successfully logged in.")
        loadXFNPanel(True, username)
    else:
        print("Incorrect username or password.")
else:
    print("Incorrect username or password.")


