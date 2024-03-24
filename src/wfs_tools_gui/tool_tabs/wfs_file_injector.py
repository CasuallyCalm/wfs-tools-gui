from .tool_tab_abc import ToolTabs


class WFSFileInjector(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-file-injector"
        super().__init__()
