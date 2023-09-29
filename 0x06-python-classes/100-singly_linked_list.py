#!/usr/bin/python3
"""
A class that defines a node of a singly linked list.
"""


class Node:
    """
    This class defines the node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        instance initilization method.
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter property that retrieves a private instance
        attribute date
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        Data property setter
        """

        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Getter property that retrieves a private instance
        attribute next_node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter
        """

        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """"
    A class that defines representation of a singly linked list
    """

    def __init__(self):
        """
        instance initilization method.
        """

        self.__head = None

    def sorted_insert(self, value):
        """
        A public instance method that inserts a new Node into
        the correct sorted position in the list (increasing order).
        """

        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None\
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        String representation of a linked list class.
        """

        string = list()
        temp = self.__head

        while temp:
            string.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(string)
