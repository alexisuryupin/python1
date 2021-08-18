my_list = [1, 1, 4, 5, 6, 7, 11, 4, 19, 23, 13]
print(my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)
