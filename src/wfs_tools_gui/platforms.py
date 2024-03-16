import subprocess
import sys
from abc import ABC
from typing import List

from .tools import TOOLS


class Drive:
    
    def __init__(self, label:str, path:str) -> None:
        self.label = label
        self.path = path

class PlatformBase(ABC):

    name:str
    extension:str

    @property
    def executables(self)-> List[str]:
        return [tool+self.extension for tool in TOOLS]
    
    def get_drives(self)->List[Drive]:
        pass


class Windows(PlatformBase):
    name = "win"
    extension = ".exe"

    def get_drives(self) -> List[Drive]:
        proc = subprocess.run('powershell Get-WmiObject Win32_DiskDrive', capture_output=True)
        dicts = [{line.split(':')[0].strip():line.split(':')[1].strip() for line in drive.split('\n')}  for drive in bytes.decode(proc.stdout).strip().replace('\r','').split('\n\n') ]
        return [Drive(drive['Caption'], drive['DeviceID']) for drive in dicts]

class Linux(PlatformBase):
    name = "linux"
    extension = ""


def get_platform()->PlatformBase:
    platforms = dict(win32=Windows(), linux = Linux())
    return platforms[sys.platform]

