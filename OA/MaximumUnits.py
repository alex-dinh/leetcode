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
    heap = []
    for i in range(len(boxes)):
        units_per_box = unitsPerBox[i]
        # by default python heapq is a minheap, so negate values to sim a maxheap,
        # most negative nums at top of heap
        heapq.heappush(heap, (-units_per_box, boxes[i]))

    res = 0

    # "adding" boxes to the truck
    # get the box with most units from heap, calculate how many units can be shipped
    # taking min() is faster than iterating 1 by 1
    while truckSize > 0 and heap:
        curr_max = heapq.heappop(heap)
        max_boxes = min(truckSize, curr_max[1])
        truckSize -= max_boxes
        res += max_boxes * (curr_max[0] * -1)

    return res


boxes = [1, 2, 3]
unitsPerBox = [3, 2 ,1]
truckSize = 3
print(getMaxUnits(boxes, unitsPerBox, truckSize))
