from .. import arguments
from .tool_tab_abc import ToolTabs


class WFSFileInjector(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-file-injector"
        super().__init__()
        arguments.input_type(parent=self.tab)
        arguments.inject_file(parent=self.tab)
        arguments.inject_path(parent=self.tab)
        self.run_button()

    def command(self) -> str:
        cmd = super().command()
        return f"{cmd} --image {arguments.get_input()} --type {arguments.get_type()} --inject-file {arguments.get_inject_file()} --inject-path {arguments.get_inject_path()}"
