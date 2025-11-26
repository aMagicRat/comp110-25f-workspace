"""Algorithms to process a singly-linked list data structure"""


from __future__ import annotations


__author__: str = "730859678"

class Node: 
        """Node of singly-linked list"""

        value: int 
        next: Node | None

        def __init__(self, value: int, next: Node | None) -> None:
            """Create a new node"""
            self.value = value
            self.next = next

        def __str__(self) -> str:
            """Creates string to represent the node"""
            if self.next is None:
                return f"{self.value} -> None"
            else:
                return f"{self.value} -> {self.next}"
            
        def __repr__(self) -> str:
            """Creates a string representation of the node for debugging"""
            return f"{self.value} -> {self.next}"
        
        def value_at(self, head: Node | None, index: int) -> int:
            """Returns value at a specific point in the linked list"""
            if head is None:
                raise IndexError("Index out of bounds")
            if index == 0:
                return head.value
            else:
                return self.value_at(head.next, index - 1)


        def max(self, head: Node | None) -> int:
            """Returns the maximum value in the linked list"""
            if head is None:
                raise ValueError("""Cant call max if head is None""")
            potential: int = 0
            if head.next is None:
                return head.value
            else:
                potential = self.max(head.next)
            if potential > head.value:
                    head.value = potential
            return head.value


        def linkify(self, items: list[int]) -> Node | None:
            """Turns integers into a linked list"""
            if len(items) == 0:
                return None
            Linked: Node = Node(items[0], self.linkify(items[1:]))
            return Linked
                
        def scale(self, head: Node | None, factor: int) -> Node | None:
            """Scales list by provided value"""
            if head is None:
                return None
            Scaled: Node = Node(head.value * factor, self.scale(head.next, factor))
            return Scaled