# Find the Highest Profit
# https://leetcode.com/discuss/interview-question/823177/amazon-oa-2020-find-the-highest-profit/713075
# naive : sorting/heap, O(n log n)
# optimal : hashmap/dict, O(N)

'''
Amazon Basics has several suppliers for its products.
For each of the products, the stock is represented by
a list of a number of items for each supplier. As items
are purchased, the supplier raises the price by 1 per
item purchased. Let's assume Amazon's profit on any
single item is the same as the number of items the
supplier has left. For example, if a supplier has 4
items, Amazon's profit on the first item sold is 4,
then 3, then 2 and the profit of the last one is 1.

Given a list where each value in the list is the number
of the item at a given supplier and also given the number
of items to be ordered, write an algorithm to find the
highest profit that can be generated for the given product.

Input
The input to the function/method consists on three arguments:
- numSuppliers, an integer representing the number of suppliers;
- inventory, a list of long integers representing the value of the item at a given supplier;
- order, a long integer representing the number of items to be ordered.

Output
Return a long integer representing the highest profit that can be generated for the given product.
'''

def highest_profit(numSuppliers: int, inventory: list[int], order: int):
    pass