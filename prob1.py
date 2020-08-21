from enums import Session, InvalidValueException

def convertString(inString):
    strList = inString.split()
    for key, value in Session.NUMBER_TO_TEXT_MAP.items():
        for i in range(len(strList)):
            if key in strList[i]:
                strList[i] = strList[i].replace(key, value)
            elif value in strList[i]:
                strList[i] = strList[i].replace(value ,key)
    return " ".join(strList)

print(convertString('1 one 2 two 3 three'))
print(convertString('I completed 2 sessions and I rated my expert five stars'))
print()


