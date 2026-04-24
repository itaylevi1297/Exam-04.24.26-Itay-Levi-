def camel_to_hyphen(text: str) -> str:
    result = ""

    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result

print(camel_to_hyphen("helloPython"))
print(camel_to_hyphen("myVariableName"))
print(camel_to_hyphen("python"))
print(camel_to_hyphen("aBigTest"))
