import random
name = 'Bill'
question = "Am i real?"
answer = ""
random_number = random.randint(1,9)

#control flow
if random_number == 1:
  answer = "Yes-definitely"
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = "Error"

# Name check
if name == "":
  print('Question: ' + question)
else:
  print(name + ' asks: '+ question)

# Question Check
if question =='':
  print('NO question, NO fortune!')
else:
  print("Magic 8-ball's answer: " + answer)
