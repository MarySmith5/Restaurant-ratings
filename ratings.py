"""Restaurant rating lister."""


# put your code here
ratings_info = open('scores.txt')

restaurant_ratings = {}

for line in ratings_info:
    line = line.rstrip()
    place_and_rating = line.split(':')

    restaurant_ratings[place_and_rating[0]] = place_and_rating[1]

sort_me = restaurant_ratings.items()
rest_rate_sorted = sorted(sort_me)
sorted_restaurant_ratings = dict(rest_rate_sorted)

ratings_info.close()
print(sorted_restaurant_ratings)

