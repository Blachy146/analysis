from math import sqrt


def distance(preferences, person1, person2):
    items_in_each = {}
    for item in preferences[person1]:
        if item in preferences[person2]:
            items_in_each[item] = 1
    if len(items_in_each) == 0:
        return 0
    else:
        sum_of_squares = 0
        for item in items_in_each:
            sum_of_squares += pow(preferences[person1][item] - preferences[person2][item], 2)
            print(sum_of_squares)

        return 1/(1 + sqrt(sum_of_squares))

