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
# die = Die()
# print(die.value)  # Should print None initially
# die.roll()  # Roll the die
# print(die.value)  # Should print a random value between 1 and 6

class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1
    
    def roll_die(self):
        return self._die.roll()
    
# Testing the Player class:
my_die = Die()
my_player = Player(my_die)
print(my_player.value)
# print(my_player.counter)  # Should print 10 initially
my_player.roll_die()  # Roll the die
print(my_player.die.value)  # Should print a random value between 1 and 6
# my_player.decrement_counter()  # Decrement the counter
# my_player = Player(my_die, is_computer=False)
# print(my_player.is_computer)
# print(my_player.counter)
# my_player.increment_counter()
# print(my_player.counter)  # Should print 11 after incrementing
# my_player.decrement_counter()
# print(my_player.counter) 