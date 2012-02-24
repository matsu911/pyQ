pyQ: Python Q Binding
====================
This is a python wrapper for Q http://kx.com/.

Requirements
-----------
* Python 2.7.x
* Q library object file: http://kx.com/q/l64/c.o

Installation
-----------
Obtain Q object file from http://kx.com/q/l64/c.o and create shared object as follows:

$ gcc -shared c.o -o c.so

Put c.so into pyQ directory.
