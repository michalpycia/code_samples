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
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)  # podzielenie ciagu na dwie czescie (przed Dx i po)
            except ValueError:
                return 'wrong input'
            dice_value = int(dice[1:])  # D6 - przypisanie 6 jako int
            break
    else:
        return 'Wrong input'
    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return 'Wrong input'
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return 'Wrong input'
    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


def game_2001_mod():
    user_score = 0
    ai_score_ = 0
    rounds = 1
    while user_score <= 2000 or ai_score <= 2000:
        print(f'Numer rundy: {rounds}')
        score = 0
        ai_score = 0
        for _ in range(2):
            user_dice = input('Wpisz rodzaj kostki: D100 / D20 / D12 / D10 / D8 / D6 / D4 / D3: ')
            score += (roll_the_dice(user_dice))
        if score == 7 and rounds >= 2:
            score = int(score / 7)
        elif score == 11 and rounds >= 2:
            score = score * 11
        else:
            print(f'Wyrzuciles: {score}')
            user_score += score
        for _ in range(2):
            ai_dice = roll_the_dice(random.choice(POSSIBLE_DICES))
            ai_score += ai_dice
        if ai_score == 7 and rounds >= 2:
            ai_score = int(score / 7)
        elif ai_score == 11 and rounds >= 2:
            ai_score = ai_score * 11
        else:
            print(f'Komputer wyrzucil: {ai_score}')
            ai_score_ += ai_score
        rounds += 1
        print(f'Wynik komputera: {ai_score} Twój wynik: {user_score}')


if __name__ == '__main__':
    game_2001_mod()
