def first_string(list_of_strings):
    # Want to remove whitespace and then return
    # the string that is alphabetically first
    
    new_list = [string.replace(' ', '') for string in list_of_strings]
    
    return min(new_list)