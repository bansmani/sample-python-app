from os import path, listdir
import time


def waitForFile(intervalInSec, durationInSec, name):
    start = time.time()
    elapsedTime = 0

    while not path.exists(name) and elapsedTime < durationInSec:
        time.sleep(intervalInSec)
        elapsedTime = int(time.time() - start)

    return path.exists(name)


def waitUntilDirEmpty(intervalInSec, durationInSec, dir):
    start = time.time()
    elapsedTime = 0

    while listdir(dir).__len__() <= 0 and elapsedTime < durationInSec:
        time.sleep(intervalInSec)
        elapsedTime = int(time.time() - start)

    return listdir(dir).__len__() > 0
