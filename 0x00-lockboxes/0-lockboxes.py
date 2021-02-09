#!/usr/bin/python3

""" lockboxes module """

def openBox(boxes, box, memo={0}):
    """ itertate recursively truough list of boxes
        and save them on memo set
    """
    for i in boxes[box]:
        if i not in memo:
            memo.add(i)
            openBox(boxes, i, memo)

    return memo


def canUnlockAll(boxes):
    """ check box is valid then start recursive function to verify
        if all list of boxes are opened
    """
    if type(boxes) is list and boxes != []:
        openedBoxes = openBox(boxes, 0, {0})
        return len(boxes) == len(openedBoxes)
    return False
