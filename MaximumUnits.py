'''
Maximum Units (Amazon OA)

https://leetcode.com/discuss/interview-question/793606/

Description:
- Warehouse manager needs to create shipment and fill truck
- All products in warehouse are in same-size boxes
'''

from typing import List
import heapq

def get_max_units_default(num: int, boxes: List[int], unit_size: int, units_per_box: List[int], truckSize: int):
    '''
    :param num: number of products
    :param boxes: list of ints, # of available boxes of each product
    :param unit_size: size of list units_per_box
    :param units_per_box: list of ints, # of units packed in each box
    :param truckSize: capacity of truck (in # of boxes)
    :return: int, max # of units that truck can carry

    note: num & unit_size not necessary in python, redundant vars useful for C/Java/etc
    '''
    pass


def get_max_units(boxes: List[int], units_per_box: List[int], truck_size: int):
    '''
    :param boxes: list of ints, # of available boxes of each product
    :param units_per_box: list of ints, # of units packed in each box
    :param truck_size: capacity of truck (in # of boxes)
    :return: int, max # of boxes that truck can carry

    possible approaches: list sorting, heap. O(nlogn)
    '''
    products = []
    for i in range(len(units_per_box)):
        for j in range(boxes[i]):
            products.append(units_per_box[i])
    heapq._heapify_max(products)
    # print(products)
    return sum(products[0:truck_size])




'''
Example:
'''
boxes = [1, 2, 3]
units_per_box = [3, 2, 1]
truck_size = 3
# max units = 3*1 + 2*2 = 7
print(get_max_units(boxes, units_per_box, truck_size))


