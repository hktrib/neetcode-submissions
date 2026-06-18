class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            middle = len(nums) // 2

            left = nums[:middle]
            right = nums[middle : ]

            sortedLeft = self.sortArray(left)
            sortedRight = self.sortArray(right)

            return self.merge(sortedLeft, sortedRight)
    
    def merge(self, left, right) -> List[int]:
        result = []
        pointerLeft = 0
        pointerRight = 0

        # adding smallestElement from either array first
        while pointerLeft < len(left) and pointerRight < len(right):
            if left[pointerLeft] <= right[pointerRight]:
                result.append(left[pointerLeft])
                pointerLeft += 1
            else:
                result.append(right[pointerRight])
                pointerRight += 1
            

        # if pointerLeft < len(left):
        #     result.append(left[pointerLeft: ])        
        # else:
        #     result.append(right[pointerRight: ])
        while pointerLeft < len(left):
            result.append(left[pointerLeft])
            pointerLeft += 1

        while pointerRight < len(right):
            result.append(right[pointerRight])
            pointerRight += 1

        return result

