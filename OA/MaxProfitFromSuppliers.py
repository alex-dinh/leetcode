'''
Max Profit From Suppliers (Amazon OA2)

from amazon thread:
https://leetcode.com/discuss/interview-question/868302/
optimal solution:
https://leetcode.com/discuss/interview-question/823177/amazon-oa-2020-find-the-highest-profit/713075
'''

import heapq
from typing import List

# naive approach: use heap (python's heapq), O (n^2) solution
def highest_profit_heap(numSuppliers: int, inventory: List[int], order: int):
    '''
    :param numSuppliers: number of suppliers
    :param inventory: list of ints, represent value of item at given supplier
    :param order: number of items that the customer has ordered
    :return: highest amount of profit that can be generated for given item

    note: if supplier has n items, the amount of profit is n! (n factorial)
                          4 items,                         4 + 3 + 2 + 1
    in other words: profit on item = # of items supplier has left
    note 2: this problem in Java specifies long ints, but doesn't matter in python
    '''

    profit = 0
    inv = [-i for i in inventory]
    heapq.heapify(inv)  # O(n)
    for i in range(order): # O(n)
        item = heapq.heappop(inv) # O(log n)
        profit += -item
        heapq.heappush(inv, item + 1) # O(log n)
        # print(item)

    return profit

# optimal approach: O(n), using hashmap/dict
def highest_profit(numSuppliers: int, inventory: List[int], order: int):
    '''
    :param numSuppliers: number of suppliers
    :param inventory: list of ints, represent value of item at given supplier
    :param order: number of items that the customer has ordered
    :return: highest amount of profit that can be generated for given item

    note: if supplier has n items, the amount of profit is n! (n factorial)
                          4 items,                         4 + 3 + 2 + 1
    in other words: profit on item = # of items supplier has left
    note 2: this problem in Java specifies long ints, but doesn't matter in python
    '''

    profits = {}
    for item in inventory: # O(n)
        profits[item] = profits.get(item, 0) + 1

    mpi = max(inventory) # most profitable item, O(n)
    max_profit = 0
    for i in range(order): # O(n)
        max_profit += mpi
        profits[mpi - 1] = profits.get(mpi - 1, 0) + 1
        if profits[mpi] == 1:
            del profits[mpi]
            mpi -= 1
        elif profits[mpi] > 1:
            profits[mpi] -= 1

    return max_profit

def highest_profit_lc(numSuppliers: int, inventory: List[int], order: int):
    # key principle: given the current max price, the next largest max prices is always 1 less

    # map, item price : number of items we can sell at the price
    profit = dict()
    for price in inventory:
        profit[price] = profit.get(price, 0) + 1

    # the current most profitable item price,
    #   could have just taken max(inventory)
    curr_max = max(profit.items(), key=lambda x: x[0])[0]

    res = 0 # variable to count max possible profit
    while order > 0:
        # maxi: number of items we can sell at current max price,
        #   take min() in case because:
        #       possible that # of items remaining in order < # of items we can sell at current max price
        maxi = min(order, profit[curr_max])

        # add max profits for current item to result
        res += curr_max * maxi

        # update number of remaining number of items in order to fulfill
        order -= maxi

        # update inventory available in profits dict()
        # if there was 2 items we could sell for 5, that means:
        #   now there is 2 of that same item we can sell for 4
        profit[curr_max] -= maxi
        profit[curr_max - 1] = profit.get(curr_max - 1, 0) + maxi

        # when the remaining inventory for a current max price reaches 0,
        #   remove from profits dict
        #   update current max price
        if profit[curr_max] == 0:
            del profit[curr_max]
            curr_max -= 1

    return res

numSuppliers = 2
inventory = [3, 5]
order = 6
# max profit = 5 + 4 + 3 + 3 + 2 + 2 = 19
print(highest_profit(numSuppliers, inventory, order))
print(highest_profit_heap(numSuppliers, inventory, order))

numSuppliers = 2
inventory = [5, 5]
order = 4
# max profit = 5 + 5 + 4 + 4 = 18
print(highest_profit(numSuppliers, inventory, order))
print(highest_profit_heap(numSuppliers, inventory, order))

numSuppliers = 1
inventory = [5]
order = 5
# max profit = 5 + 4 + 3 + 2  + 1 = 15
print(highest_profit(numSuppliers, inventory, order))
print(highest_profit_heap(numSuppliers, inventory, order))
