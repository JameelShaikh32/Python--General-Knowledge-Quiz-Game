#Q1 Which is the biggest continent in the world?
a1 = 'Asia'
#Q2 Which is longest river in the world?
a2 = 'Nile'
#Q3 Which is the largest Ocean in the world?
a3 = 'Pacific Ocean'
#Q4 Which is India's first super computer?
a4 = 'Param8000'
#Q5 Which is largest animal on land?
a5 = 'African Elephant'
#Q6 Which is largest animal in the world?
a6 = 'Blue Whale'
#Q7 Which is largest island in the world?
a7 = 'Greenland'
#Q8 Which is largest flower in the world?
a8 = 'Rafflesia'
#Q9 Which is the 29th state of India?
a9 = 'Telangana'
#Q10 Which is largest desert in the world?
a10 = 'Sahara'

def authenticate():
    pwd = ''
    attempt = 0
    while (pwd != "2345") and (attempt < 3):
        pwd = input("Enter Password: ")
        attempt = attempt + 1
        if pwd != '2345':
            print("Invalid Password! Try Again")

        if attempt == 3:
            print("Sorry! You have reached maximum number of attempts")
            break

        if (pwd == '2345'):
            answers()
        
    

def startGame():
    q1 = input("\nQ1. Which is the biggest continent in the world?\nAns: ")
    q2 = input("\nQ2. Which is longest river in the world?\nAns: ")
    q3 = input("\nQ3. Which is the largest Ocean in the world?\nAns: ")
    q4 = input("\nQ4. Which is India's first super computer?\nAns: ")
    q5 = input("\nQ5. Which is largest animal on land?\nAns: ")
    q6 = input("\nQ6. Which is largest animal in the world?\nAns: ")
    q7 = input("\nQ7. Which is largest island in the world?\nAns: ")
    q8 = input("\nQ8. Which is largest flower in the world?\nAns: ")
    q9 = input("\nQ9. Which is the 29th state of India?\nAns: ")
    q10 = input("\nQ10. Which is largest desert in the world?\nAns: ")

    if q1 == 'Asia':
        print("Answer 1 is Correct\n")
    else:
        print("Answer 1 in Incorrect\n")

    if q2 == 'Nile':
        print("Answer 2 is Correct\n")
    else:
        print("Answer 2 in Incorrect\n")

    if q3 == 'Pacific Ocean':
        print("Answer 3 is Correct\n")
    else:
        print("Answer 3 in Incorrect\n")

    if q4 == 'Param8000':
        print("Answer 4 is Correct\n")
    else:
        print("Answer 4 in Incorrect\n")

    if q5 == 'African Elephant':
        print("Answer 5 is Correct\n")
    else:
        print("Answer 5 in Incorrect\n")

    if q6 == 'Blue Whale':
        print("Answer 6 is Correct\n")
    else:
        print("Answer 6 in Incorrect\n")

    if q7 == 'Greenland':
        print("Answer 7 is Correct\n")
    else:
        print("Answer 7 in Incorrect\n")

    if q8 == 'Rafflesia':
        print("Answer 8 is Correct\n")
    else:
        print("Answer 8 in Incorrect\n")

    if q9 == 'Telangana':
        print("Answer 9 is Correct\n")
    else:
        print("Answer 9 in Incorrect\n")

    if q10 == 'Sahara':
        print("Answer 10 is Correct\n")
    else:
        print("Answer 10 in Incorrect\n")


    print("Do you want to display Answers? Y/N")
    opt = input()
    if opt == 'Y':
        authenticate()
    else:
        print("OK")
        print("Do you want to play again? Y/N")
        opt2 = input()
        if opt2 == 'Y':
            startGame()
        else:
            print("OK Byeee...")
        
    
    

def answers():
    print("\nQ1 Which is the biggest continent in the world?")
    print("Answer: Asia")
    print("\nQ2 Which is longest river in the world?")
    print("Answer = Nile")
    print("\nQ3 Which is the largest Ocean in the world?")
    print("Answer = Pacific Ocean")
    print("\nQ4 Which is India's first super computer?")
    print("Answer = Param8000")
    print("\nQ5 Which is largest animal on land?")
    print("Answer = African Elephant")
    print("\nQ6 Which is largest animal in the world?")
    print("Answer = Blue Whale")
    print("\nQ7 Which is largest island in the world?")
    print("Answer = Greenland")
    print("\nQ8 Which is largest flower in the world?")
    print("Answer = Rafflesia")
    print("\nQ9 Which is the 29th state of India?")
    print("Answer = Telangana")
    print("\nQ10 Which is largest desert in the world?")
    print("Answer = Sahara")

    print("Do you want to play the quiz again? Y/N")
    playagain = input()
    if playagain == 'Y':
        startGame()
    else:
        print("OK Byeee...")
        


st = input("Type 'start' to start the game\n> ")

if st == 'start':
    startGame()
else:
    print("Byeee..")
    








    
    
