import lib1.f_lib
import lib2
from lib2 import h
from lib2 import x

if __name__ == "__main__":
    lib1.f_lib.f()
    lib2.g()
    h()
    x()
