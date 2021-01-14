import pytest
from stacks_and_queues.stacks_and_queues import Stack, Queue, InvalidOperationError
from queue_with_stacks.queue_with_stacks import PseudoQueue

def test_enqueue():
  pq = PseudoQueue()
  pq.enqueue(10)
  pq.enqueue(15)
  pq.enqueue(20)
  pq.enqueue(5)
  actual = pq.stack1.top.value
  expected = 5
  assert actual == expected

def test_dequeue():
  pq = PseudoQueue()
  pq.enqueue(20)
  pq.enqueue(5)
  pq.enqueue(10)
  pq.enqueue(15)
  actual = pq.dequeue()
  expected = 20
  assert actual == expected