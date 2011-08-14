#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform

class _Getch():
    def __init__(self):
        if platform.system() == "Linux":
            self.implementation = _GetchUnix()
        elif platform.system() == "Windows":
            self.implementation = _GetchWindows()
        else:
            raise Exception("This platform isn't supported.")
        
    def __call__(self):
        return self.implementation()
        
class _GetchUnix:
    def __init__(self):
        import sys
        import termios
        import tty
    
    def __call__(self):
        import sys
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char
    
class _GetchWindows():
    
    def __init__(self):
        import msvcrt
    
    def __call__(self):
        import msvcrt
        char = msvcrt.getch()
        return char 

if __name__ == '__main__':
    getch = _Getch()
    char = getch()
    print(char)