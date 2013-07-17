def bubble_sort(unsorted):
    no_swaps = True
    while no_swaps:
        no_swaps = False
        for item in range(1,len(unsorted)-1):
            if unsorted[item] > unsorted[item+1]:
                temp = unsorted[item+1]
                unsorted[item+1] = unsorted[item]
                unsorted[item] = temp
                no_swaps = True


with open("students_unsorted.txt",mode="r",encoding="utf-8") as my_file:
    students = my_file.read().splitlines()
bubble_sort(students)
with open("students_sorted.txt",mode="w",encoding="utf-8") as my_file:
    for student in students:
        my_file.write(student+'\n')
