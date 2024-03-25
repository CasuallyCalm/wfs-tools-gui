from .. import arguments
from .tool_tab_abc import ToolTabs


class WFSExtract(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-extract"
        super().__init__()
        arguments.input_type(parent=self.tab)
        arguments.output(parent=self.tab)
        arguments.dump_path(parent=self.tab)
        self.run_button()

    def command(self) -> str:
        cmd = super().command()
        return f"{cmd} --input {arguments.get_input()} --type {arguments.get_type()} --output {arguments.get_outupt()} --dump-path {arguments.get_dump_path()} --verbose"

    def execute(self) -> None:
        return super().execute()
