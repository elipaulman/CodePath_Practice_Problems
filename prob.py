def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    print(merged)

intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals1)

intervals2 = [[1, 4], [4, 5]]
merge_intervals(intervals2)