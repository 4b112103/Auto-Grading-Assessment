#!/usr/bin/env python3

def sign_pairs(numbers):
    pass
    #---------------------- 
    # write your code here
    #---------------------- 
    num_list = [int(num) for num in numbers.split()]

    result = []

    for i in range(len(num_list) - 1):
        if (num_list[i] > 0 and num_list[i + 1] > 0) or (num_list[i] < 0 and num_list[i + 1] < 0):
            result.append([num_list[i], num_list[i + 1]])

    return result
#---------------------------------------------------------------------
# you can modify the following to test your code more thoroughly
#---------------------------------------------------------------------
data = [
    "1 -2 3 4 -5 6 7 8 -9 10",
    "1 -2 3 -5 6 -7 8 -9 10",
    "1 2 3 4 5 6 7 8 9 10",
    "1 -2 3 -4 5 -6 7 -8 9 -10",
    "1 -2 3 -4 5 -6 7 -8 9 -10 11",
    "1 -2 3 -4 5 -6 7 -8 9 -10 11 -12",
    "-1 -2 -3 -4 -5 -6 -7 -8 -9 -10",
 ]

        
def main():
    global data
    for test_case in data:
        result = sign_pairs(test_case)
        print(result)
        
if __name__ == '__main__':
    main()
