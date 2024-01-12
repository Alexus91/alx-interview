#!/usr/bin/python3
""" module for 0. Lockboxes
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Parameters:
        boxes (List[List[int]]): A list of lists.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
