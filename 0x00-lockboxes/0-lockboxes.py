#!/usr/bin/python3

""" lockboxes module """

def openBox(boxes, box, memo):
    """ itertate recursively truough list of boxes
        and save them on memo set
    """
    try:
        keys = boxes[box]
        if type(keys) != list:
            return set()
        memo.add(box)
    except IndexError:
        return

    for key in keys:
        if key not in memo:
            openBox(boxes, key, memo)

    return memo


def canUnlockAll(boxes):
    """ check box is valid then start recursive function to verify
        if all list of boxes are opened
    """
    if type(boxes) is list and boxes != []:
        openedBoxes = openBox(boxes, 0, set())
        return len(boxes) == len(openedBoxes)
    return False
