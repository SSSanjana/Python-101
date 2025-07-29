scores = {"GRYFFINDOR": 0, "HUFFLEPUFF": 0, "RAVENCLAW": 0, "SLYTHERIN": 0}

DD = int(input("Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk\n> "))
if DD == 1:
    scores["GRYFFINDOR"] += 1
    scores["RAVENCLAW"] += 1
elif DD == 2:
    scores["HUFFLEPUFF"] += 1
    scores["SLYTHERIN"] += 1
else:
    print("Wrong input for Q1; no points added.")

ques2 = int(input(
    "Q2) When I’m dead, I want people to remember me as: \n"
    "1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n> "
))
if ques2 == 1:
    scores["HUFFLEPUFF"] += 2   # The Good
elif ques2 == 2:
    scores["SLYTHERIN"] += 2    # The Great
elif ques2 == 3:
    scores["RAVENCLAW"] += 2    # The Wise
elif ques2 == 4:
    scores["GRYFFINDOR"] += 2   # The Bold
else:
    print("Wrong input for Q2; no points added.")


QUES3 = int(input(
    "Q3) Which kind of instrument most pleases your ear?\n"
    "1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n> "
))
if QUES3 == 1:
    scores["SLYTHERIN"] += 4
elif QUES3 == 2:
    scores["HUFFLEPUFF"] += 4
elif QUES3 == 3:
    scores["RAVENCLAW"] += 4
elif QUES3 == 4:
    scores["GRYFFINDOR"] += 4
else:
    print("Wrong input for Q3; no points added.")

print("\nResults:")
print("SLYTHERIN:  ", scores["SLYTHERIN"])
print("HUFFLEPUFF: ", scores["HUFFLEPUFF"])
print("RAVENCLAW:  ", scores["RAVENCLAW"])
print("GRYFFINDOR: ", scores["GRYFFINDOR"])
