# Write your function, here.
def sum_first_last_list(first_lst, second_lst):
    return first_lst[0] + second_lst[-1]


print(sum_first_last_list([1, 2, 3], [5, 8, 9]))     #> 10
print(sum_first_last_list([53, 26], [5]))            #> 58
print(sum_first_last_list([9], [5, 8]))              #> 17
print(sum_first_last_list([64], [5, 6, 2]))          #> 66