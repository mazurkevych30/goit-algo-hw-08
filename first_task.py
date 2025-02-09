import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

def calculate_min_cost(cabels):
    cabels = heap_sort(cabels)
    total_cost = 0

    while len(cabels) > 1:
        first_cabel = heapq.heappop(cabels)
        second_cabel = heapq.heappop(cabels)

        new_cabel_cost = first_cabel + second_cabel
        total_cost += new_cabel_cost

        heapq.heappush(cabels, new_cabel_cost)

    return total_cost

arr = [12, 11, 13, 5, 6, 7]
print("Мінімальні витрати на з'єднання кабелів:", calculate_min_cost(arr))
