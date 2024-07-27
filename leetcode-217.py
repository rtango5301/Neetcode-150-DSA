# Brute force - O(n^2) and O(1) gives TLE for large n 
# Optimise - Sort the array and compare adjacent values, still O(nlogn) and O(1)
# Most optimal solution using HashSet(set with hashing) - Time Complexity: O(n) , Space Complexity: O(n) 


def containsDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
        #   print('yes')
            return True
        hashset.add(n)
#   print('no')
    return False

# list = [1,2,3,3,4,5]

# containsDuplicate(list)
# hashset = set()
# set = {3,4,5,3}

# hashset.add(3)
# hashset.add(4)
# hashset.add(5)
# hashset.add(3)

# print(hashset)
# print(set)



