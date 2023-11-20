 
# TK_1.py - модуль для завдання 1 
def input_values(count): 
 
    values = [] 
    for i in range(count): 
        value = input(f"Введіть значення {i + 1}: ") 
        values.append(value) 
    return values 
 
