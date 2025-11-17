from collections import deque

# Implementing Queue using collections.deque
queue = deque()

# Enqueue 4 values
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

# Dequeue 1 value
dequeued_value = queue.popleft()

# Display queue
print("Current Queue:", list(queue))


