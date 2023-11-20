# TK_3.py - модуль для завдання 3 
def divide_by_mean(input_list): 
 
    mean_value = sum(input_list) / len(input_list) 
    result = [value / mean_value for value in input_list] 
    return result 
 
