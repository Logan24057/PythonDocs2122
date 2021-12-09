import random
number=random.randint(0,4)
answerList=['Yes', 'No', 'what?', ' uh okay...', 'absolutely not']
userQuestion=input('Ask a question. ')
print(answerList[number])
