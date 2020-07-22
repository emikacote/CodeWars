def check_exam(arr1, arr2):
    test = list(map(list, zip(arr1, arr2)))
    grade = 0
    for i in range(4):
        letter = test[i]
        if "" in letter: continue
        if letter[1] == letter[0]: grade += 4
        else: grade -= 1
    if grade < 0: return 0
    return grade
