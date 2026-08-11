class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        midRightStart = 0

        k = k % n

        def reverse(leftStart: int, rightStart: int) -> None:
            nonlocal nums
            left = leftStart

            right = rightStart - 1

            print(left)
            print(right)
            print()
            while left < right:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp

                right -= 1
                left += 1

        
        reverse(0, n)
        reverse(0, k)
        reverse(k, n)
        pass
