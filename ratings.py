"""Restaurant rating lister."""


# put your code here

ratings_info = open('scores.txt')
#Import needed info

restaurant_ratings = {}

#User option to add restaurant and rating 
while True:

    choice = input("Would you like to make an entry? Y or N: ").upper()

    if choice.startswith('Y'):

        rest_name = input("Enter the restaurant name: ").title()
        rating = input("Enter the rating: ")

        restaurant_ratings[rest_name] = rating

    else:
        break

#Process info into dictionary
for line in ratings_info:
    line = line.rstrip()
    place_and_rating = line.split(':')

    restaurant_ratings[place_and_rating[0]] = place_and_rating[1]

#Sort the dictionary
sort_me = restaurant_ratings.items()
rest_rate_sorted = sorted(sort_me)
sorted_restaurant_ratings = dict(rest_rate_sorted)

#Print dictionary in readable sorted lines.
for key in sorted_restaurant_ratings:
    print(f"{key} is rated at {sorted_restaurant_ratings[key]}.")

ratings_info.close()
#print(sorted_restaurant_ratings)

