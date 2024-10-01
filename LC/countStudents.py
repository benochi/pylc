# not linkedlist style
def countStudents(students, sandwiches):
    while students and sandwiches:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            students.append(students.pop(0))
        # if we still ahve sandwiches and no matching students, break.
        if sandwiches and students.count(sandwiches[0]) == 0:
            break

    return len(students)


# easier with hashmap:
def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    res = len(students)
    count = Counter(students)

    for s in sandwiches:
        if count[s] > 0:
            res -= 1
            count[s] -= 1
        else:
            return res

    return res


# Test case 1
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
print("Test case 1 result:", countStudents(students, sandwiches))  # Expected output: 0

# Test case 2
students = [1, 1, 0, 0]
sandwiches = [1, 1, 1, 0]
print("Test case 2 result:", countStudents(students, sandwiches))  # Expected output: 2

# Test case 3
students = [0, 0, 0, 0]
sandwiches = [1, 1, 1, 1]
print("Test case 3 result:", countStudents(students, sandwiches))  # Expected output: 4

# Test case 4
students = [1, 0, 1, 0]
sandwiches = [0, 0, 1, 1]
print("Test case 4 result:", countStudents(students, sandwiches))  # Expected output: 0
