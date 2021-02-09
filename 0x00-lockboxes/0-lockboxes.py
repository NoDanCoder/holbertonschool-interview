#!/usr/bin/python3

""" lockboxes module """


def openBox(boxes, box, memo):
    """ itertate recursively truough list of boxes
        and save them on memo set
    """

    for key in boxes[box]:
        if key not in memo and key < len(boxes):
            memo.add(key)
            openBox(boxes, key, memo)

    return memo


def canUnlockAll(boxes):
    """ check box is valid then start recursive function to verify
        if all list of boxes are opened
    """

    if not boxes:
        return False
    openedBoxes = openBox(boxes, 0, {0})
    return len(boxes) == len(openedBoxes)
