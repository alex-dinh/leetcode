'''
Max Profit From Suppliers (Amazon OA2)

from amazon thread:
https://leetcode.com/discuss/interview-question/868302/
optimal solution:
https://leetcode.com/discuss/interview-question/823177/amazon-oa-2020-find-the-highest-profit/713075
'''

'''
Amazon Basics has several suppliers for its products.
The inventory available from each supplier is given a list of numbers.
Let's assume Amazon's profit on any single item = quantity remaining

If a supplier has 4 items, the profit on the first item is 4, then 3, then 2, then 1.
https://leetcode.com/discuss/interview-question/868302/

Find the maximum amount of profit given the number of suppliers, the inventory for each supplier, 
and the customer's order (in number of units order)
'''


from typing import List

# optimized everything
def highest_profit_comments(numSuppliers: int, inventory: List[int], order: int):
    # key principle: given the current max price, the next largest max prices is always 1 less

    # map, item price : number of items we can sell at the price
    profit = dict()
    for price in inventory: # price = quantity
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

def highest_profit(numSuppliers: int, inventory: List[int], order: int):
    profit = dict() # dictionary to keep track of prices
    for price in inventory:
        profit[price] = profit.get(price, 0) + 1

    curr_max = max(profit.items(), key=lambda x: x[0])[0]

    res = 0
    while order > 0:
        maxi = min(order, profit[curr_max])
        res += curr_max * maxi
        order -= maxi
        profit[curr_max] -= maxi
        profit[curr_max - 1] = profit.get(curr_max - 1, 0) + maxi
        if profit[curr_max] == 0:
            del profit[curr_max]
            curr_max -= 1

    '''
    N: size of inventory
    K: number of items in the order
    time complexity: O(N + K) = O(N) or O(K)
    # Space: O(N)
    '''
    return res

numSuppliers = 2
inventory = [3, 5]
order = 6
# max profit = 5 + 4 + 3 + 3 + 2 + 2 = 19
print(highest_profit(numSuppliers, inventory, order))







