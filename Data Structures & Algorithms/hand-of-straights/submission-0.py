class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        heap = []
        groupVals = {}

        for num in hand:
            groupVals[num] = 1 + groupVals.get(num, 0)
        
        # heapq.heapify(heap)

        # print(heap)
        print(groupVals)

        groups = []

        # n = len(hand) // groupSize

        # in place sort of hand
        hand.sort()

        i = 0
        smallest = hand[i]
        while i < len(hand):

            if groupVals[hand[i]] == 0:
                i += 1
                continue
            # min_smallest = len(hand)
            group = []
            smallest = hand[i]
            for j in range(groupSize):
                if smallest in groupVals and groupVals[smallest] > 0:
                    group.append(smallest)
                    groupVals[smallest] -= 1
                    # if groupVals[smallest] > 0:
                    #     min_smallest = min(i + j, min_smallest)
                    #     i = min_smallest

                    smallest += 1
                else:
                    return False
            
            print(group)
            groups.append(group)

        return True


