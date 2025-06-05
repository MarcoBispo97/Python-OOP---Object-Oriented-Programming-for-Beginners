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
#print(my_player.value)
# print(my_player.counter)  # Should print 10 initially
my_player.roll_die()  # Roll the die
#print(my_player.die.value)  # Should print a random value between 1 and 6
# my_player.decrement_counter()  # Decrement the counter
# my_player = Player(my_die, is_computer=False)
# print(my_player.is_computer)
# print(my_player.counter)
# my_player.increment_counter()
# print(my_player.counter)  # Should print 11 after incrementing
# my_player.decrement_counter()
# print(my_player.counter) 

class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    @property
    def play(self):
        """
        Main game loop.

        Prints a welcome message and enters a loop where it rolls the dice and
        determines the winner and loser. The loop continues until either the
        player or the computer's score reaches 0.

        Note: This method does not take any parameters and does not return any
        value.
        """
        print("🎲 Welcome to dice game! 🎲")
        while True:
            input("\Press Enter to play or type 'here' to exit: ")
            
            self.play_round()

            if self.check_game_over():
                break


    def play_round(self):
        #Welcome the user
        #Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the rolled values
        self.show_dice(player_value, computer_value)

        #Determine the winner and loser:
        if player_value > computer_value:
            print("🎉 You win this round! 🎉")
            self.update_scores(winner = self._player, loser = self._computer)
        elif player_value < computer_value:
            print("😢 You lose this round. 😢")
            self.update_scores(loser=self._player, winner=self._computer)
        else:
            print("It's a tie! No points awarded.")

        #Show the values
        print(f"Your score: {self._player.counter}")
        print(f"Computer's score: {self._computer.counter}")

        self.show_final_scores()

    def print_welcome_message(self):
        print("------ New Round -----")
        print("🎲 Press any key to roll the dice.🎲 ")    

    def show_dice(self, player_value, computer_value):
        print(f"You rolled: {player_value}")
        print(f"Computer rolled: {computer_value}")

    def update_scores(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_final_scores(self):
        print("==================================")
        print("🎲 Final Scores 🎲")
        print(f"Your score: {self._player.counter}")
        print(f"Computer's score: {self._computer.counter}")
        print("==================================")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._computer)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._player)
            return True

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n==================================")
            print(" GAME OVER! 😢")
            print("\n==================================")
            print("The computer wins! Better luck next time! 🎲")
            print("\n==================================")
        else:
            print("\n==================================")
            print(" GAME OVER! 🎉")
            print("\n==================================")
            print("Congratulations! You win! 🎉")
            print("\n==================================")

        

player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)
game = DiceGame(my_player, computer_player)

#Start the game
game.play()