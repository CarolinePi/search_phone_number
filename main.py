from functools import wraps


def check_type(func):
    """Decorator for function which check type of numbers. """

    @wraps(func)
    def inner(self, number, *args, **kwargs):
        try:
            int(number)
            func(self, number)
        except ValueError:
            # print('The wrong number: ' + number)
            pass

    return inner


class Node:
    """ Node contains dict children, where key = digit, value = Node-links of children. """

    def __init__(self):
        self.children = {}
        self.is_finished = False


class SuffixTree:
    def __init__(self):
        self.__root = Node()
        self.__numbers = []

    @check_type
    def add(self, number: str):
        """Adding new phone number. """

        node = self.__root
        for digit in list(number):
            if not node.children.get(digit):
                node.children[digit] = Node()
            node = node.children[digit]
        node.is_finished = True

    def search(self, prefix: str):
        """ Search numbers"""

        node = self.__root
        self.__numbers.clear()
        is_found = False
        temp = ''
        for digit in list(prefix):
            if not node.children.get(digit):
                is_found = True
                break
            temp += digit
            node = node.children[digit]

        if is_found:
            return 0
        elif node.is_finished and not node.children:
            return -1

        self.suggest(node, temp)

    def suggest(self, node: Node, number: str):
        """ Function which add ending word. """

        if node.is_finished:
            self.__numbers.append(number)

        for digit, n in node.children.items():
            self.suggest(n, number + digit)

    @property
    def numbers(self):
        return self.__numbers[:10]
