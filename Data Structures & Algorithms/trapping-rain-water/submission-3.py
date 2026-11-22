class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        N = len(height)
        left_max_height = [0] * N
        right_max_height = [0] * N

        # Pass 1: Strict max strictly to the left of index i (0 .. i-1)
        max_height = 0
        for i in range(1, N):
            max_height = max(max_height, height[i - 1])
            left_max_height[i] = max_height

        # Pass 2: Strict max strictly to the right of index i (i+1 .. N-1)
        max_height = 0
        for i in range(N - 2, -1, -1):
            max_height = max(max_height, height[i + 1])  # Fixed: i + 1 instead of i - 1
            right_max_height[i] = max_height

        # print(f"left_max_height: {left_max_height}")
        # print(f"right_max_height: {right_max_height}")

        # Pass 3: Clamp at 0 whenever height[i] is taller than its surrounding walls
        for i in range(N):
            water_at_i = min(left_max_height[i], right_max_height[i]) - height[i]
            total += max(0, water_at_i)  # Fixed: max(0, ...) prevents negative water

        return total