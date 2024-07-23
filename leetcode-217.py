# Time Complexity: O(n) , Space Complexity: O(n) - Most optimal solution using hashset(set with hashing)
def containsDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

