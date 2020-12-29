import heapq

heap = []

heapq.heappush(heap,(1,2,3))
heapq.heappush(heap,(2,5,8))
heapq.heappush(heap,(-1,3,8))
heapq.heappush(heap,(-8,999,999))
heapq.heappush(heap,(-8,997,1000))
print(heapq.heappop(heap))