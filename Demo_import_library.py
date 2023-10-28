import Libraries.utils as utils
import random

courses = ['Math', 'Art', 'English',  'Design', 'CompSci']
target = random.choice(courses) # Randomly takes an element from the passed list, changes everytime

index_postition = utils.search_pattern_in_list(courses, target)

if index_postition == -1:
    print(f"Guven tatget is not present in the list!")
else:
    print(f"Index position of '{target}' in given list {courses} is: {index_postition}")



# import Libraries.utils as utils
#
# courses = ['Math', 'Art', 'English',  'Design', 'CompSci']
# target = 'English'
#
# index_postition = utils.search_pattern_in_list(courses, target)
#
# if index_postition == -1:
#     print(f"Guven tatget is not present in the list!")
# else:
#     print(f"Index position of '{target}' in given list {courses} is: {index_postition}")





# from Libraries.utils import search_pattern_in_list
#
# courses = ['Math', 'Art', 'English',  'Design', 'CompSci']
# target = 'English'
#
# index_postition = search_pattern_in_list(courses, target)
#
# if index_postition == -1:
#     print(f"Guven tatget is not present in the list!")
# else:
#     print(f"Index position of '{target}' in given list {courses} is: {index_postition}")
