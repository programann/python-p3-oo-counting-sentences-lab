#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        #Instantiating
        self._value = value if isinstance(value, str) else ""
  # The getter method
    @property
    def value(self):
        return self._value
  # The setter method to enforce the requirements
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if not self._value:
            return 0
        #
        import re
        # Function of the \b is to check for word boudaries which include spaces and stuff
        #re.findall finds all substrings with the pattern of r'\b[^,?!]*[.?!]'
        sentences = re.findall(r'\b[^.!?]*[.!?]', 
        self._value)
        return len(sentences)

# if __name__ == "__main__":
#     s = MyString("Hello world. Is this a question? Yes it is!")
#     print(s.is_sentence())  # Output: False
#     print(s.is_question())  # Output: False
#     print(s.is_exclamation())  # Output: True
#     print(s.count_sentences())  # Output: 3


# print(type(__name__))