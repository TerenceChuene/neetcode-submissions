class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Loop through the array
        for i in range(len(nums)):
            # Step 2: Create a second loop
            for j in range(i + 1, len(nums)):
                # Step 3: Check whether two numbers equal target
                if nums[i] + nums[j] == target:
                    # Step 4: Return their indices
                    return [i, j]