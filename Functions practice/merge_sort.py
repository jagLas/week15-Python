# Write your code here.
def merge_sort(lst):
    # Call merge somewhere in here
    mid = int(len(lst) / 2)

    first_half = lst[: mid]
    second_half = lst[mid:]

    if len(first_half) > 1:
        first_half = merge_sort(first_half)

    if len(second_half) > 1:
        second_half = merge_sort(second_half)

    return merge(first_half, second_half)

def merge(first_half, second_half):
    # Merge logic goes here
    sorted_list = []
    while len(first_half) or len(second_half):
        if len(first_half) == 0:
            sorted_list.append(second_half.pop(0))
        elif len(second_half) == 0:
            sorted_list.append(first_half.pop(0))
        elif first_half[0] < second_half[0]:
            sorted_list.append(first_half.pop(0))
        else:
            sorted_list.append(second_half.pop(0))

    return sorted_list


lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
print(sorted_lst)

# merge_sort(lst)                     # In place solution
# print(lst)