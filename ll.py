import os
import threading
from optparse import OptionParser
parse = OptionParser(usage='python3 ll.py -f test_atk.exe(default) -t 300')
parse.add_option('-f', '--file', dest='filename', default="test_atk.exe", type='string', help='Atk file name')
parse.add_option('-t', '--threads', dest='thread', default="300", type='string', help='Start threads')
options, args = parse.parse_args()
Filename = options.filename
thread = options.thread

def Go(filename):
    os.system("cmd /c "+filename)
    
if __name__ == "__main__":
    threads = []
    print("Start")
    for thread_ in range(int(thread)):
        t = threading.Thread(target=Go, args=(Filename,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("End")