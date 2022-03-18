
from time import sleep
import os 

filename = os.path.dirname(os.path.realpath(__file__))  # Change your directory here.
file_encode = '.txt'

problems_dict = dict()

problems_amount = int(input("How many problems?\n> "))
for num in range(1, problems_amount+1):
    problems_dict[num] = input(f"{num}. ").upper()
    
while True:
    user_choice = input("Save, Input false problems, or look at answers?\n> ")
    if user_choice == '0':
        save_as = input("With what name should it be saved?\n> ")
        new_filename = filename + '\\' + save_as + file_encode
        with open(new_filename, 'a') as f:
            for k, v in problems_dict.items():
                f.write(f"{str(k)}. {v}\n")
        print('Saved')
    elif user_choice == '1':
        wrongs = 0
        while True:
            false_problems = input("Enter number and correct answer [3, A]. Enter 'done' once you're done:\n> ")
            if false_problems == 'done':
                break
            false_problems = false_problems.split(', ')
            try:
                problems_dict[int(false_problems[0])] += f" x {false_problems[1].upper()}"
                wrongs += 1
            except Exception as e:
                print("ERROR: " + str(e))
        amount = len(problems_dict)
        calc = ((amount - wrongs)/amount) * 100
        print(f"You got score: {calc}, {wrongs}/{amount} wrong answers.")
        problems_dict['Score'] = f"{calc}, {wrongs}/{amount} wrong."
    elif user_choice == '2':
        while True:
            num = input("Which number? Enter 'done' once you're done.\n> ")
            if num == 'done':
                break
            print(num + '. ', problems_dict[int(num)])
    elif user_choice == 'done':
        sleep(300)
