def activity_selection(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 1
    last_end = intervals[0][1]

    for s, e in intervals[1:]:
        if s >= last_end:
            count += 1
            last_end = e
    return count

# Example
print(activity_selection([(1,3),(2,4),(0,6),(5,7),(8,9),(5,9)]))
