from critics import critics
from recomendations import *

person1 = 'Toby'
person2 = 'Gene Seymour'
movie1 = 'Cale szczescie'

euclidean_dist = euclidean_distance(critics, person1, person2)
pearson_dist = pearson_coefficient(critics, person1, person2)

print('euclidean distance between {0} and {1} = {2}'.format(person1, person2, euclidean_dist))
print('pearson coefficient between {0} and {1} = {2}'.format(person1, person2, pearson_dist))

euclidean_distance_top_matches_for_person1 = top_matches(critics, person1, euclidean_distance)
pearson_coefficient_top_matches_for_person1 = top_matches(critics, person1, pearson_coefficient)

print('top matches using euclidean distance for {0} = {1}'.format(person1, euclidean_distance_top_matches_for_person1))
print('top matches using pearson coefficient for {0} = {1}'.format(person1, pearson_coefficient_top_matches_for_person1))

euclidean_distance_recommendations_for_person1 = get_recommendations(critics, person1, euclidean_distance)
pearson_coefficient_recommendations_for_person1 = get_recommendations(critics, person1, pearson_coefficient)

print('recommendations using euclidean distance for {0} = {1}'.format(person1, euclidean_distance_recommendations_for_person1))
print('recommendations using pearson coefficient for {0} = {1}'.format(person1, pearson_coefficient_recommendations_for_person1))

movies = transform_preferences(critics)

print('movies = {0}'.format(movies))

movies_similar_to_movie1_euclidean_distance = top_matches(movies, movie1, euclidean_distance)
movies_similar_to_movie1_pearson_coefficient = top_matches(movies, movie1, pearson_coefficient)

print('movies similar to {0} using euclidean distance = {1}'.format(movie1, movies_similar_to_movie1_euclidean_distance))
print('movies similar to {0} using pearson coefficient = {1}'.format(movie1, movies_similar_to_movie1_pearson_coefficient))

recommended_critics_for_movie1_euclidean_distance = get_recommendations(movies, movie1, euclidean_distance)
recommended_critics_for_movie1_pearson_coefficient = get_recommendations(movies, movie1, pearson_coefficient)

print('recommended critics for {0} using euclidean_distance = {1}'.format(movie1, recommended_critics_for_movie1_euclidean_distance))
print('recommended critics for {0} using pearson_coefficient = {1}'.format(movie1, recommended_critics_for_movie1_pearson_coefficient))

similar_items_euclidean = calculate_similar_items_euclidean(critics)
similar_items_pearson = calculate_similar_items_pearson(critics)

print('similar items for euclidean distance = {0}'.format(similar_items_euclidean))
print('similar items for pearson coefficient = {0}'.format(similar_items_pearson))

recomended_items_for_person1_euclidean = get_recommended_items(critics, similar_items_euclidean, person1)
recomended_items_for_person1_pearson = get_recommended_items(critics, similar_items_pearson, person1)

print('recomended items for {0} using euclidean distance = {1}'.format(person1, recomended_items_for_person1_euclidean))
print('recomended items for {0} using pearson coefficient = {1}'.format(person1, recomended_items_for_person1_pearson))
