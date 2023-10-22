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


encMessage("Hello, World", 3)

encMessage("Hello, World", 10)

