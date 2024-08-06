from itertools import permutations


arr = input().split()
arr2 = [int("".join(p)) for p in permutations(arr, len(arr))]
max_ = max(arr2) if
print(max(arr2))



