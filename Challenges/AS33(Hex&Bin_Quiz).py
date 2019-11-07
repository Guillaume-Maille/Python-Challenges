################################################################################################

import random
x = 0   # For random # generation
t = 0   # Counts the # of questions answered
s = 0   # Your Score
sc = 0  # Counts how many times you have skipped a question
print("You will have a total of 10 questions.")
print("Do NOT answer using capital letters or you will get the question wrong.")
print("Should you want to skip a question answer with 'SKIP'.")
print("Do not type any '0' that are at the front of the Binary number.")
print("eg: 00101011 should be type out as 101011.")
print("________________________________________________________________________________________")

################################################################################################

print("                                                                                        ")
print("                            Converting Binary to Hexadecimal                            ")
print("                                                                                        ")
print("________________________________________________________________________________________")

################################################################################################

while True:
    if t > 4:
        break
    else:
        x = random.randint(1, 255)
        print("")
        print("Question (", t + 1, ")")
        print("________________________")
        print("Binary number to turn into Hexadecimal:")
        print(bin(x)[2::])
        a = input("Answer:")
        if a == "SKIP":
            sc += 1
            print("")
            print("")
            print("Question Skipped!")
            print("")
            print("SCORE:", s)
            print("Questions skipped:", sc)
        else:
            if a == hex(x)[2::]:
                s += 1
                print("")
                print("")
                print("Correct!")
                print("")
                print("SCORE:", s)
                print("Questions skipped:", sc)
                t += 1
            else:
                print("")
                print("")
                print("The answer was", hex(x)[2::])
                print("")
                print("SCORE:", s)
                print("Questions skipped:", sc)
                t += 1
t = 0
################################################################################################

print("                                                                                        ")
print("                            Converting Hexadecimal to Binary                            ")
print("                                                                                        ")
print("________________________________________________________________________________________")

################################################################################################

while True:
    if t > 4:
        break
    else:
        x = random.randint(1, 255)
        print("")
        print("Question", t + 6)
        print("________________________")
        print("Hexadecimal number to turn into Binary:")
        print(hex(x)[2::])
        a = input("Answer:")
        if a == "SKIP":
            sc += 1
            print("")
            print("")
            print("Question Skipped!")
            print("")
            print("SCORE:", s)
            print("Questions skipped:", sc)
            t -= 1
        else:
            if a == bin(x)[2::]:
                s += 1
                print("")
                print("")
                print("Correct!")
                print("")
                print("SCORE:", s)
                print("Questions skipped:", sc)
                t += 1
            else:
                print("")
                print("")
                print("The answer was", bin(x)[2::])
                print("")
                print("SCORE:", s)
                print("Questions skipped:", sc)
                t += 1

################################################################################################

print("_________________________________________________________________________________________________________________")
print("_________________________________________________________________________________________________________________")
print("_________________________________________________________________________________________________________________")

################################################################################################

print("Well Done! You have completed the quiz!")
print("")
print("Total Score:", s)
print("# of Questions Skipped:", sc)
