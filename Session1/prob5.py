def find_missing_clues(clues, lower, upper):
    clues = sorted(clues)
    clue_set = set(clues)
    missing_ranges = []
    start = lower
    
    for num in range(lower, upper + 1):
        if num in clue_set:
            if start < num:
                missing_ranges.append([start, num - 1])
            start = num + 1
    
    if start <= upper:
        missing_ranges.append([start, upper])
    
    return missing_ranges

clues1 = [0, 1, 3, 50, 75]
lower1 = 0
upper1 = 99
print(find_missing_clues(clues1, lower1, upper1))

clues2 = [-1]
lower2 = -1
upper2 = -1
print(find_missing_clues(clues2, lower2, upper2))