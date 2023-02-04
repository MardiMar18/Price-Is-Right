                 # Task # 1:
import random

""" def guess_random_number (tries, start, stop):

    num = random.randint(start,stop)

    while tries != 0:
        print(f"Number of tries remaining: {tries}")
        guess = int(input("Guess a number between 0 and 10."))

        if guess < num: 
            print("Guess Higher!")
        elif guess > num:
            print("Guess lower!")
        else:
            print("You guessed the correct number!")
            return 
        tries = tries -1

        if tries == 0:
            print(f"You have failed to guess the number: {num}")
            break 

guess_random_number(5,0,10) """

                 # Task #2 :
"""  
def guess_random_num_linear (tries,start,stop):
    num = random.randint(start,stop)
    print(f"The Target Number program is...{num}")

    for guess in range(start, stop +1):
        print(f"The program is guessing...{guess}")

        if guess != num:

            tries = tries -1
            print("The program guessed incorrectly.")
            print (f"The number of tries left: {tries}")

            if tries == 0:
                print("Your dumb program is no match againts the human intelect!")
                return 
        
        elif guess == num:
            print("BOW DOWN HUMANS! The program guessed the target number!")
            break 

guess_random_num_linear(5,0,10)
"""  
        
                 # Task #3 :
                 
def guess_random_num_binary (tries, start, stop): 
    num = random.randint(start,stop)
    print(f"The Target Number program is...{num}")


    lower_bound = start 
    upper_bound = stop 

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot 
        tries -= 1
    
        if tries <= 0:
            print("Your dumb program is no match againts the human intelect!")
            return 

        if pivot_value == num:
            print("BOW DOWN HUMANS! The program guessed the target number!")
            return
            
        elif pivot_value > num:
            upper_bound = pivot -1 
            print("Guessing Lower!")
            continue

        else:
            lower_bound = pivot +1
            print("Guessing Higher!")
            continue 

    return -1 

guess_random_num_binary(5,0,100)