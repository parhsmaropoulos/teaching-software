grade_percentages = {}

grades = [[9, 5],[4,6], [8,5], [2,9], [4,5]]

for grade in grades:
    g = grade[1] * 10
    fr = grade[0]
    if fr in grade_percentages:
        prev = grade_percentages.get(fr)
        grade_percentages[fr] = (prev+g)/2
    else:
        grade_percentages[fr] = g
    
print(grade_percentages)