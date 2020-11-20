import random

# Generate scissor, rock, paper
choices = ['rock', 'scissors', 'paper']
computer = random.choice(choices)

# Prompt the user to enter scissor, rock, or paper
player = input("Please choose rock, scissors, or paper?")

print('你选择了' + player + '，计算机选择了' + computer + '。')

# Check the guess
if computer == 'rock':
    if player == 'rock':
        print("平局！")
    elif player == 'scissors':
        print("你输了！")
    elif player == 'paper':
        print("你赢了！")
elif computer == 'scissors':
    if player == 'scissors':
        print("平局！")
    elif player == 'paper':
        print("你输了！")
    elif player == 'rock':
        print("你赢了！")
elif computer == 'paper':
    if player == 'paper':
        print("平局！")
    elif player == 'rock':
        print("你输了！")
    elif player == 'scissors':
        print("你赢了！")
