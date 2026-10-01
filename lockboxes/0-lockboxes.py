#!/usr/bin/python3
"""
Module 0-lockboxes
Contains a method that determines if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    boxes is a list of lists where each sublist contains keys.
    """
    if not boxes:
        return False

    unlocked = [0]
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.append(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)

