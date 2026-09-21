created_list = [i for i in range(1,6)]
list_with_a_second_degree = [i**2 for i in created_list]
list_with_a_third_degree = [i**3 for i in created_list]
list_with_a_fourth_degree = [i**4 for i in created_list]
print(list_with_a_second_degree,list_with_a_third_degree,list_with_a_fourth_degree)


# created_list = [[i ** power for i in range(1, 6)] for power in range(1, 5)]


# print(created_list)