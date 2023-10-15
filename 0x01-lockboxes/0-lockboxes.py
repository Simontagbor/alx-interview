#!/usr/bin/python3
"""
Module for checking if all boxex can be opened
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    AllUnlockable = False
    next_box_idx = 1
    for box in boxes:
        if box == [] and next_box_idx != len(boxes):
            AllUnlockable = False
        elif box == [] and next_box_idx == len(boxes):
            AllUnlockable = True
        else:
            for key in box:
                if key == next_box_idx:
                    AllUnlockable = True
        next_box_idx += 1
    return AllUnlockable
