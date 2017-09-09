from critics import critics
from recomendations import euclidean_distance, pearson_distance

person1 = 'Lisa Rose'
person2 = 'Gene Seymour'

euclidean_dist = euclidean_distance(critics, person1, person2)
pearson_dist = pearson_distance(critics, person1, person2)

print('euclidean distance between {0} and {1} = {2}'.format(person1, person2, euclidean_dist))
print('pearson distance between {0} and {1} = {2}'.format(person1, person2, pearson_dist))
