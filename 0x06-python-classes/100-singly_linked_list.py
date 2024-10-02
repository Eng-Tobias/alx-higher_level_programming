#!/usr/bin/python3
"""
Module for SinglyLinkedList and Node classes.
"""

class Node:
    """
    Class representing a node in a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The data to set.
        
        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node.

        Args:
            value (Node or None): The next node to set.

        Raises:
            TypeError: If the value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Class representing a singly linked list.
    """
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the entire list."""
        current = self.__head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
