import random

class Game:
    WHEEL = [
        1000,
        2000,
        5000,
        "Lose Your Turn",
        10000,
        "Bankrupt",
        25000,
        "Free Trip"
    ]
    PHRASES = ["purple", 'platypus bear', 'dragons in dungeons', 'alex is stupid', 'ice skating rink']
    
    def start_game(self):
        self.set_rand_phrase()
        self.wheel_spin = None
        self.guesses = []
        
    def set_rand_phrase(self):
        self.current_phrase = random.choice(self.PHRASES)
        self.revealed_chars = [False for i in self.current_phrase]

    def spin_wheel(self):
        while True:
            x = len(self.WHEEL) + 1
            while x >= len(self.WHEEL):
                x = int(random.expovariate(2) * len(self.WHEEL))

            result = self.WHEEL[x]
            print(f"You spun {result}!")
            if not type(result) is int:
                print(f"You spun '{result}', The Game will now end")
                print("Sike! rolling again")
                continue
            break
        self.wheel_spin = result
    
    def __str__(self):
        '''
        will be called when using str(), print(), or similar functions on a Phrase Object
        '''
        result = '|'
        for i, char in enumerate(self.current_phrase):
            if char == ' ':
                result += '|'
            elif self.revealed_chars[i]:
                result += char
            else:
                result += '_'
        result += '|'
        return result

    def guess(self):
        while True:
            print(f"The phrase so far is: {self}")
            guess = input('What letter would you like to guess?: ').strip().lower()

            if len(guess) > 1:
                print("Please enter a single letter.")
                continue
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("Please enter a valid letter.")
                continue
            elif guess in self.guesses:
                print("This letter has already been guessed.")
                continue

            break
        # guess is valid
        self.guesses.append(guess)

        if guess in self.current_phrase:
            for i, char in enumerate(self.current_phrase):
                if char == guess:
                    self.revealed_chars[i] = True

            prize = self.wheel_spin * self.current_phrase.count(guess)
            print(f"The guess '{guess}' was in the phrase {self.current_phrase.count(guess)} times! You've won {prize}")

            #Check if phrase fully guessed
            if all([self.revealed_chars[i] or char == ' ' for i, char in enumerate(self.current_phrase)]):
                print("You Won!")
                exit()

            return prize
        else:
            print(f"The letter '{guess}' does not occur in the phrase! No prize this time.")
            return 0

        
#Play game
game = Game()
score = 0

game.start_game()
while True:
    game.spin_wheel()
    score += game.guess()
    print(f"your total score is now {score}\n")

