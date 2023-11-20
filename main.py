# main.py - головний модуль 
from TK_1 import input_values 
from TK_2 import min_max_values 
from TK_3 import divide_by_mean 
from TK_4 import multiply_by_mean 
from TK_5 import square_root 
 
def main(): 
 
    count = int(input("Введіть кількість значень: ")) 
    values = input_values(count) 
    print(f"Введені значення: {values}") 
 
    min_val, max_val = min_max_values(values) 
    print(f"Мінімальне значення: {min_val}, Максимальне значення: {max_val}") 
 
    divided_values = divide_by_mean(values) 
    print(f"Значення, поділені на середнє: {divided_values}") 
 
    multiplied_values = multiply_by_mean(values) 
    print(f"Значення, помножені на середнє: {multiplied_values}") 
 
    square_root_values = square_root(values) 
    print(f"Квадратні корені від значень: {square_root_values}") 
 
if __name__ == "__main__": 
    main() 
