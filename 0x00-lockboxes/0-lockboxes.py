#!/usr/bin/python3

""" lockboxes module """


def openBox(boxes, box, memo):
    """ itertate recursively truough list of boxes
        and save them on memo set
    """

    try:
        keys = boxes[box]
        if type(keys) != list:
            memo.add(-1)
            return memo
        memo.add(box)
    except IndexError:
        return memo

    for key in keys:
        if type(key) != int:
            memo.add(-1)
            return memo
        if key not in memo:
            openBox(boxes, key, memo)

    return memo


def canUnlockAll(boxes):
    """ check box is valid then start recursive function to verify
        if all list of boxes are opened
    """
    if type(boxes) is list and boxes != []:
        openedBoxes = openBox(boxes, 0, set())
        return len(boxes) == len(openedBoxes) and -1 not in openedBoxes
    return False
