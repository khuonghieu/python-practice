class Session(object):
    NUMBER_TO_TEXT_MAP = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6':'six', '7': 'seven', '8': 'eight', '9': 'nine'}

class InvalidValueException(Exception):
    def __init__(self, message: str):
        self.message = message

