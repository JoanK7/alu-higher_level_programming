#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        result = my_list[:x]
        for i in result:
            print(i, end='')
            count += 1
    except Exception as e:
        print("Error: ", e)
    print('')
    return count
