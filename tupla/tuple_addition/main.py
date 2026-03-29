animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
temp_tuple = ('Dumbo', 'Zootopia')
animal_movies += temp_tuple

del temp_tuple

# Testing
print("Updated animal movies:", animal_movies)