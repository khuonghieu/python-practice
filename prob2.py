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

class Step():
    def __init__(self, number_of_sessions: int, number_of_stars: str):
        if(number_of_sessions < 1):
            raise InvalidValueException('Invalid num of session')
        elif(number_of_stars not in ['one', 'two', 'three', 'four', 'five']):
            raise InvalidValueException('Invalid num of star')
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars
    def make_step(self):
        print(f"I completed {self.number_of_sessions} sessions and I rated my expert {self.number_of_stars} stars.")

step1 = Step(2, "one")
step1.make_step()
print()
step2 = Step(1, 'five')
step2.make_step()
print()
step3 = Step(4, "six")
step3.make_step()