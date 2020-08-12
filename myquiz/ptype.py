#!/usr/bin/env python3

 # welcome title
print("Quiz Are you a  Extrovert or introvert?")
print("")

 # initialize vars to keep score
countA = 0
countB = 0

 # Q1  # ========================================================================

Q1= "Q1: The more you socialize, the more energized you feel."
R1= "a. true\nb. false\n"

print(Q1)
print(R1)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q2 # ========================================================================
Q2= "Q2:  Are you usually rather"
R2= "a. Quick to agree to a time\nb. Reluctant to agree to a time"
  
print(Q2)
print(R2)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1
  
 # Q3 # ========================================================================
Q3= "Q3:  As a student, do you prefer"
R3= "a. Participate in a lively discussion\nb. Listen to an interesting lecture"

print(Q3)
print(R3)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q4 # ========================================================================
Q4= "Q4: You are more likely to select an option with higher risk"
R4= "a. true\nb. false"

print(Q4)
print(R4)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q5 # ========================================================================
Q5= "Q5:  you Netflix genre do you prefer?"
R5= "a. sci-fi\nb. action"

print(Q5)
print(R5)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

 # Q6 # ========================================================================
Q6= "Q6:  Your ideal work environment includes?"
R6a= "a. one that incentivizes your hard work with reward."
R6b= "b. one that offers more autonomy to complete tasks with little oversight"

print(Q6)
print(R6a)
print(R6b)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q7 # ========================================================================
Q7= "Q7:  During group brain storming sessions - ideation comes naturally to you"
R7= "a. true\nb. false"

print(Q7)
print(R7)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1
 
 # Q8 # ========================================================================
Q8= "Q8:  You see a co-worker is visibly upset. What is your next move"
R8= "a. engage and see if you can help\nb. Walk pass as if you didnt notice"

print(Q8)
print(R8)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q9 # ========================================================================
Q9= "Q9: It is easier finding your true-self with which platform?"
R9= "a. more traditional in-person interactions\nb. online"

print(Q9)
print(R9)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q10 # ========================================================================
Q10= "Q10:  you are busy at work and co-worker is telling you their life story. You:"
R10= "a. let them continue but tune out 50%\nb. interupt to inform them you are busy"

print(Q10)
print(R10)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1

 # Q11 # ========================================================================
Q11= "Q11:  you perform better when a task has a set deadline"
R11= "a. true\nb. false"

print(Q11)
print(R11)

response = input().lower()

while response  not in ("a", "b"):
    print("please select a or b")
    break

if response == "a":
    countA += 1
else:
    countB += 1
 
 # display results  # ========================================================================

print("")
if countA > 4:
    print("you have a tendency toward introversion")
else:
    print("you have a tendency toward extroversion")

print("")





