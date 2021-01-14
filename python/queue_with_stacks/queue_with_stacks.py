from stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue():
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, value):
    self.stack1.push(value)

  def dequeue(self):
    while self.stack1.peek():
      if self.stack1.top.next == None:
        return self.stack1.top.value
      
      else:
        temp = self.stack1.pop()
        self.stack2.push(temp)
        continue

