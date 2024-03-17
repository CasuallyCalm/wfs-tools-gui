from abc import ABC

import dearpygui.dearpygui as dpg


class ToolTab(ABC):
    name: str

    def __init__(self) -> None:
        self.input = ""

        with dpg.tab(label=self.name, tag=self.tag, show=False):
            dpg.add_text(f"this is the {self.tag}")

    @property
    def tag(self):
        return self.name + "_tab"


class WFSExtract(ToolTab):
    def __init__(self) -> None:
        self.name = "wfs-extract"
        super().__init__()


class WFSFileInjector(ToolTab):
    def __init__(self) -> None:
        self.name = "wfs-file-injector"
        super().__init__()


class WFSFuse(ToolTab):
    def __init__(self) -> None:
        self.name = "wfs-fuse"
        super().__init__()


class WFSInfo(ToolTab):
    def __init__(self) -> None:
        self.name = "wfs-info"
        super().__init__()


class WFSReencryptor(ToolTab):
    def __init__(self) -> None:
        self.name = "wfs-reencryptor"
        super().__init__()
