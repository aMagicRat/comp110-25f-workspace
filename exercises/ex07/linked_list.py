"""Algorithms to process a singly-linked list data structure."""

from __future__ import annotations
from typing import Optional

__author__: str = "730859678"


class Node:
    """Node of singly-linked list."""

    value: int
    next: Optional[Node]

    def __init__(self, value: int, next: Optional[Node]) -> None:
        """Create a new node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Create string to represent the node."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"

    def __repr__(self) -> str:
        """String representation of the node for debugging."""
        return f"{self.value} -> {self.next}"
        

def value_at(head: Optional[Node], index: int) -> Optional[int]:
    """Return the value at a specific index or None if out of bounds."""
    if head is None:
        raise IndexError("Index out of bounds")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> Optional[int]:
    """Return the maximum value in the linked list or None if empty."""
    if head is None:
        raise ValueError("Can't call max if head is None")
    if head.next is None:
        return head.value
    rest_max = max(head.next)
    if rest_max is None:
        return head.value
    return rest_max if rest_max > head.value else head.value


def linkify(items: list[int]) -> Optional[Node]:
    """Turn integers into a linked list"""
    if len(items) == 0:
        return None
    Linked: Node = Node(items[0], linkify(items[1:]))
    return Linked


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Creates new list where each value is scaled by a provided value."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))