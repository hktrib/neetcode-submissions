class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a,b,c = False, False, False

        for i, triplet in enumerate(triplets):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                triplets.pop(i)

        for trip in triplets:
            a = a or trip[0] == target[0]
            b = b or  trip[1] == target[1]
            c = c or trip[2] == target[2]
        


        return a and b and c