# initialize variables
import math
import random


# Checks that users have entered a valid option on a list
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list{valid_ans}"
    while True:
        # gets the user response and makes it lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # checks if the user response is in the word list

            if item == user_response:
                return item

            # checks if the user response is the same as the first letter of an item in a list

            elif user_response == item[0]:
                return item

        # prints error if user enters somthing invalid
        print(error)
        print()


# displays the instructions
def instructions_text():
    print('''To begin, choose the number of rounds (or press <enter> for infinite mode).
You will then chose a lower and higher number (inclusive) that will contain your secret number 
You will then try to guess the number while the computer will give you hints for each guess
You will receive statistics on your guesses used and will be able to see your game history at the end of the game 
Type <quit> to end the game at anytime.
🎂🎂🎂Good Luck🎂🎂🎂''')


# checks if the integer is infinite or more than one for nuber of rounds


def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    elif low is not None and high is None:
        error = (f"please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

        # checks for infinite or exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks if too low
            if low is not None and response < low:
                print(error)

            # checks if too high
            elif high is not None and response > high:
                print(error)

            # if valid returns
            else:
                return response
        except ValueError:
            print(error)


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# **** Main routine starts here ****

rounds_played = 0
mode = 0
rounds_won = 0
rounds_lost = 0
game_history = []
already_guessed = []
end_game = ""
user_choice = ""
feedback = ""
guessed = "yes"

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔽🔽🔽")
print()
round_num = 20
want_instructions = string_checker("Do you want to read the instructions? ", ("yes", "no"))

if want_instructions == "yes":
    instructions_text()

round_num = int_check("how many rounds would you like to play to press enter for infinite", low=1, exit_code="")
# sets the mode to infinite
if round_num == "":
    mode = "Infinite"
    round_num = 5
else:
    mode = "Normal"
low = int_check("what is the lowest number that the secret number can be ")
high = int_check("what is the highest number that the secret number can be ",low=low + 1)
guesses_allowed = calc_guesses(low, high)

while round_num > rounds_played:
    if end_game == "yes":
        break
    rounds_played += 1
    guesses_used = 0
    round_heading = f"\nRound {rounds_played} ({mode} mode)"
    print(round_heading)
    secret = random.randint(low, high)
    user_choice = ""

    while user_choice != secret and guesses_used < guesses_allowed:
        user_choice = int_check("guess the secret", low=low, high=high, exit_code="xxx")
        print("you chose: ", user_choice)

        if user_choice in already_guessed:
            print(f"you have already guessed {user_choice}")
            guessed = "no"

        else:
            already_guessed.append(user_choice)
        # creates a way of breaking out of the loop
        if user_choice == "xxx" and rounds_played > 1:
            rounds_played -= 1
            end_game = "yes"
            break
        elif user_choice > secret:
            feedback = f"Too high try a lower number. you have used {guesses_used + 1}/{guesses_allowed} guesses"
        elif user_choice < secret:
            feedback = f"Too low try a higher number. you have used {guesses_used + 1}/{guesses_allowed} guesses"
        elif user_choice == secret:
            feedback = f"perfect you guessed the number {secret} you used {guesses_used + 1}/{guesses_allowed} guesses"
            if guesses_used == guesses_allowed - 1:
                print("1 guess left")
        if guessed == "yes":
            print(feedback)
            guesses_used += 1
        guessed = "yes"

        if user_choice == secret:
            print("you won and guessed the number")
            rounds_won += 1
        elif not guesses_used < guesses_allowed:
            print("you lost the round")
            rounds_lost += 1

    already_guessed = []

    if mode == "Infinite":
        round_num += 10
    if not user_choice == "xxx":
        game_history.append(feedback)

percent_won = (rounds_won / rounds_played) * 100
percent_lost = (rounds_lost / rounds_played) * 100
print(f"\nyou lost {round(percent_lost)}% of the time")
print(f"\nyou won {round(percent_won)}% of the time")
print("game history")
history = string_checker("do you want to see your history? ", ["yes", "no"])
if history == "yes":
    for item in game_history:
        print(item)

print()
print("thank you for playing higher or lower")
