class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, ${self.salary}"

e1 = Person('Sachin', 42, 70000)
e2 = Person('Virat', 38, 80000)
e3 = Person('Rohit', 39, 90000)

employees = [e1, e2, e3]
def person_sort_name(p):
    return p.name

def person_sort_age(p):
    return p.age

employees = [e1, e2, e3]
# sort by age
sorted_persons_age  = sorted(employees, key=person_sort_age)
print(f"Sorted Persons by age: {sorted_persons_age}")

# sort by name
sorted_persons_name  = sorted(employees, key=person_sort_name)
print(f"Sorted Persons by name: {sorted_persons_name}")

# sort by salart with lambda
sorted_persons_salary = sorted(employees, key=lambda e: e.salary)
print(f"Sorted Persons by salary: {sorted_persons_salary}")

from operator import attrgetter
sorted_persons_age  = sorted(employees, key=attrgetter('age'))
print(f"attrgetter - Sorted Persons by age: {sorted_persons_age}")

sorted_persons_name  = sorted(employees, key=attrgetter('name'))
print(f"attrgetter - Sorted Persons by name: {sorted_persons_name}")



# employees = [e1, e2, e3]
# for e in employees:
#     print(e)





# ##  Sort on Dictionary ##
# player = {'name': 'Sachin', 'age': 40, 'cities': ['Mumbai', 'Pune']}
# print(f'Original dictionary = {player}')
#
# sorted_player = sorted(player)
# print(f'Sorted list = {sorted_player}') # default sorts on dictionary keys


# ##  Sort on Tuple ##
# players = ('Sachin', 'Rishabh', 'Gautam', 'Virat', 'Zaheer', 'Rohit')
# print(f'Original tuple = {players}')
#
# sorted_players = sorted(players)
# print(f'Sorted list = {sorted_players}')


##  Sort on List ##
# numbers = [9, 1, 5, 7, 3, 8, 4, 6]
# print(f'Original list = {numbers}')
#
# sorted_numbers = sorted(numbers)
# print(f'Sorted list = {sorted_numbers}')