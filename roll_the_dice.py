import random

POSSIBLE_DICES = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)


def roll_the_dice(dice_code):
    """
    Program to simulate rolling the Dice from user input.
    Example correct user input:
    2D10+10 - Rolling two 10 sided dices and adding 10 to result
    D12-1   - Rolling two 12 sided dices and subtract 1 from result.
    Returns:
        integer: value.
    """
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)  # split code with dice type
            except ValueError:  # inform user that string provided did not match any dice
                return 'wrong input'
            dice_value = int(dice[1:])
            break
    else:
        return 'Wrong input'
    try:
        multiply = int(multiply) if multiply else 1  # checking how many throws, if not provided: = 1
    except ValueError:
        return 'Wrong input'  # checking if value before dice type is integer
    try:
        modifier = int(modifier) if modifier else 0  # checking if user provided value which should be added/subtract
    except ValueError:
        return 'Wrong input'
    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
