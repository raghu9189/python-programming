import copy

original = [
    [100, 2],
    [3, 4]
]

shallow_copy = copy.copy(original)      # Shallow Copy
deep_copy = copy.deepcopy(original)     # Deep copy

shallow_copy[0][0] = 1


print(original)
print(shallow_copy)
print(deep_copy)