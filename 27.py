#  Create a  program captable of displaying question to the user like KBC.
# User List data type to store the questions and thier correct answer.

import random

def q_AND_ans(x, y,ran_n, ran_no):
    print(x[ran_n][ran_no])
    ans_list = y[ran_n][ran_no]
    for options in ans_list:
        print(options)


def ans_correction(y, ran_n, ran_no):
    user_input = input("\nEnter your answer: ")
    user_ans = user_input.upper()
    correct_a = y[ran_n][ran_no].upper()

    if(user_ans == correct_a):
        kbc_amount = win_kbc[ran_no]
        total_kbc.append(kbc_amount)
        t = sum(total_kbc)
        print("\nCongratulations, You are win '",kbc_amount, "'rupess \n-------------You are WIN total '",t ,"' rupess.-------------\n")
    else:
        print("\nSorry, But you are lost this chance.\n-------------Try again next time-------------\n")


# Questions set
q = [
    ["What color is a ripe banana?",
     "How many legs does a dog typically have?",
     "What is the capital city of the United States?",
     "What is the chemical symbol for water?"],
     ["Which planet is known as the Red Planet?",
     "What is the capital of France?",
     "What color is the sky on a sunny day?",
     'What is the opposite of "hot"?'],
    ["What is the capital of Japan?", 
     "Which of the following is a primary color?", 
     "What is the chemical symbol for gold?", 
     "How many days are there in a leap year?"],
     ]


# Answers set 
ans = [ 
        [
          ['Yellow', 'Red', 'Green', 'Blue'],
          ['Three', 'Two', 'One', 'Four'],
          ['New York', 'Los Angeles', 'Washington', 'Chicago'],
          ['H2O', 'O2', 'SO4', 'CO2']
        ],
        [ ['Venus', 'Mars', 'Jupiter', 'Moon'],
          ['London', 'Paris', 'Rome', 'Berlin'],
          ['Yellow', 'Red', 'Green', 'Blue'],
          ['Cold', 'Wet', 'Tall', 'Fast']
        ],
        [
          ['Beijing', 'Seoul', 'Tokyo', 'Bangkok'], 
          ['Orange', 'Purple', 'Green', 'Red'], 
          ['Au', 'Ag', 'Fe', 'Cu'], 
          ['364', '365', '366', '367']
          ]
      ]



# Answers keys 
correct_ans = [
    ['Yellow', 'Four', 'Washington', 'H2O'],
    ['Mars', 'Paris', 'Blue', 'Cold'],
    ['Tokyo', 'Red', 'Au', '366']
             ]

# kbc amount list
win_kbc = [3000, 4000, 5000, 6000]

total_kbc = []


# loop for game start 
gameCount = 0
while(gameCount<5):
    print("\n------------------")
    print("Question no:", gameCount+1)
    print("------------------\n")
    r_no = random.randint(0, 3)
    r_n = random.randint(0, 2)
    q_AND_ans(q, ans, r_n, r_no)
    ans_correction(correct_ans, r_n, r_no)
    gameCount += 1


