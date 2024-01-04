class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[0]

# Create a new Queue
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Print the front element
print("Front element:", queue.peek())  # Should print 1

# Dequeue an element
queue.dequeue()

# Print the front element
print("Front element after dequeue:", queue.peek())  # Should print 2