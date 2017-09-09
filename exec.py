from critics import critics
from recomendations import euclidean_distance, pearson_distance, top_matches

person1 = 'Lisa Rose'
person2 = 'Gene Seymour'

euclidean_dist = euclidean_distance(critics, person1, person2)
pearson_dist = pearson_distance(critics, person1, person2)

print('euclidean distance between {0} and {1} = {2}'.format(person1, person2, euclidean_dist))
print('pearson distance between {0} and {1} = {2}'.format(person1, person2, pearson_dist))

euclidean_distance_top_matches_for_person1 = top_matches(critics, person1, euclidean_distance)
pearson_distance_top_matches_for_person1 = top_matches(critics, person1, pearson_distance)

print('top matches using euclidean distance for {0} = {1}'.format(person1, euclidean_distance_top_matches_for_person1))
print('top matches using pearson distance for {0} = {1}'.format(person1, pearson_distance_top_matches_for_person1))
