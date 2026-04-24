strings =[]
while True:
    text = input("enter a string:")

    if text == "quit":
        break
    strings.append(text)

found = False
for word in strings:
    if word [::-1] in strings and word [::-1] != word:
        found = True
        break


if found:
    print("reverse match found")
else:
    print("no reverse match found")