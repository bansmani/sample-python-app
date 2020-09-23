import filewatcher

if __name__ == '__main__':
   found = filewatcher.waitForFile(1, 10, 'c:/tmp/testfile1.txt')
   print(found)
