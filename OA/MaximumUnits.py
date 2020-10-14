# https://leetcode.com/discuss/interview-question/793606/
# Amazon OA2 question no. 1
# Warehouse manager needs to create shipment to fill a truck.

from typing import List
import heapq

def getMaxUnits(boxes: List[int], unitsPerBox: List[int], truckSize: int) -> int:
    '''
    :param boxes: list, # of available boxes for each product i
    :param unitsPerBox: list, # of units in each box of specified product i
    :param truckSize: int, capacity of truck in # of boxes
    :return: maximum number of units that can be shipped
    '''

    # build a maxheap
    # IMPORTANT NOTE: heapify() is O(n), because it takes a different amount of time for each node
    heap = []
    for i in range(len(boxes)): # O(n)
        units_per_box = unitsPerBox[i]
        # by default python heapq is a minheap, so negate values to sim a maxheap,
        # most negative nums at top of heap
        #   heapq is sorted by first item in pair, the num of units
        heapq.heappush(heap, (-units_per_box, boxes[i]))

    res = 0

    # "adding" boxes to the truck
    # get the box with most units from heap, calculate how many units can be shipped
    # taking min() is faster than iterating 1 by 1, reduces number of iterations in loop
    while truckSize > 0 and heap: # O(t), t = truck size
        curr_max = heapq.heappop(heap) # O(log n), n is
        max_boxes = min(truckSize, curr_max[1]) # while min() is typically O(n), n always == 2, so O(1) in this context
        truckSize -= max_boxes
        res += max_boxes * (curr_max[0] * -1)

    # FINAL TIME COMPLEXITY: O(T LOG N), T is truckSize, N is size of boxes[]
    return res



boxes = [1, 2, 3]
unitsPerBox = [3, 2 ,1]
truckSize = 3
print(getMaxUnits(boxes, unitsPerBox, truckSize))
