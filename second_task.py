import heapq

def merge_k_lists(lists):
    merged_list = list(heapq.merge(*lists))
    return merged_list

my_lists = [[1, 4, 5], [1, 3, 4, 8], [2, 6, 7]]
print("Відсортований список:", merge_k_lists(my_lists))
