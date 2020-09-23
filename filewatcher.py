
from os import path
import time

def waitForFile(intervalInSec, durationInSec, name) :
    start = time.time()
    elapsedTime =0

    while not path.exists(name) and elapsedTime < durationInSec :
        time.sleep(intervalInSec)
        elapsedTime = int(time.time() - start)

    return path.exists(name)
