
from collections import deque
names = deque()
names.append('pawpaw')
names.append('jackfruit')
names.append('mangoes')
names.append('apple')
print("Initial queue")
print(names)
print("\nElements dequeued from the queue")
print(names.pop())
print(names.pop())
print(names.pop())
print(names.pop())
