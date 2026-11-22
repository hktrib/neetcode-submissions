class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        total = 0
        N = len(height)
        left_max_height = [0] * N
        right_max_height = [0] * N

        left_max_height[0] = height[0]
        for i in range(1, N):
            left_max_height[i] = max(left_max_height[i - 1], height[i])

        right_max_height[N - 1] = height[N - 1]
        for i in range(N - 2, -1, -1):
            right_max_height[i] = max(right_max_height[i + 1], height[i])

        for i in range(N):
            total += (min(left_max_height[i], right_max_height[i]) - height[i])
        
        return total