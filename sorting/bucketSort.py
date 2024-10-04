# Bucket Sort Algorithm
# 1. Choose the Number of Buckets:
#    - Determine the number of buckets to use. This can be based on the data range or size of the dataset.
#    - Each bucket will hold a range of values. More buckets mean fewer elements per bucket.
#
# 2. Initialize Buckets:
#    - Create an empty list of buckets. Each bucket is a list that will contain a subset of the original data.
#
# 3. Distribute Elements into Buckets:
#    - For each element in the input array, find the appropriate bucket based on its value.
#    - Place the element into the corresponding bucket.
#    - The bucket index can be calculated using the element value and the data range.
#
# 4. Sort Each Bucket:
#    - Sort the elements within each bucket. Since buckets are smaller, any sorting method can be used efficiently.
#    - Python’s built-in `sort()` or insertion sort works well here.
#
# 5. Concatenate Buckets:
#    - Append all elements from each bucket back into the original array in sorted order.
#
# Note:
# - Bucket Sort is efficient when data is uniformly distributed over a known range.
# - It has an average time complexity of O(n + k), where n is the number of elements, and k is the number of buckets.

# Rarely used, it can only handle guaranteed values within a finite range, ie: values of 0-2


def bucketSort(arr):
    output = []
    counts = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        counts[arr[i]] += 1

    for i in range(len(counts)):
        while counts[i] > 0:
            output.append(i)
            counts[i] -= 1

    return output


print(bucketSort([1, 0, 0, 1, 1, 2, 2, 3, 3, 2, 1, 3, 2, 1, 1, 0]))
