from math import sqrt


def euclidean_distance(preferences, person1, person2):
    items_in_each = {}
    for item in preferences[person1]:
        if item in preferences[person2]:
            items_in_each[item] = 1
    if len(items_in_each) == 0:
        return 0
    else:
        sum_of_squares = 0
        for item in items_in_each:
            sum_of_squares = sum_of_squares + pow(preferences[person1][item] - preferences[person2][item], 2)
        return 1/(1 + sqrt(sum_of_squares))


def pearson_coefficient(preferences, person1, person2):
    items_in_each = {}
    for item in preferences[person1]:
        if item in preferences[person2]:
            items_in_each[item] = 1
    number_of_elems = len(items_in_each)
    if number_of_elems == 0:
        return 0
    else:
        person1_pref_sum = sum(preferences[person1][item] for item in items_in_each)
        person2_pref_sum = sum(preferences[person2][item] for item in items_in_each)
        person1_pow_pref_sum = sum(pow(preferences[person1][item], 2) for item in items_in_each)
        person2_pow_pref_sum = sum(pow(preferences[person2][item], 2) for item in items_in_each)
        multiplied_person1_person2_prefs_sum = sum(preferences[person1][item] * preferences[person2][item] for item in items_in_each)

        value = multiplied_person1_person2_prefs_sum - ((person1_pref_sum * person2_pref_sum)/number_of_elems)
        density = sqrt((person1_pow_pref_sum - pow(person1_pref_sum, 2)/number_of_elems) *
                       (person2_pow_pref_sum - pow(person2_pref_sum, 2)/number_of_elems))

        if density == 0:
            return 0
        else:
            return value/density


def top_matches(preferences, person, calculator):
    scores = [(calculator(preferences, person, other_person), other_person) for other_person in preferences if other_person != person]
    scores.sort(reverse=True)
    return scores


def get_recommendations(preferences, person, calculator):
    totals = {}
    sim_sums = {}
    for other_person in preferences:
        if other_person != person:
            similarity = calculator(preferences, person, other_person)
            if similarity > 0:
                for item in preferences[other_person]:
                    if item not in preferences[person] or preferences[person][item] == 0:
                        totals.setdefault(item, 0)
                        totals[item] += preferences[other_person][item] * similarity
                        sim_sums.setdefault(item, 0)
                        sim_sums[item] += similarity
    rankings = [(total/sim_sums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    return rankings


def transform_preferences(preferences):
    result = {}
    for person in preferences:
        for item in preferences[person]:
            result.setdefault(item, {})
            result[item][person] = preferences[person][item]
    return result
