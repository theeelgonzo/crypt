# encrypting messages

def encMessage(message, key):

    #key = 3
    string = []
    newString = []
    for char in message:
        string.append(ord(char) + key)
    print(string)

    for char in string:
        newString.append(chr(char))
    newString = "".join(newString)
    print(newString)

    textFile = open("messages/message.txt", "a")
    textFile.write(newString)
    textFile.close()


#encMessage("Hello, World", 3)

#encMessage("Hello, World", 10)

def recMessage():
    message = input("Input your message: ")
    key = int(input("Define your offset key as an integer: "))
    if type(key) is int:
        print("Encrypthing message.")
        encMessage(message, key)
    else:
        print(type(key))
        print("Please use an integer for the offset key.")

recMessage()
