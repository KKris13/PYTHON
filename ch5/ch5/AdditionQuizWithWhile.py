import random 

# Generate random numbers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# Prompt the user to enter an answer
answer = eval(input(str(number1) + " + " + str(number2) + "="))
    
# Display result
while number1 + number2 != answer:
    answer = eval(input('答案错误！请重新作答：'))
print('答案正确！')
