#!/usr/bin/python3
"""A method that determines if all boxes can be opened."""


def canUnlockAll(boxes):
    """
    There are n number of locked boxes. Each box is numbered sequentially
    from 0 to n - 1 and each box may contain keys to the other boxes.

    Parameters:
    boxes (List[List[int]]): The list of lists representing the boxes
    and their keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    visited = {0}
    boxes_length = len(boxes)

    for box_index in range(boxes_length):
        if box_index in visited:
            box = boxes[box_index]
            for key in range(len(box)):
                index = box[key]
                if (boxes[index] in boxes):
                    visited.add(index)
                    if (len(visited) == boxes_length):
                        return True
    return False
