# Brute force - O(n^2) and O(1) gives TLE for large n 
# Optimise - Sort the array and compare adjacent values, still O(nlogn) and O(1)
# Most optimal solution using HashSet(set with hashing) - Time Complexity: O(n) , Space Complexity: O(n) 


def containsDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

