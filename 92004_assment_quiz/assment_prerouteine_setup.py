import random


# this check if the input is in line with a valid x
def string_checker(text, valid_ans):
    error = f"Please enter a valid option from the following list{valid_ans}"
    while True:
        # gets the user response and makes it lowercase
        user_response = input(text).lower()

        for valid in valid_ans:
            # checks if the user response is in the word list

            if valid == user_response:
                return valid

            # checks if the user response is the same as the first letter of an item in a list

            elif user_response == valid[0]:
                return valid

        # prints error if user enters somthing invalid
        print()
        print(error)
        print()


# this holds the instructions

def instructions_text():
    print('''Algebra quiz
    You will begin by choosing the number of questions that you would like to get asked (<enter> for infinite questions).
    You will then be given an algebra problem to solve for 𝒳 get as many questions right as possible>
    Good luck and have fun :''')


# creates a question to be printed later
def question(a, b, sign, x__location):
    if sign == "÷":
        return f"{b} ÷ 𝒳 = {a}"
    if sign == "X" and x__location == 2 or sign == "X" and x__location == 3:
        return f"{a}𝒳 = {b}"
    if x__location == 2:
        return f"𝒳 {sign} {a} = {b}"
    return f"{a} {sign} 𝒳 = {b}"

# generates var2 also known as b in other places
def new_question(var_symbol, a, b, x_placement):
    if var_symbol == "+":
        return a+b
    if var_symbol == "-" and x_placement == 3:
        return a-b
    if var_symbol == "-" and x_placement == 2:
        return b-a
    if var_symbol == "X" or var_symbol == "÷":
        return a*b


# checks the validity of the received input and if valid determines the output
def int_check(question, low=None, high=None, exit_code=None, escape=None):
    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer as your x"

    elif low is not None and high is None:
        error = (f"please enter an integer that is "
                 f"more than / equal to {low}")

    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()
        if response == escape:
            return response

        # checks for infinite or exit code

        try:

            if response == exit_code or int(response) == exit_code:
                return "correct"

            # checks if too low
            if low is not None and int(response) < low:
                print(error)

            # checks if too high
            elif high is not None and int(response) > high:
                print(error)

            # if valid returns
            else:
                return int(response)
        except ValueError:
            print(error)


rounds_played = 0
round_num = 0
x = 0
# var1 and 2 are used in equations as the random variables
var1 = 0
var2 = 0
symbol = ""
x_location = 0
# x location is where x will be in the asked questions
correct_answers = 0
incorrect_answers = 0
# feedback is what will be printed as the x
feedback = ""
# holds the games history to be printed at request
history = []
# until specified otherwise the mode will be printed as normal
mode = "normal"
user_input = ""
# end game is no until they wish to quit
end_game = "no"

print()
print("*** Welcome to The Ultimate Algebra Math Quiz ***")
print()

# asks if the user wants to read the instructions and if they say yes it prints them
instructions = string_checker("would you like to view the instructions? ", ["yes", "no"])
if instructions == "yes":
    instructions_text()

# asks how many rounds they want to play and allows <enter> for infinite rounds
round_num = int_check("how many questions would you like to be asked? (press enter for infinite) ", low=1,
                      escape="")
# ensures that the rounds played will be endless by having an additional 20 rounds
if round_num == "":
    round_num = 20
    mode = "Infinite"

while round_num > rounds_played:
    # checks if the game ends at the start of the round
    if end_game == "yes":
        break
    round_heading = f"\nQuestion {rounds_played+1} ({mode} mode)"
    print(round_heading)
    # randomizes the new question by generating random variables
    symbol = random.choice(["+", "X", "÷", "-"])
    var1 = random.randint(-25, 25)
    x = random.randint(-25, 25)
    x_location = random.randint(2,3)
    var2 = new_question(symbol, var1, x, x_location)

    # this is a variable as it is used to store if history
    asked_question = question(var1, var2, symbol, x_location)
    print(asked_question)
    user_input = int_check("find 𝒳 ", exit_code=x, escape="xxx")
    # catches people trying to end the game on round 1
    while user_input == "xxx" and rounds_played < 1:
        print("cannot skip on round one ")
        user_input = int_check("find 𝒳", exit_code=x, escape="xxx")
    # lets people end the game after round 1
    if user_input == "xxx" and rounds_played > 0:
        end_game = "yes"
        break

    if user_input == "correct":
        feedback = "🎉🎉🎉that's correct good job🎉🎉🎉"
        correct_answers += 1
    else:
        feedback = f"❌❌❌im sorry that is incorrect the answer is: {x}❌❌❌"
        incorrect_answers += 1
    if not user_input == "xxx":
        print(feedback)
    rounds_played += 1

    if mode == "Infinite":
        round_num += 10
    if not user_input == "xxx":
        history.append(round_heading)
        history.append(f"the equation given was: {asked_question}")
        history.append(f"your answer was: {user_input}")
        history.append(feedback)
        history.append("")

percent_won = (correct_answers / rounds_played) * 100
percent_lost = (incorrect_answers / rounds_played) * 100
print(f"you got {correct_answers}/{rounds_played} questions correct")
print(f"\nyou were incorrect: {round(percent_lost)}% of the time")
print(f"\nyou were correct: {round(percent_won)}% of the time")
print("***game history***")
history_ask = string_checker("do you want to see your history? ", ["yes", "no"])
if history_ask == "yes":
    for item in history:
        print(item)
