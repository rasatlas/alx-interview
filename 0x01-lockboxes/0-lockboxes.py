#!/usr/bin/python3
"""A method that determines if all boxes can be opened."""


def canUnlockAll(boxes):
    """
    Parameters:
    boxes (List[List[int]]): The list of lists representing the boxes
        and their keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    set = {0}
    boxes_length = len(boxes)

    for j in range(boxes_length):
        if j in set:
            box = boxes[j]
            for i in range(len(box)):
                index = box[i]
                if (boxes[index] in boxes):
                    set.add(index)
                    if (len(set) == boxes_length):
                        return True
    return False
