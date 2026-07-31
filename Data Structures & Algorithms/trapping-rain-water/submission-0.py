class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        total_water = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total_water += (leftMax - height[l])
            elif rightMax <= leftMax:
                r -= 1
                rightMax = max(rightMax, height[r])
                total_water += (rightMax - height[r])

        return total_water
