
from time import sleep
import os 

filename = os.path.dirname(os.path.realpath(__file__))
file_encode = '.txt'

problems_dict = dict()


# Get user numbers
problems_amount = int(input("How many numbers?\n> "))
for num in range(1, problems_amount+1):
    problems_dict[num] = input(f"{num}. ").upper()
    

def get_all_problems(func_dict: dict, row: int=3) -> str:
    """get all the problems
    Args:
        func_dict (dict): the dict full of numbers and answers
        row (int, optional): Amount of rows. Defaults to 3.

    Returns:
        str: returns a row column of all answers.
    """
    keys = list(func_dict.keys())
    cols = round(len(func_dict) / row)
    s = ''
    for c in range(1, cols + 1):
        j = c
        for r in range(1, row + 1):
            try:
                d = func_dict[keys[j - 1]] # The data
                if d != 'Score' : # If it's score, don't store it 
                    s += str(j) + '. ' # To number
                    s += str(d).ljust(6)
                    j += cols
            except IndexError as e:
                print(str(e))
                break
        s += '\n' 
    return (s)
        

while True:
    user_choice = input("Save, Input false problems, or look at answers?\n> ")
    if user_choice == '0' or user_choice == 'save':
        save_as = input("Save as what name?\n> ")
        if not save_as:
            save_as = 'Untitled'
        new_filename = filename + '\\' + save_as + file_encode
        with open(new_filename, 'a') as f:
            for k, v in problems_dict.items():
                if str(k) != 'Score':
                    f.write(f"{str(k)}. {v}\n")
                    continue
                f.write(f"\n{k}: {v}")
        print('Saved')
    elif user_choice == '1' or user_choice == 'input':
        wrongs = 0
        while True:
            try:
                false_problems = input("Enter number and correct answer [3, A]. Enter 'done' once you're done:\n> ")
                if false_problems == 'done':
                    break
                false_problems = false_problems.split(', ')
                problems_dict[int(false_problems[0])] += f" x {false_problems[1].upper()}" # example: A x B
                wrongs += 1
                amount = len(problems_dict)
                calc = ((amount - wrongs)/amount) * 100
                print(f"Your score is: {calc}, {wrongs}/{amount} of wrong numbers.")
                problems_dict['Score'] = f"{calc}, {wrongs}/{amount} salah" # Add to dictionary
            except Exception as e:
                print("ERROR: " + str(e))
    elif user_choice == '2' or user_choice == 'look':
        while True:
            num = input("Which number? Enter 'done' once you're done, or 'all' to see all numbers.\n> ")
            if num == 'done':
                break
            if num == 'all':
                print(get_all_problems(problems_dict))
                break
            try: # Means user inputted a number
                print(num + '. ', problems_dict[int(num)])
            except Exception as e:
                print("ERROR: " + str(e))
    elif user_choice == 'done':
        print("Thank you. Program will close in 1 minute.")
        sleep(60)
        
