def tiggerfy(word):
    result = ""
    i = 0
    while i < len(word):
        if word[i].lower() == 't':
            i += 1
        elif word[i].lower() == 'i':
            i += 1
        elif i + 1 < len(word) and word[i:i+2].lower() == 'gg':
            i += 2
        elif i + 1 < len(word) and word[i:i+2].lower() == 'er':
            i += 2
        else:
            result += word[i]
            i += 1
    return result

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))