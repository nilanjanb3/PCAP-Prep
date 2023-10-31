class Stack():
    def __init__(self):
        """
        Initializes an instance of the class.
        """
        self.__items = []

    def push(self, data):
        """
        Adds an item to the end of the list.

        Args:
            data: The item to be added to the list.

        Returns:
            None
        """
        self.__items.append(data)

    def pop(self):
        """
        Removes and returns the last element from the stack.

        Returns:
            The last element of the stack.
        """
        return self.__items.pop()
    
    def peek(self):
        """
        Returns the last element of the list.
        """
        return self.__items[-1]
    
    def is_empty(self):
        """
        Check if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.__items == []
    
class StackSum(Stack):
    def __init__(self):
        """
        Initializes a new instance of the class.
        """
        # Stack.__init__(self) or the below line
        super().__init__()
        self.__sum = 0

    def push(self, data):
        """
        Adds the given data to the sum and calls the push method of the parent class.

        Parameters:
            data (any): The data to be added to the sum.

        Returns:
            any: The result of calling the push method of the parent class.
        """
        self.__sum+=data
        return super().push(data)
    
    def pop(self):
        """
        Removes and returns the top element from the stack.

        Returns:
            The removed element from the top of the stack.
        """
        data = super().pop()
        self.__sum-=data
        return data
    
    def sum(self):
        """
        Returns the sum of the current instance of the class.

        :return: The sum of the current instance of the class.
        """
        return self.__sum
    
if __name__ == "__main__":
    stack = StackSum()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.sum())
    stack.pop()
    print(stack.sum())
        