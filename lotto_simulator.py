import random


def random_lotto():
    """
    Function to create list of integers in range 1 - 49,
    shuffle elements of the list
    Returns:
        list: six randomly drawn numbers in range 1 - 49
    """
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    result = numbers[:6]
    return result


def ask_for_number(lst):
    """
    Function to ask user for 6 numbers in range 1 - 49
    Returns:
        list: six elements, integers in range 1 -49
    """
    while True:
        try:
            number = int(input("Provide a number between 1 - 49 "))  # ask user for number
        except ValueError:
            print(" Please enter a integer value")  # inform user that value must be integer
        else:
            if number not in range(1, 50) or number in lst:
                print("Number already on the list or out of range")
                print(lst)
                ask_for_number(lst)  # ask for another number
            else:
                lst.append(number)  # add number to the list
                print(lst)
                print("Correct, number added to list")
                return lst
        print(lst)


def lst_compare(userlist, ailist):
    """
    Funtion to compare user numbers and randomly drawn numbers
    Returns:
         list: list of scored numbers
    """
    duplicates = []
    for i in userlist:
        if i in ailist:
            duplicates.append(i)
    return duplicates


def score(score):
    """
    Funtion to inform user about score
    Returns:
        string: score information
    """
    if len(score) < 3:
        return ("No win, scored less than 3 numbers")
    elif len(score) == 3:
        return ("3 numbers scored!")
    elif len(score) == 4:
        return ("4 numbers scored!")
    elif len(score) == 5:
        return ("5 numbers scored!")
    elif len(score) == 6:
        return ("6 numbers scored! Millionaire!")


ai_numbers = random_lotto()
user_number = []

while len(user_number) <= 5:
    ask_for_number(user_number)
user_number.sort()
print('Your numbers:')
print(user_number)
scored_numbers = lst_compare(user_number, ai_numbers)
print(f'Randomly drawn numbers:\n{ai_numbers}')

if len(scored_numbers) >= 1:
    print(f'Scored numbers: {scored_numbers}')
else:
    print("No scored numbers")

print(score(scored_numbers))
