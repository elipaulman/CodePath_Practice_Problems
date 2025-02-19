def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


items1 = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target1 = 'hunny'
print(linear_search(items1, target1))

items2 = ['bed', 'blue jacket', 'red shirt', 'hunny']
target2 = 'red balloon'
print(linear_search(items2, target2))