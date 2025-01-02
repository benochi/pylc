from collections import Counter

arr = [1, 1, 2, 3, 4, 4, 4, 5, 6, 0, 0]
count = Counter(arr)
if count[4]:
    print(True)
    print(count[4])
else:
    print(False)

# def customSort(arr):
#     for i in arr:


print("a".isalnum())
print("2".isalnum())
print(ord("a"))
print(ord("b"))
print("-".isalnum())

print(arr.sort(key=customSort()))