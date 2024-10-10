from collections import Counter


def minDistinct(A, K):
    # Count the frequency of each element
    freq = Counter(A)

    # Sort the elements by their frequency in ascending order
    freq_sorted = sorted(freq.items(), key=lambda x: x[1])

    # Count of distinct elements initially
    distinct_count = len(freq)

    # Iterate over the sorted frequencies and try to reduce distinct elements
    for num, count in freq_sorted:
        if K >= count:
            # If we can remove all occurrences of this element
            K -= count
            distinct_count -= 1
        else:
            # If we can't remove all occurrences of this element, break
            break

    return distinct_count
