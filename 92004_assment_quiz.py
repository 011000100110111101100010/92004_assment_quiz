import random

# this check if the input is in line with a valid answer
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
    You will begin by choosing the number of questions that you would like to get asked (<enter> for infinite questions)
    then you will be given an algebra problem and a possible answer (rounded to 2dp) and asked if that answer is correct 
    try to get as many correct answers as possible good luck :)''')


# this will generate the question that will be printed
def question(a, b, sign, x__location):
    if sign == "X" and x__location == 2 or sign == "X" and x__location == 3:
        return f"{a}𝒳 = {b}"
    if x__location == 1:
        return f"{a} {sign} {b} = 𝒳"
    if x__location == 2:
        return f"𝒳 {sign} {a} = {b}"
    return f"{a} {sign} 𝒳 = {b}"


# this uses all the possible options to generate an answer for x
def new_question(var_symbol, a, b, x_placement):
    try:
        if x_placement == 1 and var_symbol == "+" or x_placement == 2 and var_symbol == "-":
            return a + b
        elif x_placement == 2 and var_symbol == "+" or x_placement == 3 and var_symbol == "+":
            return b - a
        elif x_placement == 1 and var_symbol == "-" or x_placement == 3 and var_symbol == "-":
            return a - b
        elif x_placement == 1 and var_symbol == "÷" or x_placement == 3 and var_symbol == "÷":
            return a / b
        elif x_placement == 1 and var_symbol == "X" or x_placement == 2 and var_symbol == "÷":
            return a * b
        elif x_placement == 2 and var_symbol == "X" or x_placement == 3 and var_symbol == "X":
            return b / a
    except ZeroDivisionError:
        return "fail"


# this checks that the input is an integer

def int_check(text, low=None, escape=None):
    # defines the error
    error = (f"please enter an integer that is "
             f"more than / equal to {low}")

    # checks for infinite or exit code
    while True:
        response = input(text).lower()
        if response == escape:
            return response

        try:
            # checks if too low
            if low is not None and int(response) < low:
                print(error)

            # if valid returns
            else:
                return int(response)
        except ValueError:
            print(error)


# ***main routine***
# initializes the variables
rounds_played = 0
round_num = 0
answer = 0
# var1 and 2 are used in equations as the random variables
var1 = 0
var2 = 0
symbol = ""
x_location = 0
# x location is where x will be in the asked questions
correct_answers = 0
incorrect_answers = 0
# feedback is what will be printed as the answer
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
round_num = int_check("how many questions would you like to be asked to press enter for infinite? ", low=1,
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
    # generates the random symbol x location and variables and weather the answer will be correct
    x_location = random.randint(1, 3)
    symbol = random.choice(["+", "X", "÷", "-"])
    var1 = random.randint(-25, 25)
    var2 = random.randint(-25, 25)
    show_answer = random.choice(["yes", "no"])
    answer = new_question(symbol, var1, var2, x_location)
    if show_answer == "no":
        if symbol == "X" or symbol == "÷":
            wrong = random.uniform(-100, 100)
        else:
            wrong = random.randint(-100, 100)
        if round(answer, 2) == round(wrong, 2):
            show_answer = "yes"
    else:
        wrong = answer
    # is the answer creates a zero division error it makes the symbol addition
    if answer == "fail":
        symbol = "+"
        answer = new_question(symbol, var1, var2, x_location)
        wrong = answer
    # asks the previously generated question

    asked_question = question(var1, var2, symbol, x_location)
    print(asked_question)
    user_input = string_checker(f"is 𝒳 approximately {round(wrong, 2)} ", ["yes", "no", "xxx"])

    # this checks if the user is trying to quit on round 1 and loops the question until they stop trying to quit
    while user_input == "xxx" and rounds_played < 1:
        print("cannot end game on round one ")
        user_input = string_checker(f"is 𝒳 approximately {round(wrong, 2)} ", ["yes", "no", "xxx"])
    # lets the user quit by pressing xxx
    if user_input == "xxx" and rounds_played > 0:
        end_game = "yes"
        break
    # checks the users answers and makes the feedback
    elif user_input == show_answer:
        feedback = f"correct the answer is : {round(answer, 2)} rounded to 2dp"
        correct_answers += 1
    else:
        feedback = f"im sorry that is incorrect, the answer is approximately: {round(answer, 2)} rounded to 2dp"
        incorrect_answers += 1
    if not user_input == "xxx":
        print(feedback)
    rounds_played += 1
    # increases the rounds if the game is infinite
    if mode == "Infinite":
        round_num += 10
    if not user_input == "xxx":
        history.append(round_heading)
        history.append(f"the equation given was: {asked_question}")
        history.append(f"the possible variable was: {round(wrong,2)}")
        history.append(f"your answer was: {user_input}")
        history.append(feedback)
        history.append("")

# holds the game history
percent_won = (correct_answers / rounds_played) * 100
percent_lost = (incorrect_answers / rounds_played) * 100
print(f"\nyou were incorrect: {round(percent_lost)}% of the time")
print(f"\nyou were correct: {round(percent_won)}% of the time")
print("***game history***")
history_ask = string_checker("do you want to see your history? ", ["yes", "no"])
if history_ask == "yes":
    for item in history:
        print(item)
