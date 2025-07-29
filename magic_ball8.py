import random

question = str(input("question: "))

answer = random.randint(0,8)

if answer == 0:
  print("Magic 8 Ball: Yes - definitely.")
elif answer == 1:
  print("Magic 8 Ball: It is decidedly so.")
elif answer == 2:
  print("Magic 8 Ball: Without a doubt.")
elif answer == 3:
  print("Magic 8 Ball: Reply hazy, try again.")
elif answer == 4:
  print("Magic 8 Ball: Ask again later.")
elif answer == 5:
  print("Magic 8 Ball: Better not tell you now.")
elif answer == 6:
  print("Magic 8 Ball: My sources say no.")
elif answer == 7:
  print("Magic 8 Ball: Outlook not so good.")
else:
  print("Magic 8 Ball: Very doubtful.")


