# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of set1 and set2
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")

# Intersection of set1 and set2
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

# Difference of set1 from set2
difference_set1 = set1.difference(set2)
print(f"Difference of set1 from set2: {difference_set1}")

# Difference of set2 from set1
difference_set2 = set2.difference(set1)
print(f"Difference of set2 from set1: {difference_set2}")

# Symmetric difference between set1 and set2
symmetric_difference_set = set1.symmetric_difference(set2)
print(f"Symmetric difference between set1 and set2: {symmetric_difference_set}")
