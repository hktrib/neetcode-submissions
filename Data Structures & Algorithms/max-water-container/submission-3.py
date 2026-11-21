class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l = 0
        r = len(heights) - 1
    
        # area is computed as (r - l) * min(heights[l], heights[r])
        # whichever wall (l or r) is shorter is the bottlebeck to the heights
        #  l += 1 if heights[l] < heights[r] else r -= 1


        while l < r:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))
    

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea