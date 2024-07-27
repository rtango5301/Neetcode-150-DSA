class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


    #SOLUTION 1 :
        # if len(s)!=len(t):
        #     return False
        # count_S, count_T = {} , {}

        # for i in range(len(s)):
        #     count_S[s[i]] = count_S.get(s[i],0)+1
        #     count_T[t[i]] = count_T.get(t[i],0)+1
        # for c in count_S:
        #     if count_S[c] != count_T.get(c,0):
        #         return False
        # return True

    #SOLUTION 2 :
            # if len(s) != len(t):
            #     return False
            # count = collections.Counter(s)
            # count.subtract(collections.Counter(t))
            # return all(freq==0 for freq in count.values())
    
    
    #SOLUTION 3 : use the collections module Counter func
        # return Counter(s)==Counter(t)

    
    #SOLUTION 4 : use the legendary python sorting function
        return sorted(s) == sorted(t)