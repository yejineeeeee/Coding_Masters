import heapq

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

N, M = map(int, input().split())
visitors = [input().split() for _ in range(M)]

time_events = []
for s, e in visitors:
    start_time = time_to_seconds(s)
    end_time = time_to_seconds(e)
    time_events.append((start_time, end_time))

time_events.sort()

current_visitors = 0
total_visitors = 0
end_times_heap = [] 

for start_time, end_time in time_events:
    while end_times_heap and end_times_heap[0] <= start_time:
        heapq.heappop(end_times_heap)
        current_visitors -= 1

    if current_visitors < N:
        current_visitors += 1
        total_visitors += 1
        heapq.heappush(end_times_heap, end_time)  

print(total_visitors)
