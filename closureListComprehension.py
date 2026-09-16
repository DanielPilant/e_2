from functools import reduce
import time
from datetime import datetime, timedelta
from decimal import Decimal
import math

# =============== 1 ===============

Y = lambda x: (x/2)+2

# ==1
new_list = list(map(Y, range(10001)))

#==2
#==3
# Higher order function
start_time = time.perf_counter()
sum_list_hof = reduce(lambda x,y:x+y,new_list)
end_time = time.perf_counter()
run_time = end_time - start_time
print(f"Higher order function runtime: {run_time}")

# Imperative approach
start_time = time.perf_counter()
sum_list_i = 0
for number in new_list:
    sum_list_i += number
end_time = time.perf_counter()
run_time = end_time - start_time
print(f"Imperative approach runtime: {run_time}")

#==4
start_time = time.perf_counter()
sum_list_all = reduce(lambda x,y:x+Y(y), range(10001), 0)
end_time = time.perf_counter()
run_time = end_time - start_time
print(f"One function runtime: {run_time}")

# =============== 2 ===============

main_list = list(range(1, 1001))
even_list = list(filter(lambda x: x%2==0, main_list))
odd_list = list(filter(lambda x: x%2!=0, main_list))

#==1
lambda_func_1 = lambda x,y: x*y
lambda_func_2 = lambda x,y: (x/2)+2+y

#==2
even_result = reduce(lambda_func_1, even_list, 1)
odd_result = reduce(lambda_func_2, odd_list, 0)

#==3
# even_result is too large to add to a float, so both results are summed as Decimal
sum_list_output_1 = reduce(lambda x,y: x+y, map(Decimal, [even_result, odd_result]))
print(f"Sum of even and odd results: {sum_list_output_1}")

# =============== 3 ===============

#==Aleph
def is_armstrong(number: int):
    digits = [int(digit) for digit in str(number)]
    len_digits = len(digits)
    return number == sum(list(map(lambda d: pow(d, len_digits), digits)))

print(is_armstrong(153))

#==bet
def armstrong_range(n1, n2):
    return list(filter(is_armstrong, range(n1,n2+1)))

#==gimel
# in main function
print(armstrong_range(1, 1000))
# =============== 4 ===============

def date_generator(date_str: str, num_of_dates: int, num_of_jumps: int):
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    return list(map(lambda i: (start_date + timedelta(days=i*num_of_jumps)).strftime("%Y-%m-%d"), range(num_of_dates)))

# =============== 5 ===============

#==Alef
def power_function(exponent: int):
    return lambda base: base ** exponent

#==bet
def generate_power_map(n: int):
    return map(power_function, range(n))
    
#==gimel
def taylor_e(x, n):
    powers = map(lambda f: f(x), generate_power_map(n))
    factorials = map(math.factorial, range(n))
    terms = map(lambda p, f: p/f, powers, factorials)
    return reduce(lambda x, y: x + y, terms)

# ============== 6 ===============
def task_manager():
    tasks = {}
    
    def add_task(task, status="incomplete"):
        tasks[task] = status
    
    def get_tasks():
        return tasks
    
    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"    
            
    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task
    }
    
# =============== 7 ===============

#==Aleph
def clean_text(text: str):
    return text.strip()

def capitalize_text(text: str):
    return text.title()

def add_stars(text: str):
    return f"***{text}***"

#==bet
def create_pipeline():
    return lambda x: x

def add_to_pipeline(pipeline, func):
    return lambda x: func(pipeline(x))

# =============== main ===============
def main():
    # == Targi3
    user_input_3 = input("Enter a number to check Armstrong range: ")
    if user_input_3.isdigit() and int(user_input_3) > 0:
        print(armstrong_range(1, int(user_input_3)))
    else:
        print("invalid input")

    #== Targil5b
    n_powers = input("Enter number of powers:\n")
    if n_powers.isdigit():
        result_map = generate_power_map(int(n_powers))
        print(type(result_map))
        base_val = input("Enter base:\n")
        if base_val.removeprefix("-").isdigit():
            print(tuple(map(lambda f: f(int(base_val)), result_map)))
        else:
            print("invalid input")
    else:
        print("invalid input")

    #== Targil7c
    
    p = create_pipeline()
    p = add_to_pipeline(p, clean_text)
    p = add_to_pipeline(p, capitalize_text)
    p = add_to_pipeline(p, add_stars)
    user_txt = input("enter text:\n")
    if not user_txt.strip():
        print("invalid input")
    else:
        print(p(user_txt))

if __name__ == "__main__":
    main() 