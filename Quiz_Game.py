print("Welcome to My Computer Game")

playing = input("Do you want to Play?" )

if playing.lower() != "yes":
    quit()

print("Ok !Lets Playing : )")
score = 0

answer = input("How many beers you can drink?")
if answer  == ("0"):
    print("Correct!")
    score += 1
else:
   print("Incorrect! Neku antha scene ledu lanja")

answer = input("Are you Virgin? ")
if answer.lower() == ("yes"):
    print("edi maku telusu le")
    score += 1
else:
   print("chivariki oppukunnavu! ")

answer = input("eppati daka enni kathalu ayinayi? ")
if answer == ("1"):
    print("Correct!")
    score += 1
else:
   print("Incorrect! Neku antha Scene Ledu lanja!")

answer = input("nee brathuku lo eppudu aina okadivi beer koni tagava?")
if answer.lower() == ("no"):
    print("Correct! Chivariki oppukunnavu")
    score +=1
else:
   print("Incorrect! nee mokaniki antha scene ledu!")

answer = input("neku takita takita work avutunda?")
if answer.lower() == ("yes"):
    score +=1
    print("Correct ! but neku antha scene unda?")
else:
   print("InCorrect! Chivariki oppukunnavu!")

print("Congratulations Lanja! " + str(score) + " questions correct")
print("Congratulations Lanja! " + str((score / 5) * 100) + "%.")