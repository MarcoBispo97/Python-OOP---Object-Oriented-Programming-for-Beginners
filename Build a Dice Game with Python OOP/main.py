import random

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return self._value
    
# Testing the class:
die = Die()
print(die.value)  # Should print None initially
die.roll()  # Roll the die
print(die.value)  # Should print a random value between 1 and 6
