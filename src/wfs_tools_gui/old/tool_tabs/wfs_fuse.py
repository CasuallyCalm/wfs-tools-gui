from .tool_tab_abc import ToolTabs


class WFSFuse(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-fuse"
        super().__init__()