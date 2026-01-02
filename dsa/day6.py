from collections import deque
prices = deque()
prices.appendleft(123)
prices.appendleft(422)
prices.appendleft(30)

print(prices.pop())
print(prices)