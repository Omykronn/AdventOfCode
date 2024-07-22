from toolbox.sort import bubbleSort


FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def bestTypeOfHand(hand: str) -> int:
    """
    Returns the best type of hand if there are jokers
    """
    headcount = {}

    for c in hand:
        if c in headcount:
            headcount[c] += 1
        else:
            headcount[c] = 1

    # Choosing which card a joker should be (the criterion is the card with higher occurence)
    # More precisiely, this loop is not run if there is only Jokers, because it's already one of the strongest hand
    if 'J' in headcount and len(headcount) > 1:
        max_value = 0
        max_key = 'J'

        for key in headcount:
            if key != 'J' and max_value < headcount[key]:
                max_value = headcount[key]
                max_key = key

        headcount[max_key] += headcount['J']
        headcount.pop('J')

    match len(headcount):
        case 1:
            return FIVE_OF_A_KIND
        case 2:
            if 3 in headcount.values():
                return FULL_HOUSE
            else:
                return FOUR_OF_A_KIND
        case 3:
            if 3 in headcount.values():
                return THREE_OF_A_KIND
            else:
                return TWO_PAIR
        case 4:
            return ONE_PAIR
        case 5:
            return HIGH_CARD

def superior(hand1: (str, str), hand2: (str, str)) -> bool:
    """ Test if hand1 is stronger than hand2 """

    hand1 = hand1[0]
    hand2 = hand2[0]

    type1 = bestTypeOfHand(hand1)
    type2 = bestTypeOfHand(hand2)

    value_converter = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': -1, 'Q': 10, 'K': 11, 'A': 12}

    if type1 > type2:
        return True
    elif type1 == type2:
        i = 0

        while i < 5 and hand1[i] == hand2[i]:
            i += 1

        return value_converter[hand1[i]] > value_converter[hand2[i]]
    else:
        return False 

def prepare(src: str) -> [(str, str)]:
    """
    Import data from a file, and format them
    """

    with open(src, 'r') as file:
        data = [line.replace('\n', '').split(' ') for line in file.readlines()]

    return data

def solve(data: [(str, str)]) -> int:
    """
    Determine the flag of data
    """

    counter = 0

    bubbleSort(data, superior)

    for i in range(len(data)):
        counter += (i + 1) * int(data[i][1])

    return counter
