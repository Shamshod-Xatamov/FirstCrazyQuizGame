import sys
print('                      Welcome all student to the final exam❤️ ')
print('You will be given 3 questions in total. If you find more than 2,you can pass the exam successfully')
start=input("To start the test enter 'START' keyword: ")
if start.upper()=='START':
    from questions import obj1
else:
    print('Invalid keyword!!!')
    sys.exit()
correct=0
n=1
b=3
for i in range(3):
    response=obj1.game()
    print(n,'Q.',response)
    n=n+1

    answer=input('Enter your answer: ')

    if answer.capitalize()==obj1.quiz_questions[response]:
        print('Correct')
        correct=correct+1
    else:
        print('No Worries!😊')

    b=b-1
    if b!=0:
        print(f'{b} questions left')


    del obj1.quiz_questions[response]

if correct>=2:
    print('You passed the exam and the number of correct answers:',correct)
else:
    print('You failed the exam Sotak!')
