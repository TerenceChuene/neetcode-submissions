class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #variable could seen 
        #Set is a pre-build method to removes duplicated intgers
        seen = set()
         # for integer in nums the variable num will be used to loop through each
        for num in nums:
        #if a variable num is hold the intger for nums and if it is seen as a duplicate it should be seen as true
          if num in seen:
           return True #if it is return true

          seen.add(num)#seen add number to idetified
        return False#if not false
