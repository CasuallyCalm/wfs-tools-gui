from abc import ABC

import dearpygui.dearpygui as dpg

from .platforms import get_platform

PLATFORM = get_platform()

class ToolTab(ABC):
    name:str
    usb=True
    mlc=False

    def __init__(self) -> None:
        with dpg.tab(label=self.name, tag=self.tag, show=False):
            dpg.add_combo(items=[drive.label for drive in PLATFORM.get_drives()])


    @property
    def tag(self):
        return self.name+"_tab"    


class WFSExtract(ToolTab):

    def __init__(self) -> None:
        self.name = 'wfs-extract'
        super().__init__()

class WFSFileInjector(ToolTab):

    def __init__(self) -> None:
        self.name = 'wfs-file-injector'
        super().__init__()

class WFSFuse(ToolTab):

    def __init__(self) -> None:
        if PLATFORM.name != 'win':
            self.name = 'wfs-fuse'
            super().__init__()

class WFSInfo(ToolTab):

    def __init__(self) -> None:
        self.name = 'wfs-info'
        super().__init__()

class WFSReencryptor(ToolTab):

    def __init__(self) -> None:
        self.name = 'wfs-reencryptor'
        super().__init__()