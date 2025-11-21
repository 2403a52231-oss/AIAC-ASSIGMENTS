"""
Unit tests for the Queue implementation in Task2.py.

Run with:
    python -m unittest test_task2.py
"""

import unittest

from Task2 import (
    Queue,
    QueueFullException,
    QueueEmptyException,
)


class TestQueue(unittest.TestCase):
    """Covers the core queue behaviors and edge cases."""

    def test_enqueue_updates_front(self):
        queue = Queue(max_size=3)
        queue.enqueue("a")
        self.assertEqual(queue.front(), "a")
        self.assertFalse(queue.is_empty())
        self.assertEqual(len(queue), 1)

    def test_fill_queue_to_capacity(self):
        queue = Queue(max_size=3)
        queue.enqueue("a")
        queue.enqueue("b")
        queue.enqueue("c")
        self.assertTrue(queue.is_full())
        self.assertEqual(len(queue), 3)

    def test_enqueue_raises_when_full(self):
        queue = Queue(max_size=1)
        queue.enqueue("a")
        with self.assertRaises(QueueFullException):
            queue.enqueue("b")

    def test_dequeue_fifo(self):
        queue = Queue(max_size=3)
        queue.enqueue("a")
        queue.enqueue("b")
        queue.enqueue("c")
        self.assertEqual(queue.dequeue(), "a")
        self.assertEqual(queue.front(), "b")
        self.assertFalse(queue.is_full())
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")
        self.assertTrue(queue.is_empty())

    def test_dequeue_raises_when_empty(self):
        queue = Queue(max_size=1)
        with self.assertRaises(QueueEmptyException):
            queue.dequeue()

    def test_front_raises_when_empty(self):
        queue = Queue(max_size=1)
        with self.assertRaises(QueueEmptyException):
            queue.front()


if __name__ == "__main__":
    unittest.main()

