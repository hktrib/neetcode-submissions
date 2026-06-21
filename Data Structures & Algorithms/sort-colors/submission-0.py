class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        
        nums[:red] = [0] * red
        nums[red: red + white] = [1] * white
        nums[red + white:red + white + blue] = [2] * blue