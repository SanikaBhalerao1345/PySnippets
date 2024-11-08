from dataclasses import dataclass
from typing import Optional, Any, List
import logging

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Node:
    data: Any
    next: Optional['Node'] = None
    prev: Optional['Node'] = None

def insert_end(head: Optional[Node], data: Any) -> Node:
    """Insert a node at the end of the doubly linked list."""
    new_node = Node(data)
    if head is None:
        logging.info(f"Inserted {data} as the first node.")
        return new_node

    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
    new_node.prev = last_node
    logging.info(f"Inserted {data} at the end of the list.")
    return head

def delete_node(head: Optional[Node], key: Any) -> Optional[Node]:
    """Delete a node with a specific value from the doubly linked list."""
    if head is None:
        logging.warning("Attempted to delete from an empty list.")
        return None

    current_node = head

    # Case: The head node has the key to be deleted
    if current_node.data == key:
        head = current_node.next
        if head:
            head.prev = None
        logging.info(f"Deleted head node with key {key}.")
        return head

    # Case: Search for the key in the rest of the list
    while current_node is not None and current_node.data != key:
        current_node = current_node.next

    # Key not found
    if current_node is None:
        logging.warning(f"Key {key} not found in the list.")
        return head

    # Adjust pointers to remove current_node
    if current_node.next:
        current_node.next.prev = current_node.prev
    if current_node.prev:
        current_node.prev.next = current_node.next
    logging.info(f"Deleted node with key {key}.")
    return head

def display(head: Optional[Node]) -> List[Any]:
    """Display the doubly linked list as a list of node data."""
    result = []
    current_node = head
    while current_node:
        result.append(current_node.data)
        current_node = current_node.next
    logging.info(f"List contents: {result}")
    return result