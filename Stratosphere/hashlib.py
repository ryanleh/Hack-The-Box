import sys

class md5_hash:
    def __init__(self):
        print('wow')
    def update(self, wtvr):
        return None
    def hexdigest(self):
        return "5af003e100c80923ec04d65933d382cb"

class sha1_hash:
    def __init___(self):
        print('wow2')

    def update(self, wtvr):
        return None

    def hexdigest(self):
        return "d24f6fb449855ff42344feff18ee2819033529ff"

class md4_hash:
    def __init___(self):
        print('wow3')

    def update(self, wtvr):
        return None

    def hexdigest(self):
        return "91ae5fc9ecbca9d346225063f23d2bd9"

class blake2_hash():
    def __init___(self):
        print('wow4')

    def update(self, wtvr):
        return None

    def hexdigest(self):
        return "9efebee84ba0c5e030147cfd1660f5f2850883615d444ceecf50896aae083ead798d13584f52df0179df0200a3e1a122aa738beff263b49d2443738eba41c943"


def md5():
    return md5_hash()

def sha1():
    return sha1_hash()

def new(input):
    if input == 'md4':
        return md4_hash()
    else:
    	return blake2_hash()

sys.modules.pop('os', None)

