# /!\ Python Version must be greater than 3.10

# CONSTANT

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def type_of_hand(hand):
    headcount = {}

    for c in hand:
        if c in headcount:
            headcount[c] += 1
        else:
            headcount[c] = 1

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


def superior(hand1, hand2):
    """ Test if hand1 is stronger than hand2 """

    type1 = type_of_hand(hand1)
    type2 = type_of_hand(hand2)

    value_converter = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    if type1 > type2:
        return True
    elif type1 == type2:
        i = 0

        while i < 5 and hand1[i] == hand2[i]:
            i += 1

        return value_converter[hand1[i]] > value_converter[hand2[i]]
    else:
        return False


def buble_sort(data):
    for k in range(len(data)):
        for i in range(k - 1, -1, -1):
            if superior(data[i][0], data[i + 1][0]):
                data[i], data[i + 1] = data[i + 1], data[i]                


data = list(map(lambda x: x.replace('\n', '').split(' '), open("2023/day7/input.txt", 'r').readlines()))
sumup = 0

buble_sort(data)

for i in range(len(data)):
    print(type_of_hand(data[i][0]), data[i][0])

    sumup += (i + 1) * int(data[i][1])

print(sumup)
