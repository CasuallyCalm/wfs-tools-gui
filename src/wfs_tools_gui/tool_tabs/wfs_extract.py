
from .tool_tab_abc import ToolTabs


class WFSExtract(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-extract"
        super().__init__()
        self.run_button()