# ZIP function
players = ['Sachin', 'Virat', 'Rohit', 'Rishabh']
cities = ['Mumbai', 'Banglore', 'Pune', 'Delhi']

player_city = [(player, city) for player, city in zip(players, cities)]
print(player_city)

# player_city = [(player, city) for player in players for city in cities]
# print(player_city)


# player_city = []
# for player, city in zip(players, cities):
#     player_city.append((player, city))
#
# print(player_city)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# ## Find the even elements in the list ##
#
# # Approach 3 : list comprehension
# even_numbers = [n for n in numbers if n%2 == 0]
# print(f'Original List = {numbers}')
# print(f'Even List = {even_numbers}')

# # Approach 2 : filter function
# def func_even_number(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
#
# even_numbers = list(filter(func_even_number, numbers))
# print(f'Original List = {numbers}')
# print(f'Even List = {even_numbers}')

# # Approach 1 : basic method
# even_numbers  = []
# for n in numbers:
#     if n%2 == 0:
#         even_numbers.append(n)
# print(f'Original List = {numbers}')
# print(f'Even List = {even_numbers}')





## Find the squares of each of the element in the list ##

# # Approach 3 : list comprehension
# square_numbers = [ n*n for n in numbers]
# print(f'Original List = {numbers}')
# print(f'Squared List = {square_numbers}')


# # Approach 2 : map function
# def func_square_number(n):
#     return n*n
#
# squared_numbers = list(map(func_square_number, numbers))
# print(f'Original List = {numbers}')
# print(f'Squared List = {squared_numbers}')

# # Approach 1 : basic method
# square_numbers  = []
# for n in numbers:
#     squares = n*n
#     square_numbers.append(squares)
# print(f'Original List = {numbers}')
# print(f'Squared List = {square_numbers}')