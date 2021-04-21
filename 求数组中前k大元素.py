
import heapq


def heapsort(data, hp_size=3):
    h = []
    for i in range(len(data)):
        if i >= hp_size:
            heapq.heappushpop(h, data[i])
            print(i, h)
        else:
            heapq.heappush(h, data[i])
    return [heapq.heappop(h) for _ in range(len(h))]


res = heapsort([6, 2, 1, -4, 9, 4, 0])
print(res)
