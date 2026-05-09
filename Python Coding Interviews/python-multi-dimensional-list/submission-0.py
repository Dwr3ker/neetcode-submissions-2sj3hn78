from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_arr = []

    for arr in nested_arr:
        curr_max = 0
        for element in arr:
            curr_max = max(curr_max, element)
                

        max_arr.append(curr_max)       
    return max_arr

    # new_list = []
    # for lst in nested_arr:
    #     max_elm = max(lst)
    #     new_list.append(max_elm)
    # return new_list





# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
