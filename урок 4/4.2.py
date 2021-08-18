my_list = [4, 17, 5, 6, 85, 25, 41, 19, 6, 23]
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)
