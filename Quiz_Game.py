questions = ["1.Which planet is closest to the sun?",
             "2.What is the hardest natural substance on Earth?",
             "3.What is the largest ocean on Earth?",
             "4.How many states are there in India?",
             "5.How many bones are in the adult human body?"]

options = ["A.Jupiter\nB.Mercury\nC.Venus\nD.Mars",
           "A.Gold\nB.Copper\nC.Steel\nD.Diamond",
           "A.Indian Ocean\nB.Atlantic Ocean\nC.Pacific Ocean\nD.Bay of Bengal",
           "A.28\nB.31\nC.29\nD.30",
           "A.308\nB.208\nC.206\nD.315"]

answer = ["B","D","C","A","C"]

def  quiz():
    print("***** Welcome to Quiz Game *****")
    score = 0
    totalquestions = len(questions)

    for q,opt,ans in zip(questions,options,answer):
        print(q)
        print(opt)
        

        while True:
            guess = input("Enter your choice (A/B/C/D) : ").upper()
            if guess in ['A','B','C','D']:
                break
            else:
                print("INVALID CHOICE!")

        if (guess == ans):
            print("CORRECT!\n")
            score+=1
        else:
            print(f"WRONG!,The Correct Answer is {ans}\n")   


    percentage = round((score/totalquestions)*100)
    print(f"Your Percentage is {percentage}")
    if (percentage == 100):
        print("Fantastic! You are a Genius")
    elif(80<=percentage<100):
        print("Superb! It was Close")
    elif(60<=percentage<80):
        print("Good!Do a Lot of Practice")
    else:
        print("Poor!Need a lot Work")            
            

while True:
    quiz()

    replay = input("Do you want to Play Again? (Y-Yes/N-No)").upper()

    if replay == 'N':
        print("Thanks for Playing!")
        break

                         



