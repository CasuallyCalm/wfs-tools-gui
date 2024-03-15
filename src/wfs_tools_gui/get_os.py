import sys
from abc import ABC


class OSBase(ABC):

    name:str
    exe:str

class Windows(OSBase):
    name = "win"
    exe= "exe"

class Linux(OSBase):
    name = "linux"
    exe= "bin"


def get_os()->OSBase:
    platforms = dict(win32=Windows(), linux = Linux())
    return platforms[sys.platform]