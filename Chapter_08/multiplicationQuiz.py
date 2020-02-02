'''
Chapter 8 Input Validation

Write Your Own Multiplication Quiz

To see how much PyInputPlus is doing for you, try re-creating the 
multiplication quiz project on your own without importing it. This program will
prompt the user with 10 multiplication questions, ranging from 0 × 0 to
9 × 9. You’ll need to implement the following features:
•	 If the user enters the correct answer, the program displays “Correct!”
for 1 second and moves on to the next question.
•	 The user gets three tries to enter the correct answer before the
program moves on to the next question.
•	 Eight seconds after first displaying the question, the question is
marked as incorrect even if the user enters the correct answer after
the 8-second limit

'''

import random, time

numberOfQuestions = 10
tries = 3
starttime = 0
correctAnswers = 0
i = 0

for questionNumber in range(numberOfQuestions):
    multiplier = random.randint(0,9)
    multiplicand = random.randint(0,9)

    result = multiplier * multiplicand

    while(tries > 0):

        if(starttime == 0):
            starttime = time.time()

        while(True):
            answer = input(f'{questionNumber+1}: {multiplier} * {multiplicand} = ? ')
            try:
                answer = int(answer)
                break
            except ValueError:
                print('Not a number, please try again')

        if(answer == result):
            print('Correct!')
            correctAnswers += 1
            time.sleep(1)
            break
        elif((time.time()-starttime)>=8):
            print('Time\'s up.')
            break
        else:
            print('Incorrect, try again!')
            tries -= 1
    questionNumber += 1

time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))