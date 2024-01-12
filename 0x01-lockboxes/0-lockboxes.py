#!/usr/bin/python3
"""
Module for checking if all boxex can be opened
"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = [False] * n
    opened_boxes[0] = True
    keys = [key for key in boxes[0]]

    while keys:
        key = keys.pop()
        if key < n and not opened_boxes[key]:
            opened_boxes[key] = True
            keys.extend(boxes[key])

    return all(opened_boxes)