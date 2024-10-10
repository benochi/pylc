# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # Implement your solution here
    binary = bin(N)[2:]

    gaps = binary.strip("0").split("1")

    return max(len(gap) for gap in gaps) if gaps else 0
