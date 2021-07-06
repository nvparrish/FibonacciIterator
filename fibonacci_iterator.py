class FibonacciIterable:
    """ 
    An iterable that generates values in a fibonacci sequence 
    """
    def __init__(self, number = 0):
        """ 
        Initialize the interable
        # Arguments:
        number - the number of values to generate
        """
        self.number = number
        self.__iter__()

    def __iter__(self):
        """ 
        Set up the iterable by returning to an initial state 
        """
        self.count = 0
        self.current = 1
        self.previous = 0
        return self

    def __next__(self):
        """ 
        Get the next value in the sequence
        If the requested number of values is exceeded, raises StopIteration
        """
        if self.count >= self.number:
            raise StopIteration
        self.count += 1
        current = self.current
        self.previous, self.current = self.current, self.previous + self.current
        return current

def main(number):
    """ 
    Main function to demonstrate usage.
    # Arguments
    number - the number of values to generate
    """
    for i in FibonacciIterable(number):
        print(i)

if __name__ == "__main__":
    main(20)
