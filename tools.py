import ctypes
import subprocess
import sys
from abc import ABC


class PlatformBase(ABC):
    name: str
    extension: str

    def get_drives(self) -> dict[str, str]:
        return {}


class Windows(PlatformBase):
    name = "win"
    extension = ".exe"

    def get_drives(self) -> dict:
        proc = subprocess.run(
            "powershell Get-WmiObject Win32_DiskDrive", capture_output=True
        )
        drives = [
            {
                line.split(":")[0].strip(): line.split(":")[1].strip()
                for line in drive.split("\n")
            }
            for drive in bytes.decode(proc.stdout)
            .strip()
            .replace("\r", "")
            .split("\n\n")
        ]
        return {drive["Caption"]: drive["DeviceID"] for drive in drives}


class Linux(PlatformBase):
    name = "linux"
    extension = ""


def get_platform() -> PlatformBase:
    platforms = dict(win32=Windows(), linux=Linux())
    return platforms[sys.platform]


PLATFORM = get_platform()


def is_admin():
    if PLATFORM.name == "win":
        return ctypes.windll.shell32.IsUserAnAdmin()
    return True
