from functools import reduce

def my_func(arg1,arg2):
    return arg1*arg2

new_list = [i for i in range(100,1001) if i %2 == 0]
print(f'Полученный список -{reduce(my_func,new_list)}')
