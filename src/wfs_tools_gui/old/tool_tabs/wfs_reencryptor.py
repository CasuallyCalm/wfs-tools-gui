from .tool_tab_abc import ToolTabs


class WFSReencryptor(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-reencryptor"
        super().__init__()
