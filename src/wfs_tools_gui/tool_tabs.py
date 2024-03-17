from abc import ABC

import dearpygui.dearpygui as dpg

from .platforms import get_platform

PLATFORM = get_platform()

class ToolTab(ABC):
    name:str
    usb=True
    mlc=False

    def __init__(self) -> None:
        self.input = ''
        self.drives = PLATFORM.get_drives()

        with dpg.tab(label=self.name, tag=self.tag, show=False):
            with dpg.group(horizontal=True):
                dpg.add_text('Input:')
                self.combo_box = dpg.add_combo(items=[drive.label for drive in self.drives], callback=self.__set_input)
                dpg.add_button(label='refresh', callback=self.__refresh_drives)

    def __refresh_drives(self):
        dpg.set_value(self.combo_box, "")
        self.drives = PLATFORM.get_drives()
        dpg.configure_item(self.combo_box, items=[drive.label for drive in self.drives])

    def __set_input(self, sender, app_data, user_data):
        for drive in self.drives:
            if drive == app_data:
                self.input = drive.path

        print(self.input)

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