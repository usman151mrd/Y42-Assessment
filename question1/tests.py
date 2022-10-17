from unittest import TestCase

from question1.stack import EmptyStackException, NullElementException, Stack


class StackTestCases(TestCase):
    def test_size_of_stack(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.size(), 1)

    def test_push_operations(self):
        stack = Stack()
        self.assertIsNone(stack.push(6))
        with self.assertRaises(NullElementException):
            stack.push(None)

    def test_pop_operations(self):
        stack = Stack()
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        with self.assertRaises(EmptyStackException):
            stack.pop()

    def test_peek_value_operations(self):
        stack = Stack()
        with self.assertRaises(EmptyStackException):
            stack.peek()
        stack.push(10)
        self.assertEqual(stack.peek(), 10)

    def test_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        stack.push(100)
        self.assertFalse(stack.empty())
