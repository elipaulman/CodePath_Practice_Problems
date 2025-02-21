def delete_minimum_elements(hunny_jar_sizes):
    hunny_jar_sizes.sort()
    result = []
    for jar in hunny_jar_sizes:
        result.append(jar)
        hunny_jar_sizes.pop
    print(result)

hunny_jar_sizes1 = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes1)

hunny_jar_sizes2 = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes2)