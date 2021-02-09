#!/usr/bin/python3

def openBox(boxes, box, memo={0}):
    for i in boxes[box]:
        if i not in memo:
            memo.add(i)
            openBox(boxes, i, memo)

    return memo


def canUnlockAll(boxes):
    if type(boxes) is list and boxes != []:
        openedBoxes = openBox(boxes, 0, {0})
        return len(boxes) == len(openedBoxes)
    return False
