# Write your function, here.
def insertion_sort(lst):
    sorted_lst = []
    for i in lst:
        for j in range(len(sorted_lst)):
            digit = sorted_lst[j]
            if i <= sorted_lst[j]:
                sorted_lst.insert(j,i)
                break
            if j+1 == len(sorted_lst):
                sorted_lst.append(i)
        if len(sorted_lst) == 0:
            sorted_lst.append(i)
    return sorted_lst


print(insertion_sort([55, 21, 5, 3, 6, 95])) #> [3, 5, 6, 21, 55, 95]
print(insertion_sort([4, 1, 0, 3, 8, 9])) #> [0, 1, 3, 4, 8, 9]
print(insertion_sort([1, 4, 3, 0, 3, 0, 2, 8])) #> [0, 0, 1, 2, 3, 3, 4, 8]