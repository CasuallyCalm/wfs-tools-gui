import subprocess
import sys
from abc import ABC
from typing import List

TOOLS = ["wfs-extract", "wfs-file-injector", "wfs-fuse", "wfs-info", "wfs-reencryptor"]

# class Drive:
#     def __init__(self, label: str, path: str) -> None:
#         self.label = label
#         self.path = path

#     def __eq__(self, __value: object) -> bool:
#         return __value == self.label


class PlatformBase(ABC):
    name: str
    extension: str

    @property
    def executables(self) -> List[str]:
        return [tool + self.extension for tool in TOOLS]

    def get_drives(self) -> dict[str, str]:
        pass


class Windows(PlatformBase):
    name = "win"
    extension = ".exe"

    def get_drives(self) -> dict[str, str]:
        proc = subprocess.run(
            "powershell Get-WmiObject Win32_DiskDrive", capture_output=True
        )
        dicts = [
            {
                line.split(":")[0].strip(): line.split(":")[1].strip()
                for line in drive.split("\n")
            }
            for drive in bytes.decode(proc.stdout)
            .strip()
            .replace("\r", "")
            .split("\n\n")
        ]
        return {drive["Caption"]: drive["DeviceID"] for drive in dicts}


class Linux(PlatformBase):
    name = "linux"
    extension = ""


def get_platform() -> PlatformBase:
    platforms = dict(win32=Windows(), linux=Linux())
    return platforms[sys.platform]


PLATFORM = get_platform()
