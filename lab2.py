#counter
def counter():
    dictionary = {}
    for i in message:
        if i.isalpha():
            dictionary[i] = dictionary.get(i, 0) + 1
    for i in dictionary:
                print(i, ":", dictionary[i])

#sort
def sort():
    symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
    s_message = ""
    for letter in message:
        if letter not in symbols:
            s_message = s_message + letter
    s_message = s_message.split()
    s_message.sort()
    print("Sorted:" )
    for word in s_message:
        if len(word) > 3:
            print(word)

message = input("Enter text: ")
counter()
sort()
