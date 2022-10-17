class NullElementException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class EmptyStackException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class Stack:

    def __init__(self):
        self.__stack = list()

    def size(self) -> int:
        return len(self.__stack)

    def push(self, element):
        if element:
            self.__stack.append(element)
        else:
            raise NullElementException("The supplied element is Null/None")

    def pop(self):
        if self.empty():
            raise EmptyStackException("The stack is Empty")
        else:
            val = self.__stack[self.size() - 1]
            del self.__stack[self.size() - 1]
            return val

    def peek(self):
        if self.empty():
            raise EmptyStackException("The stack is Empty")
        else:
            return self.__stack[self.size() - 1]

    def empty(self) -> bool:
        return self.size() == 0
