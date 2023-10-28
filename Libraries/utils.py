v_test = 'This is a test variable'

def search_pattern_in_list(in_list, in_target):
    '''
    Purpose: This function finds the target in given list and returns its index position. If not found, returns -1

    :return:
    '''
    for ind, val in enumerate(in_list):
        if in_target == val:
            return ind

    return -1