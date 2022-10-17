class NullElementException(Exception):
    """
    Custom Exceptional class used for null element
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class EmptyStackException(Exception):
    """
    Custom Exceptional class used when stack is empty
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class Stack:
    """
    used class to implement stack data structure
    """

    def __init__(self):
        self.__stack = list()

    def size(self) -> int:
        """

        :return:
        """
        return len(self.__stack)

    def push(self, element):
        """

        :param element:
        """
        if element:
            self.__stack.append(element)
        else:
            raise NullElementException("The supplied element is Null/None")

    def pop(self):
        """

        :return:
        """
        if self.empty():
            raise EmptyStackException("The stack is Empty")
        else:
            val = self.__stack[self.size() - 1]
            del self.__stack[self.size() - 1]
            return val

    def peek(self):
        """
        :return:
        """
        if self.empty():
            raise EmptyStackException("The stack is Empty")
        else:
            return self.__stack[self.size() - 1]

    def empty(self) -> bool:
        """

        :return:
        """
        return self.size() == 0
