from ctypes import *
import os

# See http://kx.com/q/c/c/k.h

class _S(Structure):
    _fields_ = [("n", c_int),
                ("G0", c_ubyte * 1),]

class _U(Union):
    _fields_ = [("g", c_ubyte),
                ("h", c_short),
                ("i", c_int),
                ("j", c_longlong),
                ("e", c_float),
                ("f", c_double),
                ("s", c_char_p),
                ("k", c_void_p),
                ("array", _S)]

class _K(Structure):
    _fields_ = [("r", c_int),
                ("t", c_short),
                ("u", c_short),
                ("union", _U)]

K = POINTER(_K)

libk = CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), "c.so"))

libk.k.restype   = K
libk.ktd.restype = K

def kG(obj):
    return cast(obj.contents.union.array.G0, POINTER(K))

setattr(K, "__len__", lambda self: self.contents.union.array.n)
setattr(K, "__getitem__", lambda self, key: kG(self)[key])
setattr(K, "type", lambda self: self.contents.t)


def converter(t):
    if t == 1:
        return lambda x: cast(x, c_ubyte).value
    elif t == 4:
        return lambda x: cast(x, c_byte).value
    elif t == 5:
        return lambda x: cast(x, c_short).value
    elif t == 6:
        return lambda x: cast(x, c_int).value
    elif t == 7:
        return lambda x: cast(x, c_longlong).value
    elif t == 8:
        return lambda x: cast(x, c_float).value
    elif t == 9:
        return lambda x: cast(x, c_double).value
    elif t == 11:
        return lambda x: cast(x, c_char_p).value
    else:
        raise "unknown type"

def K_iter(self):
    for i in range(0, len(self)):
        yield self[i]

setattr(K, "__iter__", K_iter)
