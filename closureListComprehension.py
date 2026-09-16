from functools import reduce
import time
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
#sum_list_output_1 = reduce(lambda x,y: x+y, [even_result, odd_result])

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

# =============== 4 ===============

def date_generator(date: str, num_of_dates: int, num__of_jumps: int):
    pass 



def main():
    if_armstrong = input("Enter a number to check if it is an Armstrong number: ")
    if if_armstrong.isdigit():
        print(is_armstrong(int(if_armstrong)))
    else:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()