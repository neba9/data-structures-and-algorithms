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

if __name__ == "__main__":
    new_stack = Stack()
    new_stack.push("10")
    new_stack.push("15")
    new_stack.push("20")
    # new_stack.pop()
    # new_stack.pop()
    print(new_stack)