def odd_or_even(number):
    if number % 2 == 0:
        res = number // 2
    elif number %2 == 1:
        res = 3 * number + 1
    return res

def colltaz(number):
    new_num = odd_or_even(number) 
    print(f"new num is {new_num}")
    return new_num


def validate_input():
    print("Please enter a number.")
    try:
        user_input = int(input())
    except:
        raise ValueError("Non inreger input cannot be accepted") 

    return user_input 

input_num = validate_input()
print(f"the input num is {input_num}")

func_ret_val = colltaz(input_num)
while func_ret_val != 1:
    input_num = func_ret_val
    func_ret_val = colltaz(input_num)