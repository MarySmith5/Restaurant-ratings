"""Restaurant rating lister."""


def choose_option():
    """Give user options and return the chosen option."""

    while True:

        options = ['S', 'A', 'U', 'Q']
        print( "Would you like to:\n"
                "S: See restaurants/ratings\n"
                "A: Add a restautant/rating\n"
                "U: Update a rating\n"
                "Q: quit")

        option = input('> ').upper()

        if option not in options:
            print('Enter S, A, U, or Q')

        else:
            return option


def add_restaurant(restaurants_file):
    """User add restaurant and rating """
        
    rest_name = input("Enter the restaurant name: ").title()

    while True:

        rating = int(input("Enter a rating between 1 and 5: "))
        if rating < 1 or rating > 5:
            print("Invalid.")

        else:
            break
            
    ratings_info = open(restaurants_file, 'a')
    ratings_info.write(f'{rest_name}:{rating}\n')
    ratings_info.close()

    print("Restaurant added.")           
     

def make_dict(restaurants_file):
    """Process info into dictionary."""

    ratings_info = open(restaurants_file)
    restaurant_ratings = {}

    for line in ratings_info:
        line = line.rstrip()
        place_and_rating = line.split(':')

        restaurant_ratings[place_and_rating[0]] = place_and_rating[1]

    #Sort the dictionary

    sort_me = restaurant_ratings.items()
    rest_rate_sorted = sorted(sort_me)
    
    sorted_restaurant_ratings = dict(rest_rate_sorted)

    ratings_info.close()

    return sorted_restaurant_ratings


def see_restaurants(sorted_dict):
    """Print dictionary in readable sorted lines."""

    for key in sorted_dict:
        print(f"{key} is rated at {sorted_dict[key]}.")


#def update_rating()


def run_main(restaurants_file):
    """Run restaurant ratings program."""

    print(" Welcome to the restaurant rater!")
    print()

    while True:

        sorted_restaurants = make_dict(restaurants_file)

        do_this = choose_option()

        if do_this == "S":

            see_restaurants(sorted_restaurants)
            print()

        elif do_this == "A":

            add_restaurant(restaurants_file)
            
            print()

        elif do_this == "Q":

            print("Bye")
            break


run_main('scores.txt')

            

            




