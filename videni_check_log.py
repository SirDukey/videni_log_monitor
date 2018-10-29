import subprocess as sp
from datetime import datetime
from time import sleep

def getItem():
    log = sp.Popen(['tail', '/root/logs/move-indexed-files.log'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = log.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        output = output.split('\n')
        return output[-2]

    elif error:
        return 1


if __name__ == '__main__':
    itemA = getItem()
    sleep(10)
    itemB = getItem()

    if itemA == itemB:
        print(0)
    else:
        print(1)

