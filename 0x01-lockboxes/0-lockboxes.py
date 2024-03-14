#!/usr/bin/python3
"""A method that determines if all boxes can be opened."""


def canUnlockAll(boxes):
    set = {0}
    boxes_length = len(boxes)

    for j in range(boxes_length):
        box = boxes[j]
        for i in range(len(box)):
            index = box[i]
            if (boxes[index] in boxes):
                set.add(index)
                if (len(set) == boxes_length):
                    return True
    return False
